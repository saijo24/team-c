from Weight_calc import basicClass as bc
from Weight_calc import manageData as md
import json
import datetime

# 以下関数群


def InitDatabaseTable(users: list):
    """
    データベースのテーブルを作成する。

    Parameters
    ---------
    users: list of str
        ゲームに参加するユーザのリスト

    Notes
    -----
    絶対に書くこと。

    Examples
    --------
    >>> users = ("Fuge", "Hoge", "Tom", "Jon")
    >>> InitDatabaseTable(users)
    """
    md.initDatas(users)
    return


def FineDatabaseTable(users: list, table_delete=False):
    """
    テーブルに格納されているデータを削除します。

    Parameters
    ---------
    users: list of str
        ゲームに参加しているユーザのリスト    
    """
    md.fineDatas(users, table_delete)
    return


def WeightCalc(data: dict, user: str):
    """
    分類結果と発言者から重みを計算する。

    Parameters
    ----------
    data : dict
        分類結果
    user : str
        発言者のユーザ名

    Examples
    --------
    >>> users = ("Fuge", "Hoge", "Tom", "Jon")
    >>> data = {
            'basic_classification': ['Coming_out', 'Request'],
            'status': 'Disagree',
            'sub_classification': 'Wolf',
            'target': None
        }
    >>> WeightCalc(data, users[2])
    """
    bc.assem(data, user)


def SelectRoleTable(role: str):
    """
    役職テーブルの一括取得

    Parameters
    ----------
    role : str
        役職

    Returns
    -------
    list of tuple
        テーブル
        [(user_name, weight),...]

    Examples
    --------
    >>> roles = ("wolf", "citizen", "diviner", "medium", "madman", "hunter", "co_owner", "hamster",)
    >>> SelectRoleTable(roles[3])
    """
    return md.selectRoleTable(role)


def SelectUsers():
    """
    ユーザのリストを返す

    Returns
    -------
    list of str
        ユーザのリスト

    Exampls
    -------
    >>> SelectUsers()
    """
    return md.selectUsers()


def AllRoleDictArray():
    """
    現在の全テーブル情報をJSONで返す。

    Returns
    -------
    allRoleDictArray: json
        全テーブル情報
    """
    allRoleDictArray = []

    for role in roles:
        allRoleDictArray.append({role: md.selectRoleTable(role)})

    return allRoleDictArray


def OutputJSON(path="./", file=""):
    """
    指定されたディレクトリパスにテーブル情報を出力する。

    Parameters
    ----------
    path : str, optional
        保存するディレクトリ, by default "./"
    file : str, optional
        ファイル名(*.json), by default "table_data_(現座の年月日)_(現在の時刻).json"
    """
    fileName = "table_data_{0:%Y%m%d}_{0:%H%M%S}.json".format(datetime.datetime.now())
    file = fileName
    filePath = path + file
    with open(filePath, "w") as fp:
        json.dump(createAllRoleDictArray(), fp, indent=2)
    return


# 以下テスト用
gotData = {
    'basic_classification': ['Coming_out', 'Request'],
    'status': 'Disagree',
    'sub_classification': 'Wolf',
    'target': None
}

users = ("AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG")
roles = ("wolf", "citizen", "diviner", "medium",
         "madman", "hunter", "co_owner", "hamster")

if __name__ == "__main__":
    # 役職テーブルの初期化
    InitDatabaseTable(users)

    print(SelectRoleTable(roles[0]))
    # 分類結果辞書とユーザ名(or ID)を引数とする
    # この関数を実行すれば重さ計算を終えて
    # テーブルの更新も終了する
    # bc.assem(gotData, "AAA")
    WeightCalc(gotData, users[0])
    # md.exiCo()

    # print(createAllRoleDictArray())
    # for role in roles:
    #     print(SelectRoleTable(role))

    # 全ユーザを取得
    # print(SelectUsers())

    # JSON形式で全テーブルを取得
    # outputJSON()
    print(SelectRoleTable(roles[0]))

    # 役職テーブルにあるデータを全て削除
    FineDatabaseTable(users, False)
