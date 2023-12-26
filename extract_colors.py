import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse

def extract_colors(image_path, num_colors, output_path):
    # Read the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize the image to reduce computation
    image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)

    # Reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # Cluster the pixel intensities
    clt = KMeans(n_clusters=num_colors)
    clt.fit(image)

    # Build a histogram of clusters
    hist = centroid_histogram(clt)
    bar, colors_hex = plot_colors(hist, clt.cluster_centers_)

    # Output the color palette image
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.savefig(output_path + "color_palette.png")

    # Output the hex color codes to a text file
    with open(output_path + "colors_hex.txt", "w") as file:
        file.write('\n'.join(colors_hex))

def centroid_histogram(clt):
    # Grab the number of different clusters and create a histogram
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    # Normalize the histogram
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist

def plot_colors(hist, centroids):
    # Initialize the bar chart representing the relative frequency of each color
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    colors_hex = []

    # Loop over each cluster's percentage and color
    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        startX = endX

        # Convert the color from RGB to HEX
        hex_color = "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
        colors_hex.append(hex_color)

    # Return the bar chart and hex color codes
    return bar, colors_hex

# Command-line argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract the main colors from an image and create a color palette.')
    parser.add_argument('-i', '--image', type=str, help='Path to the image file.', required=True)
    parser.add_argument('-c', '--colors', type=int, help='Number of colors to extract.', required=True)
    parser.add_argument('-o', '--output', type=str, help='Output path for the color palette image and hex codes.', default='./')

    args = parser.parse_args()

    # Run the color extraction
    extract_colors(args.image, args.colors, args.output)
