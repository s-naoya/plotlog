plotlog
=======

ログファイルからグラフを生成するスクリプト。
単一ファイルの他、簡単に大量の同一フォーマットのログファイルを処理可能。

動作要件
--------

-  言語：Python 3.6.3以降
-  必要パッケージ

   -  matplotlib（グラフの描画）
   -  pandas（ログファイルの読み込み）
   -  PyYAML（設定ファイルの読み込み）

インストール
------------

.. code:: sh

    pip3 install plotlog

使用方法
--------

::

    plotlog [-h] [--setting SETTING_FILE_PATH] [--copy]
            [--new | --all | --after DATE | --select DATE [DATE ...] |
            --input LOG_FILE_PATH [LOG_FILE_PATH ...]] [--slice BEGIN END]
            [--noshift]


    引数:
      -h, --help            ヘルプの表示
      --setting SETTING_FILE_PATH
                            使用する設定ファイルの選択 (デフォルト:'user.yml')
      --copy                設定ファイルをコピー
      --new                 デフォルト: まだ描画されていないログファイルのグラフを出力
      --all                 全てのログファイルについてグラフを出力
      --after DATE          入力した日時以降のログファイルについてグラフを出力
      --select DATE [DATE ...]
                            入力した日時のログファイルについてグラフを出力
      --input LOG_FILE_PATH [LOG_FILE_PATH ...]
                            入力したパスログファイルについてグラフを出力

      --setting SETTING_FILE_PATH
                            使用する設定ファイルの選択 (デフォルト:'user.yml')
      --slice BEGIN END     入力したX軸値に基いて抽出したグラフを出力
      --noshift             ある列が0以上の数値になった地点へグラフ開始地点へのシフトを行わない

まず設定ファイルを作成する。

::

    plotlog --copy

作成されたuser.ymlを編集して、各パスや作成したいグラフ等を指定する。
変更する必要のない設定項目は削除してもよい。

設定し終えたらグラフを作成する。

::

    plotlog

user.ymlが正しく設定されていれば、
まだ出力されていないログファイルについてグラフが描画される。

設定方法
--------

user.ymlを編集することで反映される。
また、新しくyamlファイルを作成し、\ ``--setting``\ 引数で読み込むことでこれが反映される。

フォーマット要件
----------------

-  ログファイルの名称は日時を用いて“yymmddhhmmss.csv”, “yymmddhhmm.csv”,
   “yyyymmddhhmmss.csv”, “yyyymmddhhmm.csv”を推奨.

   -  e.g.) 171230235900.csv

-  拡張子、セパレートタイプは設定ファイルで変更可能
-  全ての行で列数が同じ
-  設定ファイルで指定されたディレクトリ内に設置（–input使用時を除く）

ライセンス
----------

このスクリプトはMITライセンスで配布されている
(`link <https://github.com/s-naoya/plotlog/blob/master/LICENSE>`__\ ）。
