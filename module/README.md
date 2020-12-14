# About

## import

moduleディレクトリ内のweightcalc.pyを呼び出してください。

```python=
from module import weightcalc
```

「psycopg2」もpipか何かでインストール。

## 例

```python=
```

## 関数

外部から呼び出されることを想定している関数はアッパーキャメルケースで記述している。

各関数にはDocStringで引数などの情報を記述している。

## 設定

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
