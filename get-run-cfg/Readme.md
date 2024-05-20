# get-run-cfg

get-run-cfg は Cisco Modeling Labs (CML) 上の
仮想機器 Catalyst9000v の running-config を取得するスクリプトです。
netmikoライブラリ、telnetlibライブラリの2つを使い実行するファイルを作成していますが、2つとも動作内容は同じです。
またCMLのバージョンは2.7.0です。2.6までのバージョンだと、今回用意したYAMLファイルは一部うまくインポートできませんのでご注意ください。(Catalyst9000vのNode Definitionが異なるためです。)

## フォルダ構成
- Readme.md
  - フォルダの概要や実施方法を示したものです
- get-run-cfg-netmiko-iosxe.py
  - CML上のIOS-XEで動作する機器のrunning-configをnetmikoライブラリを使い取得するスクリプトです
  - ChatGPT作です
- get-run-cfg-telnet-iosxe.py
  - CML上のIOS-XEで動作する機器のrunning-configをtelnetlibライブラリを使い取得するスクリプトです
  - ChatGPT作です
- Get_running-config_by_Programmability(IOS-XE).yaml
  - 本検証で使用したラボ環境のYAMLファイルです。CMLにインポートすることで初期構築の時間を短縮できます。
  - IPアドレスや認証周りの情報はご自分で入力してください。

## 実行順序
1. CMLでLabを準備
   1. CMLにおいてProgrammability(IOS-XE).yaml をインポートし、初期設定 (IP address/default gw/username/password/enable password/line 0 4; login local) を入力
   2. Catalyst9000vを使う場合は、Login password は ```username {username} secret {password}``` で入力してください。
2. ChatGPT にPythonスクリプト作成を依頼
   1. 本作者の環境でChatGPTに作成してもらったPythonファイルは ```get-run-cfg-netmiko-iosxe.py``` で保存
   2. このファイル下部に本作者がChatGPTに依頼したプロンプトを記載しています。
3. ChatGPTに作成してもらったPythonファイルを実行するために必要なパッケージをインストール
   1. 本作者の場合：Python3, pip3, netmiko をインストール
   2. これらのインストール方法はせっかくなのでChatGPTに聞いたりネットで調べてみましょう
   3. Pythonを使う場合は仮想環境を使うとパッケージの管理が容易になります ([参考](https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde))
4. ChatGPTに作成してもらったPythonファイルを実行 (```python3 get-run-cfg-netmiko-iosxe.py```)
   1. ```get-run-cfg-netmiko-iosxe.py```を使う場合は、{change-this} と書かれた部分を皆様の環境に応じて変更してください。

## ChatGPT プロンプト
```
あなたはCisco Modeling Labs(CML)、ネットワーク機器、プログラミングのスペシャリストです。ネットワーク機器A (IOS-XE {change-this}, IP: {change-this}, username: {change-this}, password: {change-this}, enable password: {change-this}) の running-config を取得するスクリプトをPythonで作成してください。
```

:::note warn
{change-this}の部分を環境に合わせて変更してください。
:::