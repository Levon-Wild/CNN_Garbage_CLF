# 利用卷积神经网络进行垃圾分类

## 技术架构
环境：Keras（Tensorflow2.8） + Flask + Java(Oracle JDK8)

平台：Jetson Nano

## 模块说明

### PyBoot
启动Flask以暴露接口

### Data

- Model: 模型仓库 
  - new_model.h5(2022.03.18) 
- TestSet: 随代码测试集


### Service
- Image: 处理输入图像-将其转换为适合投喂神经网络的 1 x 300 X 300 的三维信息
- Model: 加载模型

### Utils
工具类

 - ResultHandler：结果（独热编码）解析器
 - JsonData: 统一接口返回协议

# 更新说明

## 2022.03.25

更新技术栈：
- 引入Flask，API式服务（公共token="I9Lo1VEaI1")
    1. 减少时间开销：旧版本每测试一张图片需要重新加载一次模型，模型加载的时间开销是预测开销的10倍左右。新版本采用API暴露服务，仅在第一次访问接口时加载一次模型。
    2. 接口安全：拒绝无token请求（目前仅有公共token）
    3. 统一接口返回协议：增强跨平台跨语言支持

修复Bugs
  - 空文件预测时抛出FileNotFoundError
  

Tip：由于数据集采用白色背景，经过测试，当输入图片背景为白色时（如A4打印纸）能提高预测准确率。