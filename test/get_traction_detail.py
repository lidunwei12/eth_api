"""
测试get_traction_detail
"""
from src.api_eth import Eth
from config import Config

eth = Eth("http://" + Config.ip + ":" + Config.port)
detail = eth.get_traction_detail('0x696a94eaae03680dbade435c0fd49a0f8077097dd4055f683c44b98cc87f0239')
print(detail)
