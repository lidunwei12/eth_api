"""
greeter contract测试
"""
from src.api_eth import Eth
from config import Config

eth = Eth("http://" + Config.ip + ":" + Config.port + "8545")
"""
部署合约
参数(合约abi路径，bin路径，有钱的账户，对应的密码）
不报错的情况下，返回合约地址
"""
result = eth.contract_data_upload('../contract/multiply_abi.json', '../contract/multiply_bin.json',
                                  "0x4724fa64a0f5ee6da410df4db6729f2b855fa6c9", '123456')
print(result)
"""
调用合约
复制上一步的合约地址，
传入（合约abi路径，合约地址，有钱的账户，对应的密码，随便的字符串）
不报错的情况下，返回交易地址及结果
"""
# result = eth.use_contract_example('../contract/multiply_abi.json', '0x9cf602ea3551bA61EFa05489cdC44bB5a51772df',
#                                   "0x4724fa64a0f5ee6da410df4db6729f2b855fa6c9", '123456', '1234')
# print(result)
