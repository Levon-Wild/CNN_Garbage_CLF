from keras.preprocessing.image import load_img, img_to_array
import numpy as np


class Processor:
    """图像预处理"""

    def __init__(self, img_path):
        self.img_path = img_path

    def getImage(self):
        print("=" * 5 + "Getting image..." + "=" * 5)
        image = load_img(self.img_path, target_size=(300, 300))
        image = img_to_array(image, dtype=np.uint8)

        # 统一数据维度: 神经网络为batch_size X 300 x 300 x 3共四维，需要给图像添加一维batch_size信息（该值无意义）
        image = np.expand_dims(image, axis=0)

        return image
