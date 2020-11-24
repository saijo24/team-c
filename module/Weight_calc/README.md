# About

## import

moduleディレクトリ内のweightcalc.pyを呼び出してください。

```python=

```

「psycopg2」もpipか何かでインストール。

## 例

```python=
```

## 関数群

### WeightCalc(data: dict, user: str)

引数のdataは次の形を想定している。

```python=
data = {
    'basic_classification': ['Coming_out', 'Request'],
    'status': 'Disagree',
    'sub_classification': 'Wolf',
    'target': None
}
```

## 設定

データベースの設定はsettings.jsonに書く(未実装)。

初期設定は次の通り

```json
{
  "database":{
    "name": "pdmWolf",
    "user": "pdm",
    "password": "pdm"
  }
}
```
