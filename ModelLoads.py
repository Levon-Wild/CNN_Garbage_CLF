from keras.layers import Conv2D, Flatten, MaxPooling2D, Dense
from keras.models import Sequential


class ModelLoadsModule:
    """加载模型"""

    def __init__(self, model_path):
        self.model_path = model_path
        # pass

    def Generate_Model(self):
        """创建顺序模型"""
        new_model = Sequential([
            Conv2D(filters=32, kernel_size=3, padding='same', activation='relu',
                   input_shape=(300, 300, 3)),

            MaxPooling2D(pool_size=2),  # 池化核的尺寸

            Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'),
            MaxPooling2D(pool_size=2),

            Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'),
            MaxPooling2D(pool_size=2),

            Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'),
            MaxPooling2D(pool_size=2),

            Flatten(),  # 扁平层

            Dense(64, activation='relu'),  # 全连接层
            Dense(6, activation='softmax')
        ])

        """指定模型超参数"""
        new_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

        """从h5文件读取模型（权重）"""
        # print(type(self))
        new_model.load_weights(self.model_path, by_name=False)

        return new_model
