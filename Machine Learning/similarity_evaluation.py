from medmnist import *
from sklearn.metrics import pairwise_distances
from matplotlib.pyplot import *

dataset = BloodMNIST( split="train", download=True)
print(dataset)

X, y = dataset.imgs , dataset.labels
shape = X.shape
print("number of images", shape[0])
print('number of features per row', shape[1])
print('number of features per columns', shape[2])

#data cleaning
X = X.astype(np.float32) / 255.0

# To calculate the pairwise distance, we need to represent
# each image as a 1D vector instead of a 2D array of pixels.
#We will need to keep the first dimension and flatten the remaining dimensions
# For a 28x28 image, this gives us 784 features.
X = X.reshape(X.shape[0], -1)
print("Flattened shape:", X.shape)
distances = pairwise_distances(X, metric="cosine")
similarities = 1 - distances


# Compare two images
i = 0
j = 1

similarity = similarities[i, j]

fig, axes = subplots(1, 2)

axes[0].imshow(dataset.imgs[i], cmap="gray", interpolation="bicubic")
axes[0].set_title(f"Image {i}\nLabel: {y[i][0]}")

axes[1].imshow(dataset.imgs[j], cmap="gray", interpolation="bicubic")
axes[1].set_title(f"Image {j}\nLabel: {y[j][0]}")

fig.suptitle(f"Cosine Similarity = {similarity:.2f}")

for ax in axes:
    ax.axis("off")

show()