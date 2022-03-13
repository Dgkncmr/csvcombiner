import glob
import time

import pandas as pd
import os


#verilerin yüklenmesi
# df = pd.DataFrame()
#
# all_filenames = [i for i in glob.glob("files\d\*.csv")]
# for f in all_filenames:
#     df = pd.concat([df,pd.read_csv(f, header=None) ],ignore_index=True)
#
# df.columns = ['Open time','Open', 'High', 'Low', 'Close','Volume','Close time','Quote asset volume ','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Ignore']
#
# df.to_csv("C:/PycharmProjects/webserver2/files/d/btc.csv")
# print(df)

def Main():
    while True:
        df = pd.DataFrame()
        path = input("Where is the csv folder?")
        all_filenames = [i for i in glob.glob(f'{path}\*.csv')]
        for f in all_filenames:
            df = pd.concat([df, pd.read_csv(f, header=None)], ignore_index=True)

        x = input("If you wanna add column name?(Y/N)")
        if (x == "Y" or x == "y"):
            col = input("Add column/columns name?(Add like 'col1','col2',...")
            col = col.split(",")
            df.columns = [col]
        if(x == "N" or "n"):
            pass
        folder_path = input("Where should I save?")
        csv_name = input("What is the csv name?")
        df.to_csv(f'{folder_path}/{csv_name}.csv')
        z = input("Do you wanna continue?(q for quit or any button for continue)")
        if (z == "q"):
            print("Program is shutting down.")
            time.sleep(1)   
            break
        else:
            continue

if __name__ == "__main__":
    Main()

