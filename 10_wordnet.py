# -*- coding: utf-8 -*-
"""10.wordnet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bBp_tia8LHVwcKec7_PcDEv-J_dxbtWL

# 中文wordnet
完整用法：https://github.com/lopentu/CwnGraph

- 早期利用字詞表達文章的用法，可以透過查詢wordnet，找出查詢字跟那些字有關係。
- wordnet是透過人工的方式，建立起字詞之間的關係
- 本範例介紹中文的wordnet，查詢"頭"這個字，看有多少跟"頭"相關的字詞
- 另外介紹英文的wordnet，查詢跟"dog"相似的字詞
"""

!pip install CwnGraph

from CwnGraph import CwnImage
cwn = CwnImage.latest()
lemmas = cwn.find_lemma("頭")
lemmas

"""#英文wordnet
完整用法：https://www.nltk.org/howto/wordnet.html
"""

import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
wn.synsets('dog')