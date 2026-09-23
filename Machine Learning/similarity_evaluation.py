"""
This is a prototype to an investigation of how the choice of representation
affects medical-image similarity. I first established a pixel-space baseline,
then fine-tuned a ResNet-18 representation on BreastMNIST and compared the resulting
 similarity distributions for same-label and different-label image pairs.
 GPT and Gemini were used to implement my ideas in code, while I designed the
 experiment, interpreted the results, and evaluated the limitations of the approach.
 This provides the foundation for the upcoming
 interactive Medical Image Similarity Explorer.

"""
import torchvision
from medmnist import *
from sklearn.metrics import pairwise_distances
from matplotlib.pyplot import *
from torch.utils.data import TensorDataset, DataLoader
from torchvision import *
from PIL import Image

def pixel_similarity(dataset):
    print("Pixel Cosine Similarity in process...")
    X, y = dataset.imgs , dataset.labels
    shape = X.shape
    #print("number of images", shape[0])
    #print('number of features per row', shape[1])
    #print('number of features per columns', shape[2])
    #print("Original shape", X.shape)

    # Data preprocessing
    X = X.astype(np.float32) / 255.0

    # To calculate the pairwise distance, we need to represent
    # each image as a 1D vector instead of a 2D array of pixels.
    # We will need to keep the first dimension and flatten the remaining dimensions
    # For a 28x28 image, this gives us 784 features.
    X = X.reshape(X.shape[0], -1)
    #print("Flattened shape:", X.shape)
    distances = pairwise_distances(X, metric="cosine")
    similarities = 1 - distances
    return similarities


def fine_tune_model(model, dataset, epochs=10, batch_size=64, lr=1e-4):
    """
    Take a model and return another task ready model
    AI-assisted implementation. Gemini was used to help generate the initial
    fine-tuning procedure. I reviewed, tested, and modified the generated code.
    :param model:
    :param dataset:
    :param epochs:
    :param batch_size:
    :param lr:
    :return: model
    """
    print("Fine-tuning ResNet-18 on BreastMNIST...")

    # Prepare data for PyTorch training
    # Convert 28x28 grayscale to 3-channel RGB and apply standard preprocessing
    preprocess = torchvision.models.ResNet18_Weights.DEFAULT.transforms()

    X_processed = []
    for img in dataset.imgs:
        pil_img = Image.fromarray(img).convert("RGB")
        tensor_img = preprocess(pil_img)
        X_processed.append(tensor_img)

    X_tensor = torch.stack(X_processed)
    y_tensor = torch.tensor(dataset.labels, dtype=torch.float32)

    train_loader = DataLoader(TensorDataset(X_tensor, y_tensor), batch_size=batch_size, shuffle=True)

    # Modify final layer for binary classification
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.fc = torch.nn.Linear(model.fc.in_features, 1)
    model.to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = torch.nn.BCEWithLogitsLoss()

    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for batch_x, batch_y in train_loader:
            batch_x, batch_y = batch_x.to(device), batch_y.to(device)

            optimizer.zero_grad()
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
        print(f"Epoch {epoch + 1}/{epochs} - Loss: {total_loss / len(train_loader):.4f}")

    # Strip the classification head so it acts as an embedding extractor again
    model.fc = torch.nn.Identity()
    model.to("cpu")
    return model

def feature_similarity(dataset, model):
    print("Feature Cosine Similarity in process...")
    imgs, labels = dataset.imgs, dataset.labels

    nput = []

    model.eval()
    model.fc = torch.nn.Identity()

    with torch.no_grad():
        preprocess = torchvision.models.ResNet18_Weights.DEFAULT.transforms()

        for i, img in enumerate(imgs):
            img = Image.fromarray(img).convert("RGB")

            input_tensor = preprocess(img)
            input_batch = input_tensor.unsqueeze(0)

            embedding = model(input_batch)

            nput.append(embedding.squeeze(0).numpy())

        nput = np.array(nput)

    distances = pairwise_distances(nput, metric="cosine")
    similarities = 1 - distances
    return similarities

def evaluations(same_label, different_label, similarity_type):
    print(f'Results for {similarity_type}:')
    print("Evaluations in process...")
    print("=== Same-label similarity ===")
    print("Mean:", np.mean(same_label))
    print("Median:", np.median(same_label))
    print("Std:", np.std(same_label))
    print("Min:", np.min(same_label))
    print("Max:", np.max(same_label))

    print("\n=== Different-label similarity ===")
    print("Mean:", np.mean(different_label))
    print("Median:", np.median(different_label))
    print("Std:", np.std(different_label))
    print("Min:", np.min(different_label))
    print("Max:", np.max(different_label))

def visualize_distributions(same_label, different_label, similarity_type):
    print(f"Visualizations for {similarity_type} in process...")
    hist(same_label, bins=30, alpha=0.5, label="Same label")
    hist(different_label, bins=30, alpha=0.5, label="Different label")

    xlabel("Cosine similarity")
    ylabel("Number of image pairs")
    title(f"{similarity_type} Similarity Distribution")
    legend()
    show()

def plotting(similarities, i, j, similarity_type,y,x):
    similarity = similarities[i, j]
    fig, axes = subplots(1, 2)

    axes[0].imshow(x[i], cmap="gray", interpolation="bicubic")
    axes[0].set_title(f"Image {i}\nLabel: {y[i][0]}")

    axes[1].imshow(x[j], cmap="gray", interpolation="bicubic")
    axes[1].set_title(f"Image {j}\nLabel: {y[j][0]}")

    fig.suptitle(f"{similarity_type} Cosine Similarity = {similarity:.2f}")

    for ax in axes:
        ax.axis("off")

    show()


if __name__ == '__main__':
    dataset = BreastMNIST( split="train", download=True)
    X, y = dataset.imgs, dataset.labels
    model = torchvision.models.resnet18(
        weights=torchvision.models.ResNet18_Weights.DEFAULT
    )
    model = fine_tune_model(model,dataset)
    pixel_cosine_similarities = pixel_similarity(dataset)
    same_label = []
    different_label = []

    for i in range(len(y)):
        for j in range(i + 1, len(y)):

            similarity = pixel_cosine_similarities[i, j]

            if y[i][0] == y[j][0]:
                same_label.append(similarity)
            else:
                different_label.append(similarity)
    evaluations(same_label,different_label, "pixel")
    visualize_distributions(same_label, different_label,"pixel")

    feature_cosine_similarities = feature_similarity(dataset, model)

    same_label = []
    different_label = []

    for i in range(len(y)):
        for j in range(i + 1, len(y)):

            similarity = feature_cosine_similarities[i, j]

            if y[i][0] == y[j][0]:
                same_label.append(similarity)
            else:
                different_label.append(similarity)
    evaluations(same_label, different_label, "feature")
    visualize_distributions(same_label, different_label,"feature")
    image1_index = 0
    image2_index = 1
    print("\n=== PLOTTING ===")
    plotting(pixel_cosine_similarities, image1_index, image2_index,"Pixel Cosine Similarity", dataset.labels, dataset.imgs)
    plotting(feature_cosine_similarities, image1_index, image2_index,"Feature Cosine Similarity", dataset.labels, dataset.imgs)