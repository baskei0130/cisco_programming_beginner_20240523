import requests
import json

# CML Server 情報
CML_URL = "https://{change-this}"
USERNAME = "{change-this}"
PASSWORD = "{change-this}"

payload = {
    "username": "{change-this}",
    "password": "{change-this}"
}

# API Header
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

# Token を取得するための関数
def get_bearer_token():
    url = f"{CML_URL}/api/v0/authenticate"
    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Token の取得に失敗しました。")

# Lab のリストを取得するための関数
def get_labs(token):
    url = f"{CML_URL}/api/v0/labs"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, data=json.dumps(payload), verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception("Lab リストの取得に失敗しました。")

# Lab の詳細情報を取得するための関数
def get_lab_details(token, lab_id):
    url = f"{CML_URL}/api/v0/labs/{lab_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, data=json.dumps(payload), verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        raise Exception(f"Lab ID {lab_id} の詳細情報の取得に失敗しました。")

# pyATS Testbed情報を取得するための関数
def get_pyats_testbed(token, lab_id):
  url = f"{CML_URL}/api/v0/labs/{lab_id}/pyats_testbed"
  headers = {
    "accept": "application/x-yaml",
    "Authorization": f"Bearer {token}"
  }
  response = requests.get(url, headers=headers, data=json.dumps(payload), verify=False)
  if response.status_code == 200:
    return response.text
  else:
    raise Exception(f"Lab ID {lab_id} のpyAts Testbed情報の取得に失敗しました。")

# 主要な処理を実行する
def main():
    token = get_bearer_token()
    lab_ids = get_labs(token)
    for lab_id in lab_ids:
        lab_details = get_lab_details(token, lab_id)
        if lab_details['lab_title'] == "Programmability(vPC)":
            # pyATS Testbed情報を取得
            pyats_testbed = get_pyats_testbed(token, lab_id)
            # pyATS Testbed情報をファイルに書き込む
            with open("testbed.yaml", "w") as file:
              file.write(pyats_testbed)
              print("Testbed information has been saved to testbed.yaml")
            break

# 実行
if __name__ == "__main__":
    main()
