# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:58:47 2023

@author: Sh_Jurayeff
"""


car0={'model':'lacetti',
      'rang':'oq',
      'yil':2018,
      'narh':13000,
      'km':90000,
      'karobka':'avtomat'}

car1={'model':'cobalt',
      'rang':'kulrang',
      'yil':2020,
      'narh':14000,
      'km':10000,
      'karobka':'avtomat'}

car2={'model':'jiguli',
      'rang':'qora',
      'yil':2000,
      'narh':3000,
      'km':70000,
      'karobka':'mexanika'}

cars=[car0,car1,car2]
#for car in cars:
#    print(f"{car['model'].title()}, "
#          f"{car['rang']} rang, "
#          f"{car['yil']}-yil , {car['narh']}$")
    
#print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")

malibus=[]
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2000,
        'narh':None,
        'km':0,
        'karobka':'avto'
        }
    malibus.append(new_car)
#    print(malibus)

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'
#for malibu in malibus:
#    print(malibu)
    
for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'
#for malibu in malibus:
#    print(malibu)
    
for malibu in malibus[6:]:
    malibu['rang'] = 'oq'
    malibu['karobka']='mexanika'
#for malibu in malibus:
#    print(malibu)

for malibu in  malibus:
    if malibu['karobka'] =='avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000
        
#for malibu in malibus:
#    print(malibu)
     
                                    #LUG'AT ICHIDA RO'YXAT

dasturchilar={
    'ali':['python','c++'],
    'vali':['html','css'],
    'hasan':['java','kotlin'],
    'ibn':['python','C#'],
    'husan':['.net','php'],
    'yusuf':['NodeJS','mongodb']
    }

for ism , tillar in  dasturchilar.items():
     print(f" \n {ism.title()} quyidagi tillarni biladi:" , end=" ")
     for til in tillar:
         
         print(f"{til.upper()}" , end=" ")









