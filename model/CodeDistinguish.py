import base64

from config_path.path_file import read_file
from PIL import Image, ImageEnhance
from pytesseract import pytesseract


class VerificationCode(object):
    """该类主要用于验证码识别，类型为base64格式！并且是为英文类型的验证码"""
    def __init__(self, base64_data):
        pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe' # tesseract安装位置，必须指定
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
        image = Image.open(self.verification_code_path).convert('L')  # convert图片颜色变化灰色（L）
        threshold = 140
        table = []
        for color in range(256):
            if color < threshold:
                table.append(0)
            else:
                table.append(1)
        image = image.point(table, '1')  # 去燥
        image.save(self.verification_code_path)

    def _img_handle_dis(self):
        """图像处理——识别验证"""
        image = Image.open(self.verification_code_path).convert('RGB')
        sharpness = ImageEnhance.Contrast(image).enhance(1)  # 对比度增强
        sharpness.save(self.verification_code_path)
        return pytesseract.image_to_string(image)


if __name__ == '__main__':
    a = 'data:image/JPEG;base64,R0lGODlhVQAkAPAAAAGUjv///ywAAAAAVQAkAEAIxgADCBxIsKDBgwgTKlzIsKHDhxAjSpQIoGJFggACXByYUaBFjR0zbvQIsmDHiShTlnR4UqXLlzBjypxJs6bNmx5Dmtw4kufOkxdb4hxKtKjRo0iTKl2qEeFIjgufkmTqVGfOqT2trgwJNKnFlkKnghSpFSPGsFTTql3Ltq3bt3Djyp1Lt65dol8/NjWI1izftX31QlUoWCzbnlexcrWKeOXepT45iky89ezjoF4lD7a8NTJnync/M5Qa2nHUvqVTq17NuvXdgAA7'
    test = VerificationCode(a)
    print(test.distinguish_code())