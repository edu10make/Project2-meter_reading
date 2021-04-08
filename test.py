import numpy as np
import pandas as pd
from flask import Flask
from flask import request
app = Flask(__name__)

df = pd.read_csv('playbook.csv')

print(df.iterrows()[1])

# book = {}
# for no, s in df.iterrows():
#     if not np.isnan(s["id"]):
#         id = str(int(s["id"]))
#         subid = str(int(s["subid"]))
#         print("{} {}".format(id, subid), flush=True)
#         if not id in book:
#             book[id] = {}
#         if not "description" in book[id]:
#             book[id]["description"] = s["description"]
#             book[id]["process"] = {}
#         book[id]["process"][subid] = {"key": s["key"], "value": s["value"]}
# print(book)
