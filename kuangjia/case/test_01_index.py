# 首页的所有接口都放到这里
import os, sys
sys.path.append(os.getcwd())

import pytest
import requests
from utils.common import get_url
from utils.exceltools import read_excel

data = read_excel("./data/测谈网接口.xlsx", "首页")

# 方法来表示每个测试用例
def test_01_lbt():
    url = get_url(data[0][2])
    res = requests.get(url=url)
    assert res.status_code == data[0][6]
    assert res.json()["status"] == data[0][7]

def test_02_getcoures():
    url = get_url(data[1][2])
    res = requests.get(url=url)
    assert res.status_code == data[1][6]
    assert res.json()["status"] == data[1][7]

def test_03_getquestions():
    url = get_url(data[2][2])
    res = requests.get(url=url)
    assert res.status_code == data[2][6]
    assert res.json()["status"] == data[2][7]