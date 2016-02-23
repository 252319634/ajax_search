#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path

class PinYin(object):
    def __init__(self, dict_file=r'D:\maiziedu\ajax\ajax_search\search\word.data'):
        self.word_dict = {}
        self.dict_file = dict_file


    def load_word(self):
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")
        f_obj=open(self.dict_file,'r')
        for f_line in f_obj.readlines():
            try:
                line = f_line.split('    ')
                self.word_dict[line[0]] = line[1]
            except:
                line = f_line.split('   ')
                self.word_dict[line[0]] = line[1]


    def hanzi2pinyin(self, string=""):
        result = ''
        if not isinstance(string, unicode):
            string = string.decode("utf-8")

        for char in string:
            key = '%X' % ord(char)
            result+=self.word_dict.get(key, char).split()[0][:-1].lower()

        return result