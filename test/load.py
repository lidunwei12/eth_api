"""
greeter contract测试
"""
from src.api_eth import Eth
from config import Config
from src.handle_data import match

eth = Eth("http://" + Config.ip + ":" + Config.port)
"""
部署合约
参数(合约abi路径，bin路径，有钱的账户，对应的密码）
不报错的情况下，返回合约地址
"""
"""
调用合约
复制上一步的合约地址，
传入（合约abi路径，合约地址，有钱的账户，对应的密码，随便的字符串）
不报错的情况下，返回交易地址及结果
"""
result = eth.contract_data_upload('../contract/contract_abi.json', '../contract/contract_bin.json',
                                  Config.miner_address, Config.miner_password)
print(result)
if 'tx_hash' in result:
    data = match('../data/20190930124444.png')
    data['id']=1
    id=1
    contract_load_result = eth.use_contract_upload('../contract/contract_abi.json', result['tx_hash'],
                                          Config.miner_address, Config.miner_password, data)
    print(contract_load_result)
    if 'contract_result'in contract_load_result:
        contract_download_result = eth.use_contract_download('../contract/contract_abi.json', result['tx_hash'],
                                                       Config.miner_address, Config.miner_password, id)
        print(contract_download_result)
