# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract


def main():
    image = Image.open("1.png")
    print pytesseract.image_to_string(image, lang='chi_sim').decode('utf-8')


if __name__ == "__main__":
    main()
