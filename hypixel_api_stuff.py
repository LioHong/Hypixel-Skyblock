# -*- coding: utf-8 -*-
"""
Filename: hypixel_api_stuff.py
Date created: Wed Aug 26 00:06:16 2020
@author: Julio Hong
Purpose: Mess around with Hypixel's API to check own stats
Steps: 
Track bank balance over time
Track player location over time?
I just discovered that the minions hold onto the coins. How do I track that?

"""
import requests
import datetime as dt
from time import sleep
import pandas as pd
import os
from openpyxl import load_workbook

# To adjust the dataframe appearance
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 200)

api_key = '4aa4f936-c170-4a8e-849a-4418f76c8fe5'
payload = {'key': api_key}
player_name = 'LapisLiozuli'
hypixel_player_data = requests.get(
        'https://api.hypixel.net/player?key=' + api_key 
        + '&name=' + player_name, params=payload)
uuid = hypixel_player_data.json()['player']['uuid']
txn_series = pd.Series([])


# Let this run so can check whether I earn from auto bazaar sales or interest over time
print('Pulling balance data')
while True: 
    try:
        print('Pulling for this instance...')
        hsb_player_data = requests.get(
            'https://api.hypixel.net/skyblock/profiles?key='+ api_key
            + '&uuid=' + uuid, params=payload)

        # # This is a list of a single giant dict
        # hsb_player_data.json()['profiles']
        # Take out the single giant dict and look for all transactions under banking
        banking_data = hsb_player_data.json()['profiles'][0]['banking']
        # type(banking_data) = dict
        # transactions_data = banking_data['transactions']
        balance_data = banking_data['balance']
        txn_series[dt.datetime.now()] = balance_data

        # Recording balance over time is ok
        # But keeping track of all transactions would be most accurate
        sleep(5)

    except KeyboardInterrupt:
        # Put this here so I don't keep making new sheets every time I run the export section
        # Excel can't accept ":" in sheet name
        timestamp = str(dt.datetime.now()).replace(':', '_')
        break

txn_series.name = 'balance'
record_file_path = r"C:\Users\Julio Hong\Documents\GitHub\Minecraft\Hypixel Skyblock\bank_balance_record.xlsx"
print('Exporting results to Excel')
if os.path.exists(record_file_path):
        print('Update existing bank balance')
        book = load_workbook(record_file_path)
        writer = pd.ExcelWriter(record_file_path, engine='openpyxl')
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
else:
        print('Create new bank balance')
        writer = pd.ExcelWriter(record_file_path, engine='xlsxwriter')
txn_series.to_excel(writer, sheet_name=timestamp)
# txn_series.to_excel(writer, sheet_name='test')
writer.save()
writer.close()

# Load the sheet?

# Note: Takes a while to update after a transaction is made ingame
# Records all transactions after timestamp = 1598372151967
timestamp = 1598372151967 / 1000
dt_object = dt.datetime.fromtimestamp(timestamp)
print("dt_object =", dt_object)