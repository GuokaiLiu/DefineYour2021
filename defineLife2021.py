#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   defineLife.py
@Time    :   2020/12/31 10:24:04
@Author  :   GuokLiu
@Contact :   liuguokai@hust.edu.cn
@Institution   :  Huazhong Univ. of Sci. and Tech.
@Desc    :   2021 wishes
'''

class life():
    def __init__(self,vrs,sad,vac,tra,fmG,frG,lvA,hap,pap):
        # negative
        self.virus = vrs
        self.sadness = sad
        # positive
        self.vaccine = vac
        self.travel = tra
        self.familyGathering = fmG
        self.friendGathering = frG
        self.loversAccompany = lvA
        self.paper = pap
        self.happiness = hap

    def check(self):
        self.negative = self.virus + self.sadness 
        self.positive = self.vaccine + self.travel + self.familyGathering + self.familyGathering +  self.loversAccompany + self.happiness

    def wishes(self):
        if self.negative == 0 and self.positive == 6:
            print('Nothing but all the best wishes!')
            print('May {} be with you!'.format(self.paper))
        else:
            print('Please redeine your life 2021!')

# Define
yourLife2021 = life(vrs=False,sad=False,vac=True,tra=True,fmG=True,frG=True,lvA=True,hap=True,pap='Nature or Science')

# Check
yourLife2021.check()

# Wish
yourLife2021.wishes()