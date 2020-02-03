#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:12:39 2020

@author: nia

"""

z_dict=dict()
s=' '
while s!='':
    s=input('Enter the words: ')
    
    if s=='':
        break
    s=s.replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ')
    s_list=s.split()    
        
    for y in set(s_list):
        #print(y)
        if y in z_dict:          
            z_dict[y]+=s_list.count(y)
        else:
            z_dict[y]=s_list.count(y)
            
#print(z_dict)

l=z_dict.keys()

l_max=len(max(l,key=lambda x:len(x)))

for o in z_dict.keys():
    
    word_l=l_max -len(o)
    
    print('|%s %s| %d |'%(o, ' '*word_l, z_dict[o]))
    
    
    
    
    
    
    
    
    
    
    

