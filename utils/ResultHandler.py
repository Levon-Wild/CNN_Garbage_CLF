

def OneHotKeyProcessor(key):
    """处理预测结果：one-hot编码解析"""
    one_hot = {0: "cardboard", 1: "glass", 2: "metal", 3: "paper", 4: "plastic", 5: "trash"}

    for i in range(0, 6):
        if key[0][i] == 1:
            res = i
            return one_hot[res]
    return "unknown"

