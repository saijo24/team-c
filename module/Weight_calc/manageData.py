import psycopg2
import json

# jsonから対象のデータベースを作成
fileName = "utls/settings.json"
openedJson = open(fileName, "r")
loadedJson = json.load(openedJson)

# dbName データベース名
dbName = loadedJson["database"]["name"]
# userName ユーザ名
userName = loadedJson["database"]["user"]
# password パスワード
password = loadedJson["database"]["password"]

# コネクト
connect = psycopg2.connect(
    "user=" + userName + " dbname=" + dbName + " password=" + password)
# カーソル
cursor = connect.cursor()


# initDatas データベースにデフォルト値10.0をブチ込む
def initDatas(users: list):
    # 「重要」 役職テーブルは既に作られているとする
    roles = ("wolf", "citizen", "diviner", "medium",
             "madman", "hunter", "co_owner", "hamster",)

    # ふぉ〜
    for role in roles:
        for user in users:
            # 重さのデフォルト値を10.0とする
            # sen = "INSERT INTO " + role + " VALUES ('" + user + "', 10.0);"
            cursor.execute("INSERT INTO " + role +
                           " VALUES (%s, 10.0);", (user,))
    connect.commit()

    return


def select(role: str, user: str) -> float:
    """
    役職テーブルからユーザの重さを取得します。

    Parameters
    ----------
    role : str
        役職
    user : str
        テーブルに登録されているユーザ名

    Returns
    -------
    ret[0]
        指定された重さ
    """
    cursor.execute("SELECT weight FROM " + role +
                   " WHERE user_name='" + user + "';")
    ret = cursor.fetchone()
    return ret[0]


def selectAll(role: str):
    """
    役職のテーブルデータを全取得

    Parameters
    ----------
    role : str
        役職(テーブル)

    Returns
    -------
    res: dict
        多分辞書型
    """
    cursor.execute("SELECT * FROM %s", (role,))
    res = cursor.fetch()
    return res


# update 役職テーブルのユーザの重さの更新
def update(role: str, user: str, weight: float):
    """
    役職テーブルの指定されたユーザの重さの更新

    Parameters
    ----------
    role : str
        役職
    user : str
        ユーザ名(テーブルに保存されている)
    weight : float
        更新後の重さ
    """
    cursor.execute("UPDATE " + role + " SET weight=" +
                   str(weight) + " WHERE user_name='" + user + "';")
    return


# exiCo 共有者の数をカウントする
def exiCo() -> int:
    cursor.execute("SELECT weight FROM co_owner;")
    get = cursor.fetchall()
    count = 0
    for g in get:
        if g[0] == 50878.0:
            count += 1

    return count


# fineDatas 役職テーブルのデータを全部消す(一応)
def fineDatas(users: list):
    # 「重要」 役職テーブルは既に作られているとする
    roles = ("wolf", "citizen", "diviner", "medium",
             "madman", "hunter", "co_owner", "hamster",)

    # ふぉ〜
    for role in roles:
        for user in users:
            cursor.execute("DELETE FROM " + role +
                           " WHERE user_name='" + user + "';")
            connect.commit()

    return
