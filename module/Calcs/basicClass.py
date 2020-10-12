from . import manageData as md

# basicTag 基本分類辞書
Tag = {
  1:"Coming_out",
  2:"Divined_inquested",
  3:"Guard",
  4:"Vote",
  5:"Estimate",
  6:"Agree",
  7:"Disagree",
  8:"Opinion",
  9:"Information",
  10:"Question",
  11:"Ans",
  12:"Request"
}

# swapedTag 辞書のキーと値を入れ替えたもの
swapedTag = {val: key for key, val in Tag.items()}

# assem 重み計算用
def assem(data: dict, user: str):
  # 以前までの重み
  # basicClass 基本分類結果(基本は一つ)
  basicClass = data["basic_classification"][0]
  middleClass = data["basic_classification"][1]
  # subClass 基本分類の中の何なのか(付随情報)
  subClass = data["sub_classification"]
  # status Agree or Disagreeの2値判定
  status = data["status"]
  # target その文章が誰に対しての発言なのか
  target = data["target"]

  # メイン処理(start): 重み計算(ただの条件分岐)
  # カミングアウトについて
  if basicClass == "Coming_out":
    # カミングアウトで狼
    if subClass == "Wolf":
      setData("wolf", user, getData("wolf", user)*100)
    # カミングアウトで占い師
    if subClass == "Diviner":
      setData("diviner", user, getData("diviner", user)*1.3)
      setData("wolf", user, getData("wolf", user)*1.2)
      setData("madman", user, getData("madman", user)*1.2)
    # カミングアウトで霊媒師
    if subClass == "Medium":
      setData("medium", user, getData("medium", user)*1.5)
      setData("wolf", user, getData("wolf", user)*1.1)
      setData("madman", user, getData("madman", user)*1.1)
    # カミングアウトで市民
    if subClass == "Citizen":
      setData("citizen", user, getData("citizen", user)*1.5)
    # カミングアウトで共有者
    if subClass == "Co_owner":
      c = md.exiCo()
      if c <= 1:
        setData("co_owner", user, 50878.0)
      # else:
        # setData("co_owoner", )

  # 占い結果について
  if basicClass == "Divined_inquested":
    # 占い結果で人狼側だった
    if subClass == "Wolf":
      setData("wolf", target, getData("wolf", target)*2.5)
  
  # 守護する人の宣言
  if basicClass == "Guard":
    setData("diviner", target, getData("diviner", target)*1.1)
    setData("citizen", target, getData("citizen", target)*1.1)
    # 意見について
    if middleClass == "Opinion":
      # 処刑についての意見
      if subClass == "Execution":
        # 何かしらの意見をしている
        setData("citizen", user, getData("citizen", user)*1.2)
      # 進行についての意見
      if subClass == "Facilitator":
        setData("citizen", user, getData("citizen", user)*1.2)

  # 投票について
  if basicClass == "Vote":
    # 占いについて
    if subClass == "Diviner":
      setData("wolf", target, getData("wolf", target)*1.1)

  # 推測について
  if basicClass == "Estimate":
    # 人狼についての推測
    if subClass == "wolf":
      setData("wolf", target, getData("wolf", target)*1.1)
    # 狂人についての推測
    if subClass == "madman":
      setData("madman", target, getData("madman", target)*1.1)

  # 意見について
  if basicClass == "Opinion":
    # 進行についての意見
    if subClass == "Facilitator":
      if status == "Agree":
        # とりまそのまま
        setData("citizen", user, getData("citizen", user))
      else:
        # とりまそのまま
        setData("citizen", user, getData("citizen", user))
    print("")
  # メイン処理(end)
  
  return


# 決め打ちで重さを取得
def getData(role: str, user: str) -> float:
  # select文
  return float(md.select(role, user))


# 重さを更新
def setData(role: str, user: str, weight: float):
  # update文
  md.update(role, user, weight)
  return
