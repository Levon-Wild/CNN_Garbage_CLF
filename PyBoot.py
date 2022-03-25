import json
from flask import Flask
from flask import request

from service import Model, Image
from utils import ResultHandler
from utils import JsonData

app = Flask(__name__)


@app.route('/predictApi', methods=['POST'])
def predict():

    """解析json"""
    data_map = json.loads(request.get_data())

    """验证访问合法性"""
    if not data_map["token"] == "I9Lo1VEaI1":
        return json.dumps(JsonData.buildError(-1, "Request Denied: Unauthenticated Access!"))
    """模型加载"""
    model_loader = Model.Loader()
    model = model_loader.getModel()

    try:
        """预处理图像"""
        img_processor = Image.Processor(data_map["image_path"])
        img = img_processor.getImage()

        """进行预测"""
        result = ResultHandler.OneHotKeyProcessor(model.predict(img))

        return json.dumps(JsonData.buildSuccess("Prediction Success", {"result": result}))
    except FileNotFoundError:
        return json.dumps(JsonData.buildError(-2, "Internal Service Error: Could NOT find the image!"))


if __name__ == '__main__':
    app.run(debug=False)
