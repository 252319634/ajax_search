# -*- coding: utf-8 -*-
# from models import Cnword
from pinyin import PinYin
test = PinYin()
test.load_word()
print test.hanzi2pinyin(string='钓鱼岛是中国的')
print test.hanzi2pinyin_split(string='钓鱼岛是中国的')