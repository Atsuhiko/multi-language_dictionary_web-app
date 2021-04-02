# 参考: https://www.python.ambitious-engineer.com/archives/1630
# 参考: https://note.com/kamakiriphysics/n/n2aec5611af2a
# 参考:  https://qiita.com/Gen6/items/2979b84797c702c858b1

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, g, flash
import pandas as pd
import numpy as np

app = Flask(__name__)

class multi_dic:
    def __init__(self, df):
        self.df = df
    def trans_jp(self, e):
        jp = self.df[self.df["Eng"] == e]["Jap"]
        jp = str(np.array(jp)[0])
        return jp
    def trans_de(self, e):
        de = self.df[self.df["Eng"] == e]["Deu"]
        de = str(np.array(de)[0])
        return de

@app.route("/", methods=["GET","POST"])
def upload_file():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":

        eng = request.form['eng']
        kind = request.form.get('kind')

        df = pd.read_csv("dic.csv")
        dic = multi_dic(df)

        if kind == "jp":
            trans = dic.trans_jp(eng)
        elif kind == "de":
            trans = dic.trans_de(eng)
        
        return render_template("index.html", trans=trans)
      
if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0', port=3456) # ポートの変更
