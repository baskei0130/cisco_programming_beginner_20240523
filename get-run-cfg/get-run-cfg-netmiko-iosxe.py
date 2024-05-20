from netmiko import ConnectHandler

# ネットワーク機器の接続情報
device = {
    'device_type': 'cisco_xe',  # IOS-XE 用のデバイスタイプ
    'ip': '{change-this}',      # ネットワーク機器の IP アドレス
    'username': '{change-this}',        # ログインユーザー名
    'password': '{change-this}',  # パスワード
    'secret': '{change-this}',    # enable モードのパスワード
}

# ネットワーク機器に接続
net_connect = ConnectHandler(**device)

# enable モードに切り替え
net_connect.enable()

# running-config を取得
output = net_connect.send_command('show running-config')

# 出力表示
print(output)

# 接続終了
net_connect.disconnect()

