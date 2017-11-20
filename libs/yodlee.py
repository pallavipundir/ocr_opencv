import pandas as pd

#importing files
yod_user = pd.read_excel("C:\\Users\\pallavi.pundir\\Downloads\\excel files\\yod_user.xlsx")
yod_bank = pd.read_excel("C:\\Users\\pallavi.pundir\\Downloads\\excel files\\yod_bank.xlsx")

for i in yod_user.id:
    for j in yod_bank.yodlee_user_id:
        if (i == j):
            print(i,j)