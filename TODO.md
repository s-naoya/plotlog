TODO
===
## 設計
### Settingクラス
設定ファイルの読み出し、保存

### DataCutクラス
プロットに使うDataFrameを作成（=shift、sliceの実行）

### PlotGraphクラス
設定、DataFrameに従ってグラフをプロット。

### plotlog.py
コマンドライン引数の解析、各クラスの順次実行



## 要求仕様
- 設定ファイル
    - ファイル自体
        - YAMLファイルから設定を読み出す
        - 編集不可のdefault.ymlと編集用のsetting.ymlに分ける
        - setting.ymlは引数から変更可能にする
    - 設定可能項目
        - プロット関連
            - グラフファイル名
            - グラフサイズ
            - グラフ拡張子
            - 軸ラベル
            - 軸リミッター
            - プロット列名（ヘッダー名 or 列数）
            - 線色（default: ランダム）
            - 線種（default: 線4種順番）
            - 凡例（default: ヘッダー名）
            - 凡例位置（default: best）
        - フットプリント
            - 支持脚
                - 右足、左足、両足
                - デフォルトはそれぞれ0, 1, 2
            - 両足先端位置（世界座標）
            - 足サイズ
        - その他
            - ログファイルの区切り方
            - ログファイル設置場所
            - グラフ保存場所

- 読み込み可能ログデータ
    - カンマ区切り(csv)(default) or スペース区切り(dat) or タブ区切り(tsv)
    - header対応
        - header行をyamlで指定（1行目とかにメモ書けるように）
    - 単一ファイルのみ
    - ファイル名はyyyymmddhhmm.ext (default) or yymmddhhmm.ext

- グラフプロット
    - 基本的に散布図のみ
        - 他は必要そうだと思ったら対応
    - subplot対応したい。。。

- フットプリントの計算

- コマンドライン引数
    - 読み込みログファイル
        - all
        - select
        - after
        - new（default）
    - 設定ファイル
        - setting（default: setting.yml）
    - その他
        - shift
            - デフォルトはTrue(shiftする)
        - slice



### 展望
- データの前処理を行いやすくするスクリプトの作成
    - オリジナルをyymmddhhmm_orig.extとして保存する
    