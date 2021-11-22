import os
import gspread

gc = gspread.service_account(filename="./model-gearing.json")

key = "1w7nGbgzGjFOi-e0METaVcCkpdbU5P2pb4yYvuS6h7SQ"

sh = gc.open_by_key(key)

print(sh.sheet1.get('A1:A3'))
