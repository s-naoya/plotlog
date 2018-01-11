plotlog
===
ログファイルからグラフを生成するスクリプト。
単一ファイルの他、簡単に大量の同一フォーマットのログファイルを処理可能。


## 動作要件
- 言語：Python 3.6.3以降
- 必要パッケージ
    - matplotlib（グラフの描画）
        - `pip3 install matplotlib`
    - pandas（ログファイルの読み込み）
        - `pip3 install pandas`
    - PyYAML（設定ファイルの読み込み）
        - `pip3 install pyyaml`

## 使用方法
```
plotlog [-h]
        [--new | --all | --after DATE | --select DATE [DATE ...] |
        --input LOG\_FILE\_PATH [LOG\_FILE\_PATH ...]]
        [--setting SETTING\_FILE\_PATH] [--slice BEGIN END] [--noshift]


引数:
  -h, --help            ヘルプの表示
  --new                 デフォルト: まだ描画されていないログファイルのグラフを出力
  --all                 全てのログファイルについてグラフを出力
  --after DATE          入力した日時以降のログファイルについてグラフを出力
  --select DATE [DATE ...]
                        入力した日時のログファイルについてグラフを出力
  --input LOG\_FILE\_PATH [LOG\_FILE\_PATH ...]
                        入力したパスログファイルについてグラフを出力

  --setting SETTING\_FILE\_PATH
                        使用する設定ファイルの選択 (デフォルト:'user.yml')
  --slice BEGIN END     入力したX軸値に基いて抽出したグラフを出力
  --noshift             ある列が0以上の数値になった地点へグラフ開始地点へのシフトを行わない
```

## 設定ファイル
### 設定項目
[src/default.yml](https://github.com/s-naoya/plotlog/blob/master/src/default.yml)を確認。

### 設定方法
user.ymlを編集することで反映される。
また、新しくyamlファイルを作成し、`--setting`引数で読み込むことでこれが反映される。


## フォーマット要件
- ログファイルの名称は日時を用いて"yymmddhhmmss.csv", "yymmddhhmm.csv", "yyyymmddhhmmss.csv", "yyyymmddhhmm.csv"を推奨.
    - e.g.) 171230235900.csv
- 拡張子、セパレートタイプは設定ファイルで変更可能
- 全ての行で列数が同じ
- 設定ファイルで指定されたディレクトリ内に設置（--input使用時を除く）

## ライセンス
このスクリプトはMITライセンスで配布されている ([link](https://github.com/s-naoya/plotlog/blob/master/LICENSE)）。
