# Color Extractor Project

## Overview
This project includes a Python script to extract dominant colors from an image and generate a color palette. It uses OpenCV for image processing, scikit-learn for K-means clustering, and Matplotlib for visualizing the color palette.

## Dependencies
- numpy
- opencv-python
- scikit-learn
- matplotlib

These dependencies are listed in the `requirements.txt` file.

## Installation

### Local Setup
1. Clone the repository to your local machine.
2. Install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your target image in the project directory or specify its path when running the script.

### Running on Replit
For running the project on Replit, a special configuration is required to handle the `libGL.so.1` error.

1. Add `pkgs.libGL` to the `deps` array and `PYTHON_LD_LIBRARY_PATH` in the existing `replit.nix` file in your Replit project. This will install the necessary OpenGL library. Here is an example snippet to add:
   ```nix
   pkgs.libGL
   ```
2. Run or restart your Replit to apply these settings.

## Usage

### Command Line Arguments
Run the script with the following arguments:
- `-i` or `--image`: Path to the image file.
- `-c` or `--colors`: Number of colors to extract.
- `-o` or `--output`: (Optional) Output path for the color palette image and hex codes.

### Example
```bash
python extract_colors.py -i path/to/image.jpg -c 5 -o path/to/output/
```

## Output
The script generates a `/path/to/output/` showing the dominant colors and a `colors_hex.txt` file containing their HEX codes in the specified output directory.
