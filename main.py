import Model
import Image
import sys
import Utils
import time

if __name__ == '__main__':
    """模型加载"""
    model_loader = Model.Loader()
    model = model_loader.getModel()

    path = sys.argv[1]
    print("=" * 5 + ">" * 3 + path)

    start = time.time()
    """预处理图像"""
    img_processor = Image.Processor(path)
    img = img_processor.getImage()

    """进行预测"""
    print(Utils.ResultHandler(model.predict(img)))
    end = time.time()
    print("Time used: {}".format(end - start))

