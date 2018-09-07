# coding=utf-8
# 2018.04.13

import requests
import re
from url_para import para
from configuration_file import config_data


def login_sp_api():
    session = requests.session()
    # step1
    url1 = config_data['host'] + 'login?service=' + config_data['spServer']
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': url1,
        'Connection': 'keep-alive'
    }
    content1 = session.get(url1, headers=headers, verify=False)
    pattern1 = re.compile('.*?<input type="hidden" name="lt" value="(.*?)".*?')
    match1 = re.findall(pattern1, content1.text)
    ticket = match1[0]

    # step2
    url2 = config_data['host'] + '/login?'
    cookies1 = content1.cookies.values()
    data = {
        'username': 'admin',
        'password': '123321qwe',
        'lt': ticket,
        'execution': 'e1s1',
        '_eventId': 'submit',
        'submit': 'LOGIN'
    }
    url_para = para(data) + '&isCaptchaCode=0'
    content2 = session.post(
        url2 + url_para,
        headers=headers,
        cookies={'JSESSIONID': cookies1[0]},
        verify=False,
        allow_redirects=False
    )
    location = content2.headers['location']
    session.get(location)
    userInfo = session.get(config_data['spServer'] + '/userInfo')

    return session


if __name__ == "__main__":
    login_sp_api()
