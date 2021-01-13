#!/usr/bin/env python
import numpy as np
import argparse
import math
from PIL import Image
from numpy.core.fromnumeric import shape
from typing import Any
from pathlib import Path

class ImageToAscii():

    def __init__(self) -> None:
        self.gray_scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        self.gray_scale2 = '@%#*+=-:. '

    def get_average_L(self, image: Image) -> tuple or Any:

        img = np.array(image)
        w, h = img.shape

        return np.average(img.reshape(w*h))

    def convert_image_to_ascii(self, file_path: str, cols: int, scale: int, more_levels:bool) -> list:
        image: Image = None
        try:
            image = Image.open(file_path).convert("L")
        except Exception as err:
            print(f"An error has occured while opening image: {err}")

        W, H = image.size[0], image.size[1]

        print(f"\nThe dimensions of the image are:\n\nWitdth - {W}\nHeight - {H}")

        w = W/cols
        h = w/scale

        rows = int(H/h)

        print(f"\n\nTile Dimensions:\n\nWidth - {w}\nHeight - {h}")

        if cols > W or rows > H:
            print("Image is too small...")
            exit(0)

        ascii_image = []

        for row in range(rows):
            y1 = int(row*h) 
            y2 = int((row+1)*h) 

            if row == rows - 1:
                y2 = H

            ascii_image.append("")

            for col in range(cols):

                x1 = int(col*w) 
                x2 = int((col+1)*w)

                if col == cols-1:
                    x2 = W

                img = image.crop((x1, y1, x2, y2)) 

                average = int(self.get_average_L(img))

                if more_levels:
                    gsval = self.gray_scale[int((average*69)/255)]
                else:
                    gsval = self.gray_scale2[int((average*10)/255)]

                ascii_image[row] += gsval

        return ascii_image


def main():
    description = "This script can be used to convert images to ASCII art."
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("--file", dest="file_path", required=False)
    parser.add_argument("--output", dest="output_path", required=False)
    parser.add_argument("--cols", dest="cols", required=False)
    parser.add_argument("--scale", dest="scale", required=False)
    parser.add_argument("--moreLevels", dest="more_levels", action="store_true")

    args = parser.parse_args()

    img_file = args.file_path if args.file_path else str(Path(__file__).parents[1]).replace("\\", "/") + "/img/Bugs.jpg"
    
    output_file = args.output_path if args.output_path else str(Path(__file__).parents[1]) + "/out/output.txt"

    scale = args.scale if args.scale else 0.43

    cols = args.cols if args.cols else 80

    more_levels = args.more_levels

    converter = ImageToAscii()

    ascii_image = converter.convert_image_to_ascii(img_file, cols, scale, more_levels)



    with open(output_file, "w") as file:
        for row in ascii_image:
            file.write(row + "\n")

    print(f"\nASCII image ready in {output_file}")


if __name__ == "__main__":
    main()