from keras.models import load_model


class Loader:
    def __init__(self):
        """模型加载模块"""
        print("=" * 5 + "Loading model..." + "=" * 5)
        self.model = load_model('new_model.h5')
        self.model.summary()

    def getModel(self):
        return self.model
