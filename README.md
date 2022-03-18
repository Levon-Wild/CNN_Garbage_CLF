# 利用卷积神经网络进行垃圾分类

## 技术架构
环境：Keras（Tensorflow2.8） + Python（3.9） + Java（Oracle JDK8）

平台：Jetson Nano

## 模块说明

### main：程序入口
传入程序运行参数
运行：

    python main.py "Img_URL"

### Model
加载模型（.h5 Sequential ONLY）

### Image
处理输入图像：将其转换为适合投喂神经网络的 300 X 300 X * 的三维信息

### Utils
工具类

 - ResultHandler：结果独热编码解析器

# 更新说明

## 2022.03.18

重构代码：

- 简化处理逻辑：减少不必要流程代码拆分
- 重组模块分类
- 提高执行效率：图像加载预测时间减少83%（压缩至0.5秒/张）

新一代模型：
 - 减少过拟合
 - 提升测试集准确率15%（至75%）
 - 支持load_model直接读取：显著减少模型加载耗时