import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from requests_ntlm import HttpNtlmAuth
import datetime
import smtplib
import pymongo
import pandas as pd
from openpyxl.workbook import Workbook
import json

date = datetime.date.today().strftime("%d.%m.%Y")


def parse_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # db = myclient.test
    parse_db = myclient.parse_db
    parse_data = parse_db.parse_data


def send_mail(date):
    sender = 'finger@qwe.com'
    receivers = ['qwe.qwe@qwe.az']
    message = """From: Finger Scan <Finger@sgofc.com>
	To: To Person <ibrahim.babashov@intersun.az>
	Subject: Finger Scan

	Dear
	You forget scan your finger!!!
	{}
	""".format(date)

    try:
        smtpObj = smtplib.SMTP('smtp.qwe.com')
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
    except SMTPException:
        print("Error: unable to send email")


def sharepointlogin():
    # lst=[]
    # dic=[]
    url = 'http://qwe'
    username, password = 'qwe\\qwe.qwe', 'qwe'
    response = requests.get(url, auth=HttpNtlmAuth(username, password))
    # soup = BeautifulSoup(response.text, 'lxml')
    # all_data = soup.find_all("tr")
    # data = all_data[-1].find_all("td")
    dfs = pd.read_html(response.text, index_col=0)
    js = dfs[-1].to_json(orient='index')
    dic = json.loads(js)
    for v in dic.values():
        if v['TARIX'] == date:
            if v['GIRIS'] != None:  # and v['CIXIS'] == None:
                # if date in v['GIRIS']:
                print('GIRIS:', v['GIRIS'])
                send_mail(date)
            elif v['GIRIS'] == None:
                send_mail(date)
            elif v['CIXIS'] == None:
                send_mail(date)

    # for tds in data:
    # s = tds.get_text()
    # lst.append(s)
    # dic = {'name':lst[2],'entry_time':lst[7],'exit_time':lst[8]}
    # print(dic)


def main():
    sharepointlogin()
    # parse_db()


main()
