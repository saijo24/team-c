# team-c

## import

classification.pyをインポート。

```python=
from classfication import classification
```

加えて「psycopg2」もpipか何かでインストール。

## 引数

```python=
classfication(parsed_text)
```

## 返り値

basic_classificationは基本分類に該当する。最も可能性が高いものを1st label 二番目の可能性が一定量を超えた場合は参考値として2nd labelとして付与する。

sub_classificationはbasic_classificationの1st labelの詳細分類に該当する。

statusは否定的か肯定的のどちらか

targetはその文章で話題に出されている役職。複数ある場合は最初を優先。

```python=
{
    "basic_classification":["1st lab,"2nd label"],
    "sub_classification":["1st label detail"],
    "status":"Agree" or "Disagree",
    "target":role,
}
```

- exapmple

```python=
{
 'basic_classification': ['Request', 'Question'],
 'status': 'Disagree',
 'sub_classification': None,
 'target': 'Citizen'
}

{
 'basic_classification': [None],
 'status': 'Disagree',
 'sub_classification': None,
 'target': 'Wolf'
}
```

## メモ

basic_classificationについては現在ランダム、あとでmlpに換装する
targetは一応パターンは少ないけど読み取ってる
