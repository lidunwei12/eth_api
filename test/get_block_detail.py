"""
测试get_block_detail
"""
from src.api_eth import Eth
from config import Config
eth = Eth("http://" + Config.ip + ":" + Config.port + "8545")
result = eth.get_block_detail('0x4de5a0140a584bd7f6c000b1d16d7457e9c117869c7bea02ffa7b5a80e39cef0')
print(result)
