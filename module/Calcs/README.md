# このディレクトリにあるやつらの使い方

## 例

```python=
# データベースの初期化
manageData.InitDatas(usrs)

# 重み計算 と データベース更新用
basicClass.Assem(data, user)
```

## manageData.py

### InitDatas関数

データベースの初期化を行う。
与えられたユーザのリストで各役職のカラムにデータを入れる準備を行う。
重みの初期値は 10 とした。

* 引数
  * users: list ・・・ユーザリスト、ダブり無し

### FineDatas関数

データベースを空にする。

* 引数
  * users: list ・・・ユーザリスト、ダブり無し

## basicClass.py

### Assem関数

重み計算とデータベースの更新を行う。

* 引数
  * data: dict ・・・分類結果辞書を受け取る
  * user: str ・・・誰が発言した内容か

### GetData関数

役職とユーザ名で、その重みを取得する。

* 引数
  * role: str・・・役職名
  * user: str・・・ユーザ名
* 戻り値
  * float・・・重み

### SetData関数

役職とユーザ名で重みを更新する。

* 引数
  * role: str・・・役職名
  * user: str・・・ユーザ名
  * weight: float・・・重み
