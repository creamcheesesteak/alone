import sqlite3
import pandas as pd
import openpyxl


db_nation = sqlite3.connect('./nation.db')
c = db_nation.cursor()

# creat table
c.execute("CREATE TABLE nation2 (id INTEGER PRIMARY KEY, App TEXT, App_c Text, App_cat TEXT)")

# input values
path = 'C:/Users/LimTH/Desktop/practice/alone/i_f_Brazil.xls'
dfs = pd.read_excel(path, header=None)
file_name = path[path.rfind('/')+1:]
id = 0
for row in dfs.iterrows():
    app = row[1][0]
    app_c = row[1][1]
    app_cat = row[1][2]
    c.execute("INSERT INTO nation1(id, App, App_c, App_cat) VALUES(?,?,?,?) ", (id, app, app_c, app_cat))
    id += 1
db_nation.commit()


