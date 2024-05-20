# Cisco Programming Beginner

本レポジトリは、2024年5月23日に実施した「2024年から始めるAPI/プログラマビリティ入門」における
「CiscoSEによるプログラマビリティ / API 実践 Part1」の実施内容です。

## 概要
Cisco Modeling Labs (CML) 上に構築したLabに対し、
ChatGPTに作成してもらったpythonスクリプトでコンフィグの取得、インタフェースをshutdown、検証の自動化を実施しました。
またCMLのバージョンは2.7.0です。2.6までのバージョンだと、今回用意したYAMLファイルは一部うまくインポートできませんのでご注意ください。(Catalyst9000vのNode Definitionが異なるためです。)

## フォルダ説明
以下に本レポジトリ内にあるフォルダを示します。
各フォルダには詳細を説明するReadme、Pythonスクリプト、CMLでLabを構築するためのYAMLファイルがあります。
- get-run-cfg
  - running-configを取得します
- change-if-down
  - あるインタフェースをshutdownします
- vpc-test-pyats
  - vPCの検証を自動化します