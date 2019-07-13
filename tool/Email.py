import yagmail,os
from datetime import date

# email参数
email_account='340214909@qq.com'
email_pwd ='atwesnlgaedybigf'
email_host ='smtp.qq.com'
email_port='465'
email_to_account='hello18820855535@163.com'
email_to_account_list =['hello18820855535@163.com','340214914@qq.com','18820855535@139.com']
email_time=date.today()
#附件路径
reportPath='../file_generalList/TestReports'
# 获取最新报告
def get_new_report():
    l=os.listdir(reportPath)
    l.sort(key=lambda fn :os.path.getmtime(reportPath + '\\' + fn))
    f = os.path.join(reportPath,l[-1])
    return f

#发送Email
def sendEmail(s_user,s_pwd,host,port,to_user,body,subject,report_flie):

    send =yagmail.SMTP(user=s_user,password=s_pwd,host=host,port=port)
    if type(to_user) is list:
        send.send(to=to_user,cc=s_user,subject=subject,contents=[body,report_flie])
        flag = True

    elif type(to_user) is not list:
        send.send(to=to_user,subject=subject, contents=[body, report_flie])
        flag = True
    else:
        flag = False
    return flag


if __name__=='__main__':
    report = get_new_report()
    # time1=date.today()
    # sendEmail(s_user=email_account, s_pwd=email_pwd, port=email_port, host=email_host, report_flie=report,
    #           to_user=email_to_account_list, subject='EDU自动化测试报告', body='各位领导，今天{}的报告已生成，请查阅'.format(time1))
    #
    # print('邮件已发送')
