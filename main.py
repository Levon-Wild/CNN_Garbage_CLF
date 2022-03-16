import Predict


class Predictor:
    """Predictor测试类"""
    def __init__(self, model_path, img_path):
        print("="*5 + "demo Starting..." + "="*5)
        self.model_path = model_path
        self.img_path = img_path

    def PredictFun(self):
        """demo预测模块"""

        """获取模型和预处理后的图像数据"""
        prediction = Predict.PredictModule(self.model_path, self.img_path)
        """将数据传入core进行预测"""
        predict_result = prediction.PredictCore()
        """处理one-hot编码并返回"""
        return prediction.ResultHandler(key=predict_result)


if __name__ == '__main__':
    """客制化模型与图片参数"""
    custom_model_path = r"/Users/truman/Desktop/temp/model.h5"
    custom_img_path = r"/Users/truman/Desktop/temp/IMG_6304.jpg"

    """创建预测器"""
    predictor = Predictor(custom_model_path, custom_img_path)

    """进行预测"""
    print(predictor.PredictFun())

