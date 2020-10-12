import psycopg2

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


# InitDatas データベースにデフォルト値10.0をブチ込む
def InitDatas(users: list):
  # 「重要」 役職テーブルは既に作られているとする
  roles = ("wolf","citizen","diviner","medium","madman","hunter","co_owner","hamster",)

  # ふぉ〜
  for role in roles:
    for user in users:
      # 重さのデフォルト値を10.0とする
      cursor.execute("INSERT INTO " + role + " VALUES ('" + user + "', 10.0" + ");")
      connect.commit()

  return


# select 役職テーブルのユーザの重さを取得
def select(role: str, user: str) -> float:
  cursor.execute("SELECT weight FROM " + role + " WHERE user_name='" + user + "';")
  ret = cursor.fetchone()
  return ret[0]


# update 役職テーブルのユーザの重さの更新
def update(role: str, user: str, weight: float):
  cursor.execute("UPDATE " + role + " SET weight=" + str(weight) + " WHERE user_name='" + user + "';")
  return


# exiCo 共有者の数をカウントする
def exiCo() -> int:
  cursor.execute("SELECT weight FROM co_owner;")
  get = cursor.fetchall()
  count = 0
  for g in get:
    if g[0] == 50878.0:
      count+=1

  return count

# FineDatas 役職テーブルのデータを全部消す(一応)
def FineDatas(users: list):
  # 「重要」 役職テーブルは既に作られているとする
  roles = ("wolf", "citizen", "diviner", "medium","madman", "hunter", "co_owner", "hamster",)

  # ふぉ〜
  for role in roles:
    for user in users:
      cursor.execute("DELETE FROM " + role + " WHERE user_name='" + user + "';")
      connect.commit()

  return
