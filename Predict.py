import ModelLoads
import ImageProcess


class PredictModule:
    def __init__(self, model_path, img_path):
        """初始化预测模块"""
        print("=" * 5 + "Start Predict module" + "=" * 5)

        self.model_path = model_path
        self.img_path = img_path

    def PredictCore(self):
        """加载模型和预处理图像"""
        model = ModelLoads.ModelLoadsModule(self.model_path)
        model = model.Generate_Model()

        image = ImageProcess.ImageProcessModule(self.img_path)
        image = image.ProcessImage()

        """进行预测"""
        return model.predict(image)

    def ResultHandler(self, key):
        """处理预测结果：one-hot编码解析"""
        one_hot = {0: "cardboard", 1: "glass", 2: "metal", 3: "paper", 4: "plastic", 5: "trash"}

        for i in range(0, 6):
            if key[0][i] == 1:
                res = i
        return one_hot[res]
