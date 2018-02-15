import pandas as pd
import numpy as np
tg_dinner= pd.read_csv('Datafiles/tg_dinner.csv',encoding="Latin-1")

print(tg_dinner[0:10])

print(tg_dinner.columns)        #displays colums names

print(tg_dinner["Do you celebrate Thanksgiving?"].value_counts())

celebrate_true=tg_dinner["Do you celebrate Thanksgiving?"]=="Yes"

tg_dinner=tg_dinner[celebrate_true]
#print(tg_dinner)

print(tg_dinner["What is typically the main dish at your Thanksgiving dinner?"].value_counts())

print(tg_dinner["Do you typically have gravy?"][tg_dinner["What is typically the main dish at your Thanksgiving dinner?"]=="Tofurkey"])


Apple_null= tg_dinner["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].isnull()
Pumpkin_null=tg_dinner["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].isnull()
Pecan_null=tg_dinner["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].isnull()

ate_pies=Apple_null&Pumpkin_null&Pecan_null

print(ate_pies.value_counts())


def age_con(string):   
    if pd.isnull(string)==True:
        return None
    else:
        age=string.split(" ")[0]
        age=age.replace("+", "")  
        return int(age)
tg_dinner["int_age"]=tg_dinner["Age"].apply(age_con)
print(tg_dinner["int_age"].describe())

def money(string):   
    if pd.isnull(string)==True:
        return None
    else:
        money=string.split(" ")[0]
        if(string[0]=="P"):
            return None
        else:
            money=money.replace("$", "")
            money=money.replace(",", "")              
            return int(money)
tg_dinner["int_income"]=tg_dinner["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(money)
print(tg_dinner["int_income"].describe())


incomel150000=tg_dinner["int_income"]<150000
print(tg_dinner["How far will you travel for Thanksgiving?"][incomel150000].value_counts())
print(len(tg_dinner["How far will you travel for Thanksgiving?"][incomel150000]))

incomeg150000=tg_dinner["int_income"]>150000
print(tg_dinner["How far will you travel for Thanksgiving?"][incomeg150000].value_counts())
print(len(tg_dinner["How far will you travel for Thanksgiving?"][incomeg150000]))


print(tg_dinner.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns='Have you ever attended a "Friendsgiving?"', values="int_age"))

print(tg_dinner.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns='Have you ever attended a "Friendsgiving?"', values="int_income"))












