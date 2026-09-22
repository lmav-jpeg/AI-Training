"""
This work evaluates pixel similarity and feature similarity.
"""
import torchvision
from medmnist import *
from sklearn.metrics import pairwise_distances
from matplotlib.pyplot import *
from torchvision import *
from PIL import Image
dataset = BreastMNIST( split="train", download=True)
print(dataset)

print("Pixel similarity")
X, y = dataset.imgs , dataset.labels
shape = X.shape
print("number of images", shape[0])
print('number of features per row', shape[1])
print('number of features per columns', shape[2])
print("Original shape", X.shape)

# Data preprocessing
X = X.astype(np.float32) / 255.0

# To calculate the pairwise distance, we need to represent
# each image as a 1D vector instead of a 2D array of pixels.
# We will need to keep the first dimension and flatten the remaining dimensions
# For a 28x28 image, this gives us 784 features.
X = X.reshape(X.shape[0], -1)
print("Flattened shape:", X.shape)
distances = pairwise_distances(X, metric="cosine")
similarities = 1 - distances


# Compare two images. Can be generalized with a double for loop
i = 0
j = 2

similarity = similarities[i, j]

fig, axes = subplots(1, 2)

axes[0].imshow(dataset.imgs[i], cmap="gray", interpolation="bicubic")
axes[0].set_title(f"Image {i}\nLabel: {y[i][0]}")

axes[1].imshow(dataset.imgs[j], cmap="gray", interpolation="bicubic")
axes[1].set_title(f"Image {j}\nLabel: {y[j][0]}")

fig.suptitle(f"Pixel Cosine Similarity = {similarity:.2f}")

for ax in axes:
    ax.axis("off")

show()

imgs, labels = dataset.imgs, dataset.labels

nput = []

model = torchvision.models.resnet18(
    weights=torchvision.models.ResNet18_Weights.DEFAULT
)

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

# Compare two images
i = 0
j = 2

similarity = similarities[i, j]

fig, axes = subplots(1, 2)

axes[0].imshow(dataset.imgs[i], cmap="gray", interpolation="bicubic")
axes[0].set_title(f"Image {i}\nLabel: {y[i][0]}")

axes[1].imshow(dataset.imgs[j], cmap="gray", interpolation="bicubic")
axes[1].set_title(f"Image {j}\nLabel: {y[j][0]}")

fig.suptitle(f"feature Cosine Similarity = {similarity:.2f}")

for ax in axes:
    ax.axis("off")

show()