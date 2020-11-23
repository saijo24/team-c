from Weight_calc import basicClass as bc
from Weight_calc import manageData as md


def initDatabaseTable(users: list):
    """
    データベースのテーブルを作成する。

    Parameters
    ---------
    users: list of str
        ゲームに参加するユーザのリスト

    Notes
    ---------
    絶対に書いてくれ。
    """
    md.initDatas(users)
    return


def fineDatabaseTable(users: list):
    """
    テーブルに格納されているデータを削除します。

    Parameters
    ---------
    users: list of str
        ゲームに参加しているユーザのリスト    
    """
    md.fineDatas(users)
    return


def outputDatabase(path: str):
    """
    指定された場所にデータベースの内容を出力する(したい)。

    Parameters
    ----------
    path : str
        出力したい場所

    Notes
    ---------
    できてない。
    """
    print(path)
    return


# テスト用
gotData = {
    'basic_classification': ['Coming_out', 'Request'],
    'status': 'Disagree',
    'sub_classification': 'Wolf',
    'target': None
}

users = ("AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG")
roles = ("wolf", "citizen", "diviner", "medium",
         "madman", "hunter", "co_owner", "hamster",)

if __name__ == "__main__":
    # 役職テーブルの初期化
    # md.initDatas(users)
    initDatabaseTable(users)

    print(md.selectAll(roles[0]))
    # 分類結果辞書とユーザ名(or ID)を引数とする
    # この関数を実行すれば重さ計算を終えて
    # テーブルの更新も終了する
    bc.assem(gotData, "AAA")
    # md.exiCo()

    # 役職テーブルにあるデータを全て削除
    # md.fineDatas(users)
    fineDatabaseTable(users)
