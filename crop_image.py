from PIL import Image

tiles = [
    "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m", "9m",
    "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p",
    "1s", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s",
    "1z", "2z", "3z", "4z", "5z", "6z", "7z",
]

for t in tiles:
    img = Image.open(f"img/{t}.png")
    w, h = img.size
    area = (0, 0, w - 20, h)
    cropped_img = img.crop(area)
    cropped_img.save(f"img/_{t}.png")
