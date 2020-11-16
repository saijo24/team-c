from Weight_calc import basicClass as bc
from Weight_calc import manageData as md

# ここのプログラムは全てテスト用(サンプル)

# gotData テスト用
gotData = {
    'basic_classification': ['Coming_out', 'Request'],
    'status': 'Disagree',
    'sub_classification': 'Wolf',
    'target': None
}

# users テスト用
users = ("AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG")

if __name__ == "__main__":
    # 役職テーブルの初期化
    md.initDatas(users)

    # 分類結果辞書とユーザ名(or ID)を引数とする
    # この関数を実行すれば重さ計算を終えて
    # テーブルの更新も終了する
    bc.assem(gotData, "AAA")
    md.exiCo()

    # 役職テーブルにあるデータを全て削除
    md.fineDatas(users)
