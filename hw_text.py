#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:10:44 2020

@author: nia
"""
#Определения и термины¶
#Буква - один символ латинского алфавита в верхнем иил нижнем регистре.
#Цифра - это один сивол десятичной цифры от 0 до 9.
#Число - последовательность цифр, которые идут подряд.
#Специальный символ - всё, что не является буквой или цифрой, например, знаки препинания, 
#скобки и т.п.
#Слово - от 1 до N символов (буквы, цифры), которые идут подряд (специальные символы не 
#считаются словами).
#ПРедложение - всё, что до точки.

# ТЕКСТ ДЛЯ АНАЛИЗА
TEXT = """
The term "data science" has appeared in various contexts over the past thirty years but did not become an established term until recently. In an early usage, it was used as a substitute for computer science by Peter Naur in 1960. Naur later introduced the term "datalogy".[15] In 1974, Naur published Concise Survey of Computer Methods, which freely used the term data science in its survey of the contemporary data processing methods that are used in a wide range of applications.

In 1996, members of the International Federation of Classification Societies (IFCS) met in Kobe for their biennial conference. Here, for the first time, the term data science is included in the title of the conference ("Data Science, classification, and related methods"),[16] after the term was introduced in a roundtable discussion by Chikio Hayashi.[3]

In November 1997, C.F. Jeff Wu gave the inaugural lecture entitled "Statistics = Data Science?"[17] for his appointment to the H. C. Carver Professorship at the University of Michigan.[18] In this lecture, he characterized statistical work as a trilogy of data collection, data modeling and analysis, and decision making. In his conclusion, he initiated the modern, non-computer science, usage of the term "data science" and advocated that statistics be renamed data science and statisticians data scientists.[17] Later, he presented his lecture entitled "Statistics = Data Science?" as the first of his 1998 P.C. Mahalanobis Memorial Lectures.[19] These lectures honor Prasanta Chandra Mahalanobis, an Indian scientist and statistician and founder of the Indian Statistical Institute.

In 2001, William S. Cleveland introduced data science as an independent discipline, extending the field of statistics to incorporate "advances in computing with data" in his article "Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics," which was published in Volume 69, No. 1, of the April 2001 edition of the International Statistical Review / Revue Internationale de Statistique.[20] In his report, Cleveland establishes six technical areas which he believed to encompass the field of data science: multidisciplinary investigations, models and methods for data, computing with data, pedagogy, tool evaluation, and theory.

In April 2002, the International Council for Science (ICSU): Committee on Data for Science and Technology (CODATA)[21] started the Data Science Journal,[22] a publication focused on issues such as the description of data systems, their publication on the internet, applications and legal issues.[23] Shortly thereafter, in January 2003, Columbia University began publishing The Journal of Data Science,[24] which provided a platform for all data workers to present their views and exchange ideas. The journal was largely devoted to the application of statistical methods and quantitative research. In 2005, The National Science Board published "Long-lived Digital Data Collections: Enabling Research and Education in the 21st Century" defining data scientists as "the information and computer scientists, database and software and programmers, disciplinary experts, curators and expert annotators, librarians, archivists, and others, who are crucial to the successful management of a digital data collection" whose primary activity is to "conduct creative inquiry and analysis."[25]

Around 2007,[citation needed] Turing award winner Jim Gray envisioned "data-driven science" as a "fourth paradigm" of science that uses the computational analysis of large data as primary scientific method[4][5] and "to have a world in which all of the science literature is online, all of the science data is online, and they interoperate with each other."[26]

In the 2012 Harvard Business Review article "Data Scientist: The Sexiest Job of the 21st Century",[6] DJ Patil claims to have coined this term in 2008 with Jeff Hammerbacher to define their jobs at LinkedIn and Facebook, respectively. He asserts that a data scientist is "a new breed", and that a "shortage of data scientists is becoming a serious constraint in some sectors", but describes a much more business-oriented role.

