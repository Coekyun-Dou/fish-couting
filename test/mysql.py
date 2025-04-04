import pymysql


def getTableData(username, password):
    conn = pymysql.connect(
        host='127.0.0.1',  # 连接主机, 默认127.0.0.1
        user='root',  # 用户名
        passwd='123456',  # 密码
        port=3306,  # 端口，默认为3306
        db='hsfdSystem',  # 数据库名称
        charset='utf8'  # 字符编码
    )
    # 生成游标对象 cursor
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM `hsfdsystem`.`usertable` WHERE `user`='{username}'")
    data = cursor.fetchone()

    if data is None:
        print('该用户不存在')
    else:
        if data[1] == password:
            print('登录成功！')
        else:
            print('密码错误！')
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接


if __name__ == "__main__":
    data1 = getTableData();
    print(data1)
