# 导入pymysql
import os, sys
sys.path.append(os.getcwd())

import pymysql


# 封装查询方法
def query(sql):
    # 1.连接mysql数据库
    db = pymysql.connect(host="118.24.105.78", user="root", password="1qaz!QAZ123***123", db="ljtestdb")
    # 2.获取对应的查询窗口：游标
    cur = db.cursor()
    # 3.执行查询sql语句
    cur.execute(sql)
    # 4.获取所有的结果
    res = cur.fetchall()
    # 5.关闭数据库连接
    db.close()
    return res

if __name__ == "__main__":
    sql = "select * from t_user where id=248"
    r = query(sql)
    print(r)