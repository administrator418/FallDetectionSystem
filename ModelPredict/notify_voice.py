# 接口类型：互亿无线语音通知接口。
# 账户注册：请通过该地址开通账户https://user.ihuyi.com/new/register.html
# 注意事项：
# （1）调试期间，请仔细阅读接口文档；
# （2）请使用APIID（查看APIID请登录用户中心->语音通知->帐户及签名设置->APIID）及 APIkey来调用接口
# （3）该代码仅供接入互亿无线语音通知接口参考使用，客户可根据实际需要自行编写；

#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
import urllib.parse

host = "api.vm.ihuyi.com"
sms_send_uri = "/webservice/voice.php?method=Submit"

# //用户名是登录用户中心->语音通知->帐户及签名设置->APIID
account = "VM14938824"
# 密码 查看密码请登录用户中心->语音通知->帐户及签名设置->APIKEY
password = "adae8b8e1c1c7f7d9232e5d58d462bb0"


def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {
            "account": account,
            "password": password,
            "content": text,
            "mobile": mobile,
            "format": "json",
        }
    )
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain",
    }
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == "__main__":

    mobile = "15892032103"
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))
