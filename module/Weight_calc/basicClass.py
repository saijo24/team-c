from . import manageData as md
from . import datas as dts
import random


# assem 重み計算用
def assem(data: dict, user: str):
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
            # SetData("wolf", user, GetData("wolf", user)*100)
            SetData("wolf", user, willProduct("wolf", user, 100))
            # SetData("madman", user, GetData("madman", user) * random.uniform(2.0, 4.0))
            SetData("madman", user, willProduct("madman", user, random.uniform(2.0, 4.0)))
            # SetData("hamster", user, GetData("hamster", user) * random.uniform(1.0, 3.0))
            SetData("hamster", user, willProduct("hamster", user, random.uniform(1.0, 3.0)))
            SetData("citizen", user, random.uniform(0.0, 1.0))
            SetData("diviner", user, random.uniform(0.0, 1.0))
        # カミングアウトで占い師
        if subClass == "Diviner":
            SetData("diviner", user, willProduct("diviner", user, 1.3))
            SetData("wolf", user, willProduct("wolf", user, random.uniform(1.0, 2.0)))
            SetData("madman", user, willProduct("madman", user, random.uniform(1.0, 2.0)))
        # カミングアウトで霊媒師
        if subClass == "Medium":
            SetData("medium", user, willProduct("medium", user, 1.5))
            SetData("wolf", user, willProduct("wolf", user, 1.1))
            SetData("madman", user, willProduct("madman", user, 1.1))
        # カミングアウトで市民
        if subClass == "Citizen":
            SetData("citizen", user, willProduct("citizen", user, random.uniform(1.0, 3.0)))
        # カミングアウトで共有者
        if subClass == "Co_owner":
            c = md.exiCo()
            if c <= 1:
                SetData("co_owner", user, 50878.0)
            # else:
                # setData("co_owoner", )

    # 占い結果について
    if basicClass == "Divined_inquested":
        # 占い結果で人狼側だった
        if subClass == "Wolf":
            SetData("wolf", target, willProduct("wolf", target, 2.5))

    # 守護する人の宣言
    if basicClass == "Guard":
        SetData("diviner", target, willProduct("diviner", target, 1.1))
        SetData("citizen", target, willProduct("citizen", target, 1.1))
        # 意見について
        if middleClass == "Opinion":
            # 処刑についての意見
            if subClass == "Execution":
                # 何かしらの意見をしている
                SetData("citizen", user, willProduct("citizen", user, 1.2))
            # 進行についての意見
            if subClass == "Facilitator":
                SetData("citizen", user, willProduct("citizen", user, 1.2))

    # 投票について
    if basicClass == "Vote":
        # 占いについて
        if subClass == "Diviner":
            SetData("wolf", target, willProduct("wolf", target, 1.1))

    # 推測について
    if basicClass == "Estimate":
        # 人狼についての推測
        if subClass == "wolf":
            SetData("wolf", target, willProduct("wolf", target, 1.4))
        # 狂人についての推測
        if subClass == "madman":
            SetData("madman", target, willProduct("madman", target, 1.3))

    # 意見について
    if basicClass == "Opinion":
        # 進行についての意見
        if subClass == "Facilitator":
            if status == "Agree":
                # とりまそのまま
                SetData("citizen", user, GetData("citizen", user))
            else:
                # とりまそのまま
                SetData("citizen", user, GetData("citizen", user))
        print("")

    roles = ("wolf", "citizen", "diviner", "medium",
             "madman", "hunter", "co_owner", "hamster")
    for role in roles:
        normalize(role)
    # メイン処理(end)

    return


def willProduct(grole: str, guser: str, c: float) -> float:
    """
    代入するウェイト計算用

    Parameters
    ----------
    grole : str
        役職
    guser : str
        ユーザ名
    c : float
        定数倍用

    Returns
    -------
    float
    """
    gd = GetData(grole, guser)
    # 負の値を許容しない
    if c < 0:
        return gd
    else:
        return gd*c

    return gd


def normalize(role: str):
    sum = md.sumWeightThisRole(role)
    roleTable = md.selectRoleTable(role)

    for rt in roleTable:
        # print(rt)
        SetData(role, rt[0], rt[1]/sum)

    return


# 決め打ちで重さを取得
def GetData(role: str, user: str) -> float:
    # select文
    return float(md.select(role, user))


# 重さを更新
def SetData(role: str, user: str, weight: float):
    # update文
    md.update(role, user, weight)
    return
