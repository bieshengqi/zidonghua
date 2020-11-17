import os, sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.dbtools import query
from utils.filetools import read_file,save_file
from utils.common import get_url
from utils.exceltools import read_excel

data = read_excel("./data/测谈网接口.xlsx", "文章")

def test_01_new_aritcle():
    """
    新建文章case
    """
    u = get_url(data[0][2])
    h = eval(data[0][5])
    d = eval(data[0][4])
    res = requests.post(url=u,headers=h,json=d)
    # print(res.text)
    assert res.status_code == data[0][6]
    assert res.json()["status"] == data[0][7]
    aid = res.json()["data"]["articleid"]
    sql = "select * from t_article where id = {}".format(aid)
    assert len(query(sql)) != 0