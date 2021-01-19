import psycopg2
import json

# dbName データベース名
dbName = "pdmWolf"
# userName ユーザ名
userName = "pdm"
# password パスワード
password = "pdm"

# コネクト
connect = psycopg2.connect("user=" + userName + " dbname=" + dbName + " password=" + password)
# カーソル
cursor = connect.cursor()


def initDatas(users: list):
    """
    データベースの初期化を行う。
    全ユーザに重み10.0を設定する。

    Parameters
    ----------
    users : list of str
        全ユーザのリスト
    """
    createAllTables()
    roles = ("wolf", "citizen", "diviner", "medium", "madman", "hunter", "co_owner", "hamster",)
    userNum = len(users)
    w = 1/userNum

    for role in roles:
        for user in users:
            # 重さのデフォルト値を10.0とする
            # sen = "INSERT INTO " + role + " VALUES ('" + user + "', 10.0);"
            cursor.execute("INSERT INTO " + role + " VALUES (%s, " + str(w) + ");", (user,))
    connect.commit()

    return


def createAllTables():
    """
    役職テーブルの作成
    """
    roles = ("wolf", "citizen", "diviner", "medium", "madman", "hunter", "co_owner", "hamster",)
    for role in roles:
        cursor.execute("CREATE TABLE IF NOT EXISTS " + role + " (user_name text, weight real);")

    connect.commit()
    return


def delectAllTables():
    """
    役職テーブルの削除
    """
    roles = ("wolf", "citizen", "diviner", "medium", "madman", "hunter", "co_owner", "hamster",)
    for role in roles:
        cursor.execute("DROP TABLE IF EXISTS " + role + ";")

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
    cursor.execute("SELECT weight FROM " + role + " WHERE user_name='" + user + "';")
    ret = cursor.fetchone()
    return ret[0]


def selectRoleTable(role: str):
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
    if role == "wolf":
        cursor.execute("SELECT * FROM wolf")
        res = cursor.fetchall()
    elif role == "citizen":
        cursor.execute("SELECT * FROM citizen")
        res = cursor.fetchall()
    elif role == "diviner":
        cursor.execute("SELECT * FROM diviner")
        res = cursor.fetchall()
    elif role == "medium":
        cursor.execute("SELECT * FROM medium")
        res = cursor.fetchall()
    elif role == "madman":
        cursor.execute("SELECT * FROM madman")
        res = cursor.fetchall()
    elif role == "hunter":
        cursor.execute("SELECT * FROM hunter")
        res = cursor.fetchall()
    elif role == "co_owner":
        cursor.execute("SELECT * FROM co_owner")
        res = cursor.fetchall()
    elif role == "hamster":
        cursor.execute("SELECT * FROM hamster")
        res = cursor.fetchall()
    else:
        print("[ERROR]存在しない役職が指定されています。")
    return res


def sumWeightThisRole(role: str) -> float:
    """
    指定された役職テーブルのウェイトの合計

    Parameters
    ----------
    role : str
        役職名

    Returns
    -------
    float
    """
    res = 0.0
    dic = selectRoleTable(role)
    for d in dic:
        res += d[1]

    return res


def selectUsers():
    """
    ユーザのリストを返す

    Returns
    -------
    list of str
        ユーザのリスト
    """
    users = []
    cursor.execute("SELECT user_name FROM wolf;")
    res = cursor.fetchall()
    for r in res:
        users.append(r[0])

    users.sort()
    return users


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
    cursor.execute("UPDATE " + role + " SET weight=" + str(weight) + " WHERE user_name='" + user + "';")
    return


def exiCo() -> int:
    """
    共有者の数をカウントする。
    ただし現環境では使えない。

    Returns
    -------
    int
        共有者(っぽい)数
    """
    cursor.execute("SELECT weight FROM co_owner;")
    get = cursor.fetchall()
    count = 0
    for g in get:
        if g[0] == 50878.0:
            count += 1

    return count


# fineDatas 役職テーブルのデータを全部消す(一応)
def fineDatas(users: list, table_delete=False):
    """
    ゲームの終了処理

    Parameters
    ----------
    users : list of str
        ユーザのリスト
    table_delete : bool, optional
        テーブルも削除するのか, by default False
    """
    roles = ("wolf", "citizen", "diviner", "medium", "madman", "hunter", "co_owner", "hamster",)

    for role in roles:
        for user in users:
            cursor.execute("DELETE FROM " + role + " WHERE user_name='" + user + "';")

    connect.commit()

    if table_delete:
        delectAllTables()

    return
