"""
文件预处理及合约预处理
"""
import hashlib  # 导入hashlib模块
import os
import time

"""
获取unix时间戳调用unix_time()
"""
unix_time = lambda: int(round(time.time() * 1000))


def match(file_path, Bytes=1024):
    """
    提取文件的名字及文件进行哈希
    :param file_path: 文件路径
    :param Bytes:只读取固定字节
    :return:名字和文件哈希
    """
    (file_path, filename) = os.path.split(file_path)
    md5_1 = hashlib.md5()  # 创建一个md5算法对象
    with open(file_path, 'rb') as f:  # 打开一个文件，必须是'rb'模式打开
        while 1:
            data = f.read(Bytes)  # 由于是一个文件，每次只读取固定字节
            if data:  # 当读取内容不为空时对读取内容进行update
                md5_1.update(data)
            else:  # 当整个文件读完之后停止update
                break
    file_hash = md5_1.hexdigest()  # 获取这个文件的MD5值
    return {'name': filename, 'file_hash': file_hash}


def contract_windows_solc(contract_file):
    """
    如果windows装了solc.exe，可以编译智能合约，生成abi和bytecode，传入全路径文件
    :param contract_file: 全路径文件
    :return: contract文件编译后的abi和bytrcode
    """
    data = os.popen('solc.exe --combined-json abi,bin,interface,metadata '+contract_file)
    print(data.read())
# print(match('../data/20190930124444.png'))
