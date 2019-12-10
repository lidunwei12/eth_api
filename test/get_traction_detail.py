"""
测试get_traction_detail
"""
from src.api_eth import Eth
from config import Config

eth = Eth("http://" + Config.ip + ":" + Config.port)
detail = eth.get_traction_detail('0xeb445a55c200f3c722cd908cd87f0b224e52d1f08cfadd1a78f0ccfda403c103')
print(detail)
