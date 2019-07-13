import pymysql

def edu_pyMySql(sql,host='localhost',port=3306,user='edu',password='edu',db='edu'):
    # 连接数据库
    conn=pymysql.connect(host=host,port=port,user=user,password=password,db=db)
    # 获取游标
    cuer=conn.cursor()
    # 执行SQL语句
    cuer.execute(sql)
    # 获得域的名字
    r =cuer.description
    # cuer.fetchall()是获取返回值
    var=cuer.fetchall()
    if var !=():
        for values in var:
            # print(values)
            sqlData={}
            for i in range(len(r)):
                sqlData[r[i][0]]=values[i]
    elif var ==():
        sqlData ='你可能在删除、更新、新增操作，也可能查询的数据不存在'
    # 关闭游标
    cuer.close()
    # 关闭数据库连接
    conn.close()
    return sqlData

# print(edu_pyMySql('select password,username,email from xsmart_users where username="13900000003";'))
# print(edu_pyMySql('delete  from  xsmart_users where username="13900000003";'))
# print(edu_pyMySql('update xsmart_users set realname="huang" where username="13700003225";'))
# print(edu_pyMySql("insert into xsmart_users (`id`, `logo`, `classid`, `email`, `username`, `type`, `realname`, `password`, `question`, `answer`, `sex`, `birthday`, `user_money`, `frozen_money`, `pay_points`, `rank_points`, `address_id`, `addtime`, `last_login`, `last_time`, `last_ip`, `visit_count`, `user_rank`, `is_special`, `ec_salt`, `salt`, `parent_id`, `flag`, `alias`, `msn`, `qq`, `office_phone`, `home_phone`, `phone`, `province`, `city`, `address`, `age`, `is_validated`, `credit_line`, `passwd_question`, `passwd_answer`, `balance`, `company_id`, `client_user`, `profession`, `district`, `year_count`, `month_count`, `down_count`, `order_time`, `expire_time`, `month_price`, `year_price`, `client_price`, `year_month`, `last_buy`, `hobby`, `job`, `location_p`, `location_c`, `location_a`, `head_img`, `birth_year`, `birth_month`, `birth_day`, `audit`, `openid_type`, `openid`, `is_edm`, `points`, `qiandaodate`, `adds`, `uptime`, `introduce`, `roleid`, `rolename`, `orid`, `orgname`, `m`, `isstart`, `startname`, `studytime`, `studynum`, `real_img`, `ponits`, `QopenId`, `WopenId`) values('99993','22','0','hell@40163.com','13900000003','1','hgao1','1234567','','','1','0000-00-00','0.00','0.00','0','0','0','1559224324','0','0000-00-00 00:00:00','','0','0','0',NULL,'0','0','0','','','','','','13777777777','0','0','%E5%BE%88%E5%AF%B9%E5%95%8A','0','0','0.00',NULL,NULL,'0.00','0','','','','0','0','0','0','0','0.00',NULL,NULL,'0.00','0',NULL,NULL,'%E5%8C%97%E4%BA%AC%E5%B8%82','%E5%B8%82%E8%BE%96%E5%8C%BA','%E4%B8%9C%E5%9F%8E%E5%8C%BA',NULL,NULL,NULL,NULL,'1',NULL,NULL,'0',NULL,NULL,NULL,NULL,'北京市区','8',NULL,'110',NULL,NULL,'0',NULL,NULL,'',NULL,NULL,NULL,NULL);"))