import numpy as np
from PIL import Image
import random
import os

def get_script_directory():
    """获取脚本所在的目录"""
    return os.path.dirname(os.path.abspath(__file__))

def encrypt_image(image_filename, output_filename='encrypted_image.png', key_filename='encryption_keys.npy'):
    script_dir = get_script_directory()
    
    # 读取原始图像
    image_path = os.path.join(script_dir, image_filename)
    img = Image.open(image_path)
    RGB = np.array(img)
    s = RGB.shape
    n = s[0] * s[1] * s[2]

    # 第一步: 像素点随机打乱
    r = list(range(n))
    random.shuffle(r)  # 随机序列
    RGBS = RGB.reshape(-1)  # 将图像转换为一维数组
    RGBSS = RGBS[r].reshape(s)  # 应用随机序列打乱像素

    # 第二步: 图像三维数据重置
    Gadd = np.random.randint(0, 256, size=s, dtype=np.uint8)  # 生成随机矩阵
    G1 = np.zeros_like(RGBSS, dtype=np.float32)

    # 加密操作
    G1 = 0.1 * RGBSS + 0.9 * Gadd
    G1 = G1.astype(np.uint8)

    # 保存加密图像和密钥（随机序列和随机矩阵）
    encrypted_image_path = os.path.join(script_dir, output_filename)
    key_file_path = os.path.join(script_dir, key_filename)
    Image.fromarray(G1).save(encrypted_image_path)
    np.save(key_file_path, {'r': r, 'Gadd': Gadd})

def decrypt_image(input_filename='encrypted_image.png', key_filename='encryption_keys.npy', output_filename='decrypted_image.png'):
    script_dir = get_script_directory()
    
    # 读取加密图像和加载密钥
    input_path = os.path.join(script_dir, input_filename)
    key_file_path = os.path.join(script_dir, key_filename)
    G1 = np.array(Image.open(input_path))
    keys = np.load(key_file_path, allow_pickle=True).item()
    r = keys['r']
    Gadd = keys['Gadd']

    # 解密操作
    G2 = (G1 - 0.9 * Gadd) / 0.1
    G2 = G2.clip(0, 255).astype(np.uint8)

    # 使用还原索引解密图像
    f = np.zeros_like(r)
    for t in range(len(r)):
        f[r[t]] = t
    RGBE = G2.reshape(-1)
    RGBEE = RGBE[f].reshape(G1.shape)

    # 保存解密后的图像
    decrypted_image_path = os.path.join(script_dir, output_filename)
    Image.fromarray(RGBEE).save(decrypted_image_path)

# 测试函数，假设你将图片命名为 "original_image.png" 并放在与脚本相同的文件夹中
encrypt_image('original_image.png')
decrypt_image()

# 注意：这里没有显示图像的功能，如果需要显示可以用matplotlib.pyplot.imshow() 或者直接打开文件查看。
