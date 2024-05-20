from genie.testbed import load
from datetime import datetime
import os

# テストベッドファイルをロード
testbed = load('testbed.yaml')

# 結果を保存するディレクトリを作成
result_dir = 'result'
os.makedirs(result_dir, exist_ok=True)

# 現在の日時を取得
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# テスト結果ファイルパス
result_file_path = os.path.join(result_dir, f"test_result_{now}.txt")

# インターフェースの状態を変更する関数
def change_interface_state(device, interface, state):
    device.connect()
    device.configure([f"interface {interface}", f"{'shutdown' if state == 'Down' else 'no shutdown'}"])
    device.disconnect()

# インターフェースステータスを取得する関数
def get_interface_status(device, interfaces):
    device.connect()
    status = f"{device.name} Interface Status:\n"
    for interface in interfaces:
        output = device.parse(f"show interface {interface}")
        status += f"{interface} - {output[interface]['oper_status']}\n"
    device.disconnect()
    return status

# pingテストを実行する関数
def ping_test(device, target):
    device.connect()
    result = device.execute(f'ping {target}')
    device.disconnect()
    return result

# テストとインターフェースステータスを記録する関数
def log_test_result(description, ping_result, interface_status):
    with open(result_file_path, 'a') as file:
        file.write(f"--- {description} ---\n")
        file.write(interface_status)
        file.write(f"Ping Result:\n{ping_result}\n\n")

n9kv_3 = testbed.devices['n9kv-3']
pc = testbed.devices['pc']

# Step 1: pc から 10.0.0.1 に対して ping を実施
ping_result = ping_test(pc, '10.0.0.1')
interface_status = get_interface_status(n9kv_3, ['Ethernet1/64', 'Ethernet1/63'])
log_test_result("Step 1: Ping from PC to 10.0.0.1", ping_result, interface_status)

# Step 2: n9kv-3 の Ethernet1/64 を Down
change_interface_state(n9kv_3, 'Ethernet1/64', 'Down')
ping_result = ping_test(pc, '10.0.0.1')
interface_status = get_interface_status(n9kv_3, ['Ethernet1/64', 'Ethernet1/63'])
log_test_result("Step 2: Ethernet1/64 Down", ping_result, interface_status)

# Step 3: Ethernet1/64 を Up、Ethernet1/63 を Down
change_interface_state(n9kv_3, 'Ethernet1/64', 'Up')
change_interface_state(n9kv_3, 'Ethernet1/63', 'Down')
ping_result = ping_test(pc, '10.0.0.1')
interface_status = get_interface_status(n9kv_3, ['Ethernet1/64', 'Ethernet1/63'])
log_test_result("Step 3: Ethernet1/64 Up, Ethernet1/63 Down", ping_result, interface_status)

# Step 4: Ethernet1/64 と Ethernet1/63 を Down
change_interface_state(n9kv_3, 'Ethernet1/64', 'Down')
change_interface_state(n9kv_3, 'Ethernet1/63', 'Down')
ping_result = ping_test(pc, '10.0.0.1')
interface_status = get_interface_status(n9kv_3, ['Ethernet1/64', 'Ethernet1/63'])
log_test_result("Step 4: Ethernet1/64 Down, Ethernet1/63 Down", ping_result, interface_status)

# Step 5: Ethernet1/64 と Ethernet1/63 を Up
change_interface_state(n9kv_3, 'Ethernet1/64', 'Up')
change_interface_state(n9kv_3, 'Ethernet1/63', 'Up')
ping_result = ping_test(pc, '10.0.0.1')
interface_status = get_interface_status(n9kv_3, ['Ethernet1/64', 'Ethernet1/63'])
log_test_result("Step 5: Ethernet1/64 Up, Ethernet1/63 Up", ping_result, interface_status)

