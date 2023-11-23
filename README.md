# Simple_EVM_Inscription_Tool
本腳本用於自轉打銘文用途，僅限EVM使用，目前BSC鏈暫不支援，任何問題可至推特詢問

推特 https://twitter.com/kylekkkkwu61


### 以下為腳本中需修改處：

rpc -> 該鏈RPC  （ 可至   https://chainlist.org/    尋找速度快的使用 ）

to_address -> 銘文接收地址 （填寫該私鑰的地址）

private_key -> 你的私鑰

nums -> 要打多少張

data = 'data:,{"p":"asc-20","op":"mint","tick":"aval","amt":"100000000"}'  # 換為要打的銘文內容



### 間隔時間

腳本最下方的 time.sleep(1) 處，代表每張交易間隔一秒發送，發現交易速度太快會報錯可以適量調高
