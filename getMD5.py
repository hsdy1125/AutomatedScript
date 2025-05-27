import hashlib

def pdf_to_md5(pdf_path):
    with open(pdf_path, 'rb') as f:
        file_data = f.read()
        md5_hash = hashlib.md5(file_data).hexdigest()
    return md5_hash

# 使用示例
pdf_path = '/Users/dengyang/Downloads/Supplementary.pdf'
md5 = pdf_to_md5(pdf_path)
print(f'MD5: {md5}')

# # python getMD5.py

from PIL import Image

# 打开原始图片
image = Image.open("/Users/dengyang/Review/SigraphAsia/img/RepresentativeImage.jpeg")

# 保存为300 DPI的新文件（不改变像素尺寸）
image.save("/Users/dengyang/Review/SigraphAsia/img/RepresentativeImage_300dpi.jpeg", dpi=(300, 300))
