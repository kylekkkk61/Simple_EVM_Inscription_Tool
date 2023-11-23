#### 本腳本為自轉腳本，僅適用於EVM，不包括BSC
#### Uploaded By kylekkkk.eth
#### 追蹤推特 @kylekkkkwu61

##--------------------------------##

from web3 import Web3, Account
import time


# rpc地址
rpc = "替換為欲使用RPC"  # https://chainlist.org/ 可找尋
# 銘文接收地址
to_address = "銘文接收地址"
# 你自己的私鑰
private_key = "你的私鑰"
nums = 100  # 打多少張
data = 'data:,{"p":"frc-20","op":"mint","tick":"fans","amt":"10000"}'  # 換為要打的銘文

# 連接到rpc節點
w3 = Web3(Web3.HTTPProvider(rpc))
from_address = Account.from_key(private_key).address
# 判断網路是否連接
if w3.is_connected() == True:
    print("網路連接成功 開始發送交易")
    # 當前noce
    nonce = w3.eth.get_transaction_count(from_address)
    # 當前gas價格
    gas_price = w3.eth.gas_price
    print("當前nonce:", nonce, "發送地址:", from_address)
    # 發送交易
    for i in range(nums):
        transaction = {
            "from": from_address,  # from：發送地址
            "to": to_address,  # to：接收地址
            "value": w3.to_wei(0, "ether"),  # value：發送的eth數量
            "nonce": nonce,  # nonce
            "gas": 25000,  # gas大小
            "gasPrice": gas_price,  # gasPrice 以Wei为單位
            "data": w3.to_hex(text=data),  # 銘文內容
            "chainId": w3.eth.chain_id,  # 發送至哪個鏈
        }
        # 簽名交易
        signed = w3.eth.account.sign_transaction(transaction, private_key)
        try:
            # 3.推送到區塊鏈
            tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
            print("Hash:", tx_hash.hex(), "nonce:", nonce)
        except Exception as e:
            print("Error: ", e)
        nonce += 1
        time.sleep(1)  # 每次交易休息時間，會出錯請延長
elif w3.is_connected() == False:
    print("網路連接失敗 請重新開啟腳本/更換rpc節點")
