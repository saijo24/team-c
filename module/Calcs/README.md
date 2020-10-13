# このディレクトリにあるやつらの使い方

## import

```python=
from calcs import weightcalcs
```

## 例

```python=
# データベースの初期化
weightcalcs.init_database(usrs)

# 重み計算 と データベース更新用
weightcalcs.weight_calc(data, user)
```

## 関数群

### weight_calc関数

分類結果から重みを計算し、データベースを更新する関数.

* 引数
  * data: dict・・・分類結果
  * user: str・・・誰の分類結果か

### init_database関数

データベースの初期化を行う。
重みの初期値は 10 に設定。

* 引数
  * users: list・・・ユーザリスト

### fine_database関数

データベースの内容を全て消す。

* 引数
  * users: list・・・ユーザリスト