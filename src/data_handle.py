import hashlib
import time
current_milli_time = lambda: int(round(time.time() * 1000))

def hash(data_one, data_two):
    sha = hashlib.sha1()
    sha.update("{0}{1}".format(data_one, data_two).encode("utf8"))
    return sha.hexdigest()
print(hash('我是你爹','叫爸爸'))
print(current_milli_time())
import os
data =os.popen('solc.exe --combined-json abi,bin,interface,metadata contract/test.sol')
print(data.read())