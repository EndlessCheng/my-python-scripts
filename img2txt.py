# -*- coding: utf-8 -*-
from PIL import Image

CHAR_PIX_LIST = ['M', '&', 'D', 'n', '1', '+', ',', ' ']
GAP = 256 / len(CHAR_PIX_LIST)


class Img2txt:
    def __init__(self, src, resize=0.3):
        self.src = src
        img = Image.open(src)
        if img.mode == 'P' or img.mode == 'RGBA':
            im = Image.new('RGB', img.size, 'white')
            im.paste(img.convert('RGBA'), img.convert('RGBA'))
            img = im
        img = img.convert('L')
        self.w = int(img.size[0] * resize)
        self.h = int(img.size[1] / 2.0 * resize)
        img = img.resize((self.w, self.h), Image.ANTIALIAS)
        self.pixes = img.load()

    def img2txt(self):
        with file(self.src + '.txt', 'w') as txt:
            for y in range(self.h):
                def get_char_pix():
                    for x in range(self.w):
                        pix = self.pixes[x, y]
                        for index, c in enumerate(CHAR_PIX_LIST, 1):
                            if pix < index * GAP:
                                yield c
                                break

                line = ''.join(get_char_pix())
                txt.write(line + '\n')



if '__main__' == __name__:
    img2txt = Img2txt('img.jpg')
    img2txt.img2txt()