In 2013, the IEEE Task Force on Data Science and Advanced Analytics[27] was launched. In 2013, the first "European Conference on Data Analysis (ECDA)" was organised in Luxembourg, establishing the European Association for Data Science (EuADS). The first international conference: IEEE International Conference on Data Science and Advanced Analytics was launched in 2014.[28] In 2014, General Assembly launched student-paid bootcamp and The Data Incubator launched a competitive free data science fellowship.[29] In 2014, the American Statistical Association section on Statistical Learning and Data Mining renamed its journal to "Statistical Analysis and Data Mining: The ASA Data Science Journal" and in 2016 changed its section name to "Statistical Learning and Data Science".[30] In 2015, the International Journal on Data Science and Analytics[31] was launched by Springer to publish original work on data science and big data analytics. In September 2015 the Gesellschaft für Klassifikation (GfKl) added to the name of the Society "Data Science Society" at the third ECDA conference at the University of Essex, Colchester, UK.
"""

#1. Найти количество букв в тексте¶
#в разрезе:
#всего
#верхний регистр
#нижний регистр
#Результат записать в словарь с ключами:
#"total"
#"upper"
#"lower"

#letters=[l for l in TEXT if l.isalpha()]
letters=list()
for l in TEXT:
    if l.isalpha():
        letters.append(l)

print(letters)


#розрахунок кількості букв всього
total=len(letters)
print(total)

count_ll=0
for ll in letters:
    if ll.islower():
        count_ll+=1
print(count_ll)

count_ul=0
for ul in letters:
    if ul.isupper():
        count_ul+=1
print(count_ul)        

letter_dict={'total':total, 'lower':count_ll, 'upper':count_ul}

#2. Неупорядоченный список количества букв¶
#Найти количество каждой букве в тексте. Результат записать в список, где каждый
# элемент – это кортеж(буква, количество).

s=set(letters)
print(s)
C=letters.count('C')
list_k=list()
for x in s:
    list_k.append((x,letters.count(x)))
print(list_k)   
     
    
#3. Упорядоченный список количества букв¶
#Создать список на основе списка из задачи №2, в котором элементы отсортированы
# по количеству букв.
sort_l=sorted(list_k, key=lambda x:x[1],reverse = True )
print(sort_l)

#4. Найти общее количество слов в тексте; результат записать как int.¶
from string import whitespace, punctuation
symbols_trans = str.maketrans(punctuation, ' '*len(punctuation))


words=TEXT.translate(symbols_trans).split()
#words=TEXT.replace('.',' ').replace(',',' ').replace(':',' ').replace(';',' ').split()
words_count=len(words)

#5 Найти количество чисел в тексте, результат записать как int;¶

numbers=list(filter(lambda x: x.isdigit(),words))
su_m=len(numbers)
print(su_m)

#6. Создать dict, в котором Ключи - длина слова, а Значения - количество слов с такой длиной;¶
dict_words=dict()
for x in words:
    l=len(x)
    if dict_words.get(l)==None:
        dict_words[l]=1
    else:
        dict_words[l]+=1
print(dict_words)
        
#7. Найти долю предложений, в коотрых встречается словосочетание "Data Science"; результат записать как число float < 1.¶
state=TEXT.split('.')
state_ds=list(filter(lambda x: "Data Science" in x, state))
s=len(state)
sd=len(state_ds)
part=sd/s
print(part)


#8. Найти колчичество специалных символов в тектсе, результат записать в dict, в котором¶
#Ключи - специальные символы, значения - их количество
simbol=dict()
for x in TEXT:
    if x in punctuation:
        if simbol.get(x)==None:
            simbol[x]=1
        else: 
            simbol[x]+=1
print(simbol)

#9. Создать список букв в верхнем регистре, отсортированных по их количеству¶
letters=list()
for l in TEXT:
    if l.isalpha():
        letters.append(l)

print(letters)

ll_up=list()
#ll_up=list(filter(lambda x: x.isupper(),letters))
#print(ll_up)
for x in letters:
    if x.isupper():
        ll_up.append(x)
print(ll_up)

print(set(ll_up))
ll_up_dict=dict()
for x in set(ll_up):
    ll_up_dict[x]=ll_up.count(x)
sort_ll_up=sorted(ll_up_dict.items(), key=lambda x:x[1])
print(sort_ll_up)
print(ll_up_dict.items())
z=list(map(lambda x:x[0], sort_ll_up)) 
print(z)   

#10. Найти буквы, которые встречаются чаще и реже всех остальных. 
#Результат записать как tuple.¶
('max','k')
zzz=sort_l[0][0]
print(zzz)
xxx=sort_l[-1:-4][0]
print(xxx)
max1=max(sort_l,key=lambda x:x[1])[1]
min1=min(sort_l,key=lambda x:x[1])[1]

l_max=list(filter(lambda x:x[1]==max1,sort_l))
l_min=list(filter(lambda x:x[1]==min1,sort_l))

t=(list(map(lambda x:x[0],l_max)),list(map(lambda x:x[0], l_min)))
print (t)
#
#11. Найти все числа и записать их в list, отсортировав их 
#от большего к меньшему.¶
number=list()
   
for x in words:
    
    if x.isdigit():
        number.append(int(x))
        
number.sort(reverse = True) 
  
print(number)



#12. Найти минимальное и максимальное число;
# результат записать как tuple(меньшее, большее)¶


numbers=list(filter(lambda x: x.isdigit(),words))
su_m=len(numbers)
print(su_m)
#
#13. Найти абзац, в котором "Data Science" встречается наиболее часто;
# результат - строка с текстом этого абзаца.¶

d_s=TEXT.split('\n')
s=''
m=0
for d in d_s:
    h=d.count('Data Science')
    if h>m:
        m=h
        s=d
print(s,m)    
    
#14. Создать dict, в котором¶
#Ключи - это слово
#Значения - количество раз упоминания его в тексте
for x in words:
    
    if dict_words.get(x)==None:
        dict_words[x]=1
    else:
        dict_words[x]+=1
print(dict_words)


#15. Найти слова, которые встречаются чаще и реже других.¶
#Результат записать как
#tuple(
#    tuple(самое_редкое_слово, количество), 
#    tuple(самое_популярное_слово, количество)dict_words=dict()

max_words=max(dict_words.items(),key=lambda x: x[1])
min_words=min(dict_words.items(),key=lambda x: x[1])
a=(max_words, min_words)
print(a)
