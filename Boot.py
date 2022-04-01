from keras.models import load_model

import numpy as np
import cv2


def OneHotKeyProcessor(key):
    """处理预测结果：one-hot编码解析"""
    one_hot = {0: "cardboard", 1: "glass", 2: "metal", 3: "paper", 4: "plastic", 5: "trash"}

    for i in range(0, 6):
        if key[0][i] == 1:
            return one_hot[i]
    return "unknown"


if __name__ == '__main__':

    # 模型加载
    model = load_model('Data/Model/new_model.h5')

    # 打开摄像头
    capture = cv2.VideoCapture(0)

    while True:
        # 获取一帧
        ret, frame = capture.read()
        # 预处理图像
        inputImg = cv2.resize(frame, (300, 300), interpolation=cv2.INTER_CUBIC)
        image = np.expand_dims(inputImg, axis=0)
        # 输出结果
        result = OneHotKeyProcessor(model.predict(image))
        print(result)
        # 显示视频
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) == ord('q'):
            capture.release()  # 释放摄像头
            cv2.destroyAllWindows()  # 删除建立的全部窗口
            break
