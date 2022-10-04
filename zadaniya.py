#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # 1
    school = {'1a': 20, '2b': 24, '11a': 15, '11b': 10}
    school['1a'] = 59
    school['2b'] = 127

    del school['2b']
    S = sum(school.values())
    print(school, "\nКоличество учеников: ", S, '\n')

    # 2
    a = {1: 'one', 2: 'two', 3: 'three'}
    inverse_a = {}
    for k, v in a.items():
        inverse_a[v] = k
    print(a)
    print(inverse_a)
