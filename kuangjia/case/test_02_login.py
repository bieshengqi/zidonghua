# 这个文件是登陆的case
import os, sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.dbtools import query
from utils.filetools import read_file,save_file
from utils.common import get_url
from utils.exceltools import read_excel

data = read_excel("./data/测谈网接口.xlsx", "登录")

def test_01_success():
    u = get_url(data[0][2])
    h = eval(data[0][5])
    d = eval(data[0][4])
    res = requests.post(url=u,headers=h,json=d)
    assert res.status_code == data[0][6]
    assert res.json()["status"] == data[0][7]
    # print(res.text)
    sql = "select * from t_user where username = '{}'".format(d["username"])
    assert len(query(sql)) != 0
    token = res.json()["data"]["token"]
    save_file(content=token)