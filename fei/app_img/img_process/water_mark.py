from PIL import Image, ImageFont, ImageDraw
import os
import time
import random

class CustEmoji(object):
    """表情图片加文字
    
    Arguments:
        folder -- 保存到文件夹
        url_prefix -- 

    Returns:
        [type] -- [description]
    """
    def __init__(self, folder=None, url_prefix=None, src_img=None):
        self._folder = folder
        self._url_prefix = url_prefix
        self._filename = self._gen_filename()
        self._font = "ZiTiQuanXinYiGuanHeiTi2.0-2.ttf"
        self._src_img = src_img

        self.font = os.path.join(self._folder, self._font)
        self.src_img = os.path.join(self._folder, self._src_img)
        self.emoji_file = os.path.join(self._folder, self._filename)
        self.emoji_url = os.path.join(url_prefix, self._filename)

        

    def get_emoji_url(self):
        return self._url_prefix + self.emoji_file

    def _gen_filename(self):
        ts = 'emoji_' + str(int(time.time())) + '_' + str(random.randint(1, 9999))
        filename = ts + '.jpg'
        return filename

    def water_mark_from_left_top(self, text):
        src_img = self.src_img
        font = self.font
        save_to_file = self.emoji_file

        img = Image.open(src_img)
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(font, 45)
        draw.text((0, 500), text, (0,0,0), font=font)
        img.save(save_to_file)

    def water_mark(self, text):
        src_img = self.src_img
        font = self.font
        save_to_file = self.emoji_file

        img = Image.open(src_img)
        weight, height = img.size
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(font, 45)
        draw.text((0, height - 50), text, (0,0,0), font=font)
        img.save(save_to_file)

if __name__ == '__main__':
    save_to_file, url = get_filename(url_prefix='/static/upload/')
    print(water_mark('哼哼哈哈', save_to_file))
