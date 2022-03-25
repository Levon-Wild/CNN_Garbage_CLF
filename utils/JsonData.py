# 统一接口返回协议JsonData遵循阿里巴巴后端开发规范

"""
Success默认状态码0
Error默认状态码自定义
"""


def buildSuccess(msg, obj):
    jsonDict = {"code": 0, "msg": msg, "data": obj}
    return jsonDict


def buildError(code, msg):
    jsonDict = {"code": code, "msg": msg}
    return jsonDict
