# encoding: utf-8

import requests
from lxml import etree

import http.cookiejar as cookielib

class SchoolLogin():
    def __init__(self):
        self.loginUrl = 'http://xjw1.ncst.edu.cn'
        self.postUrl = 'http://xjw1.ncst.edu.cn/loginAction.do'
        self.infoUrl = 'http://xjw1.ncst.edu.cn/userInfo.jsp'
        self.validateUrl = 'http://xjw1.ncst.edu.cn/validateCodeAction.do'

        self.headers = {
            'Referer': 'http://xjw1.ncst.edu.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Host': 'xjw1.ncst.edu.cn'
        }

        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename='school_cookie')

    def post_account(self, zjh, mm):
        post_data = {
            'zjh1': '',
            'tips': '',
            'lx': '',
            'evalue': '',
            'eflag': '',
            'fs': '',
            'dzslh': '',
            'zjh': zjh,
            'mm': mm,
            'v_yzm': self.get_yzm()
        }
        response = self.session.post(self.postUrl, data=post_data, headers=self.headers)
        self.session.cookies.save()

    def load_cookie(self):
        try:
            self.session.cookies.load(ignore_discard=True)  # 从文件加载
        except:
            print('cookie 获取不成功')


    def get_yzm(self):
        response = self.session.get(self.validateUrl, headers=self.headers)
        f = open('valcode.jpeg', 'wb')
        f.write(response.content)
        f.close()
        code = input('请输入验证码:')
        return str(code)

    def isLogin(self):
        self.load_cookie()  # 携带cookie访问网页
        response = self.session.get(self.infoUrl, headers=self.headers)
        selector = etree.HTML(response.text)
        flag = selector.xpath('//td[@class="fieldName"]/text()')
        # 登陆成功返回来的个人设置信息
        print(u'个人设置Profile标题: %s' % flag)

if __name__ == "__main__":
    school = SchoolLogin()
    # 输入自己email账号和密码
    school.post_account(zjh='*******', mm='*******')
    # 验证是否登陆成功
    school.isLogin()