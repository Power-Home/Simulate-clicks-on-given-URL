# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:32:07 2020

@author: PanHom
"""
import random
import requests
import time
from fake_useragent import UserAgent

def auto_click(urls,num):
        success = 0
        fail = 0
        
        referer_list=[
                'https://www.google.com/search?q=csdn&rlz=1C1EJFC_enSE810SE810&oq=csdn&aqs=chrome..69i57j69i59l2j0l5.2484j0j8&sourceid=chrome&ie=UTF-8',
                'http://blog.csdn.net/',
                'https://blog.csdn.net/weixin_41896265',
                'https://www.sogou.com/tx?query=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F&hdq=sogou-site-706608cfdbcc1886-0001&ekv=2&ie=utf8&cid=qb7.zhuye&',
                'https://www.baidu.com/s?wd=csdn&rsv_spt=1&rsv_iqid=0xa615ef5b0000b256&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=78040160_26_pg&ch=8&rsv_enter=1&rsv_dl=tb&rsv_sug2=0&inputT=1113&rsv_sug4=1528'
            ]
         
        while(num>0):
            #随机user_agent和Referer
            ua = UserAgent()
            for url in urls:
                headers = {
                            'User-Agent': ua.random,
                            'Referer':random.choice(referer_list)
                          }
                print("【正在访问】{}".format(url))
                try:
                    resp=requests.get(url,headers=headers)
                    time.sleep(1)
                    resp=requests.get(url,headers=headers)
                    time.sleep(1)
                    resp=requests.get(url,headers=headers)
                    time.sleep(1)
                    if resp.status_code == requests.codes.ok:
                        success+=1
                        print("【访问成功{}】".format(success))
                        time.sleep(1)
                except:
                #无响应则print出该代理ip
                    print ('【访问失败】')
                    fail+=1
                    time.sleep(5)
            num-=1
            time.sleep(60)
        print("-----------共访问{0}次，成功{1}次，失败{2}次--------------".format(success+fail,success,fail))

if __name__ == '__main__':
    num=10   # 运行次数,酌情修改
    urls=['https://blog.csdn.net/weixin_41896265/article/details/105393694','https://blog.csdn.net/weixin_41896265/article/details/105394115','https://blog.csdn.net/weixin_41896265/article/details/105371624']
    auto_click(urls,num)
  
    
  
    
  
    
  
    
