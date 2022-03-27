# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from statistics import NormalDist
muvalue = int(input("enter mu value:"))
sigma= int(input("enter your sigma value:)"))
nd=NormalDist(muvalue,sigma)
opt = int(input("No. of values:"))
if(opt == 1):
   value=int(input("Enter your value:"))
   nd.cdf(value)
else:
    value1=int(input("enter your first value:"))
    value2=int(input("Enter your second value:"))
    nd.cdf(value1)-nd.cdf(value2)

