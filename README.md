# word2vec おためし

## さんこう

http://antibayesian.hateblo.jp/entry/2014/03/10/001532

## すること

※ Windows 環境なので Python2/3 両方入れたうえで `py` で 2 系を明示して使ってます
※ 違う環境とかの場合はなんか適宜読み替えて下さい

```cmd
> py -2 getdat.py http://uni.open2ch.net/ gameswf/ 艦これ > kankore.txt
> & 'C:\Program Files (x86)\MeCab\bin\mecab.exe' -Owakati .\kankore.txt > wakati_kankore.txt
```

open2ch の当該板における指定ワードを使用してレスを全部取得、mecab で分かち書き

```cmd
> py -2 -m pip install gensim
```

## つかいかた

```cmd
> py -2
```

して python のコマンドラインに移行後、コマンドラインに下記をコピペ

```python
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('wakati_kankore.txt')
model = word2vec.Word2Vec(sentences, size=200)

def s(posi, nega=[], n=5):
    cnt = 1
    result = model.most_similar(positive = posi, negative = nega, topn = n)
    print '順位', 'キャラ名', '類似度'
    for r in result:
        print cnt, r[0], r[1]
        cnt += 1
```

で、そのまま python コマンドラインでおためしする。

```python
>>> s([u'鹿島'])
順位 キャラ名 類似度
1 妹 0.871128022671
2 様 0.861209869385
3 嫁 0.851140677929
4 加賀 0.840426325798
5 天龍 0.8387170434
```

....んー？
~~やはりおーぽんは信用ならんか~~
