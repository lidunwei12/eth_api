from src.api_eth import Eth

eth = Eth("http://localhost:8545")
# ans = eth.contract_data_upload('../contract/contract_abi.json', '../contract/contract_bin.json',
#                                "0x4724fa64a0f5ee6da410df4db6729f2b855fa6c9", '123456')
# temp = eth.get_block_detail('0x4de5a0140a584bd7f6c000b1d16d7457e9c117869c7bea02ffa7b5a80e39cef0')