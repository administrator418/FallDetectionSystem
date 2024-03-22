# python3
# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户https://user.ihuyi.com/new/register.html
# 注意事项：
# （1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
# （2）请使用 用户名 及 APIkey来调用接口，APIkey在会员中心可以获取；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

import urllib.parse
import urllib.request

# 接口地址
url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"

# 定义请求的数据
values = {
    "account": "C67266089",
    "password": "fab6091b9dd4cae53d603d3a9ae3883e",
    "mobile": "15892032103",
    "content": "您的验证码是：7835。请不要把验证码泄露给其他人。",
    "format": "json",
}

# 将数据进行编码
data = urllib.parse.urlencode(values).encode(encoding="UTF8")

# 发起请求
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
res = response.read()

# 打印结果
print(res.decode("utf8"))
