import base64
import warnings

from config_path.path_file import read_file
from PIL import Image, ImageEnhance
from pytesseract import pytesseract


class VerificationCode(object):
    """该类主要用于验证码识别，类型为base64格式！并且是为字母和数字类型的验证码"""
    def __init__(self, base64_data):
        pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' # tesseract安装位置，必须指定
        self.base64_data = base64_data
        self.verification_code_path = read_file('img', 'ver_code.png')

    def _handle_base_data(self):
        """提取base64数据,并写入验证码图片"""
        content = self.base64_data.split(',')[1]
        conversion = base64.b64decode(content)
        with open(self.verification_code_path, 'wb') as w:
            w.write(conversion)

    def distinguish_code(self):
        """识别验证码图片"""
        self._handle_base_data()
        self._img_handle_gray()
        return self._img_handle_dis()

    def _img_handle_gray(self):
        """图像处理——置灰"""
        warnings.filterwarnings('ignore')
        image = Image.open(self.verification_code_path).convert('L')  # convert图片颜色变化灰色（L）
        sharpness = ImageEnhance.Contrast(image).enhance(1)  # 对比度增强
        threshold = 140
        table = []
        for color in range(256):
            if color < threshold:
                table.append(0)
            else:
                table.append(1)
        image = sharpness.point(table, '1')  # 去燥
        image.save(self.verification_code_path)

    def _img_handle_dis(self):
        """图像处理——识别验证"""
        image = Image.open(self.verification_code_path).convert('L')
        image.crop((16, 5, 69, 27)).save(self.verification_code_path)
        image = Image.open(self.verification_code_path).convert('L')
        return pytesseract.image_to_string(image, lang='eng')


class ImageSetHandle(object):
    """该类主要用于PIL各种图像处理方法"""
    def __init__(self, image_path):
        self.path = image_path

    def img_rotate(self, rotate_degrees, image_mode=''):
        # 图像旋转
        # rotate_degrees：旋转度数;
        # image_mode: 为空，立即展示效果，为路径即为保存处理后路径
        image = Image.open(self.path)
        mode = image.rotate(rotate_degrees)
        if not image_mode:
            mode.show()
        else:
            mode.save(image_mode)

    def img_thumbnail(self, thumbnail_size, save_path):
        # 图像变更为缩略图
        # thumbnail_size: 缩小范围为元组类型, 如（300, 300）&& [300, 300]
        # save_path: 保存路径
        image = Image.open(self.path)
        image.thumbnail(thumbnail_size)
        image.save(save_path)

    def img_size(self):
        # 获取图片尺寸（左、上、右、下）
        image = Image.open(self.path)
        print(image.getim())
        return image.getbbox()

if __name__ == '__main__':
    change = r'D:\work_file\auto_script\UI\img\tes2.jpg'

    i = ImageSetHandle(r'D:\work_file\auto_script\UI\img\test.jpg')
    i.img_size()