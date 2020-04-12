# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:32:07 2020

@author: PanHom

"""

import random
import requests
import time
from fake_useragent import UserAgent

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            ip = response.text
            #设置代理,格式如下
            proxy_ip = "http://" + ip
            proxy_ips = "https://" + ip
            proxy = {"https":proxy_ips,"http":proxy_ip} 
            return proxy
    except ConnectionError:
        return None
    
def get_cookie(url,urls):
    if(url==urls[0]):
        f=open(r'cookie0.txt','r')#打开所保存的cookies内容文件
    if(url==urls[1]):
        f=open(r'cookie1.txt','r')#打开所保存的cookies内容文件
    if(url==urls[2]):
        f=open(r'cookie2.txt','r')#打开所保存的cookies内容文件
    cookies={}#初始化cookies字典变量
    for line in f.read().split(';'):   #按照字符：进行划分读取
        #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value  #为字典cookies添加内容
    return cookies


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
            headers = {
                'user-agent': ua.random,
                'Referer': random.choice(referer_list),
            }
            proxies = get_proxy()
            for url in urls:
                cookies = get_cookie(url,urls)
                print("【正在访问】{}".format(url))
                try:
                    session = requests.session()
                    resp=session.get(url,headers=headers,proxies=proxies,cookies=cookies,timeout=3) 
                    if resp.status_code == requests.codes.ok:
                        print("---------------------------\n")
                        print(resp.text[10000:30000])
                        print("---------------------------\n")
                        success+=1
                        print("【访问成功{}】".format(success)+proxies["https"])
                        time.sleep(40)
                except Exception as e:
                #无响应则print出该代理ip
                    fail+=1
                    print ('【访问失败{}/】'.format(fail)+proxies["https"])
                    print("访问异常--->"+str(e)+"\n")
                    proxies = get_proxy()
                    time.sleep(0.5)
            num-=1
        print("-----------共访问{0}次，成功{1}次，失败{2}次--------------".format(success+fail,success,fail))

if __name__ == '__main__':
    num=100   # 运行次数,酌情修改
    urls=['https://blog.csdn.net/weixin_41896265/article/details/105393694','https://blog.csdn.net/weixin_41896265/article/details/105394115','https://blog.csdn.net/weixin_41896265/article/details/105371624']
    auto_click(urls,num)
  
    
  
    
  
    
  
    
  
''' 
proxy_list=[]
def get_proxy_list():
    global proxy_list
    print ("导入proxy_list...")
    #ip文件可以浏览我上文链接文章“多线程爬虫——抓取代理ip”
    f=open("ip.txt")
    #从文件中读取的line会有回车，要把\n去掉
    line=f.readline().strip('\n')
    while line:
        proxy_list.append(line)
        line=f.readline().strip('\n')
    f.close()
    print(proxy_list)
    
    if resp.status_code == requests.codes.ok:
        html = etree.HTML(resp.text)
        article_links=html.xpath('//div[@class="article-item-box csdn-tracking-statistics"]/h4/a/@href')
        # 访问每一篇文章，模拟点击
        for article_link in article_links:
            requests.get(article_link,headers=header, proxies=proxy)
            print('正在第 [{0}] 次点击 {1}'.format(num,article_link))
    times+=1
    time.sleep(2)
    #每当所有的代理ip刷过一轮，延时15秒
    if not times%len(proxy_list):
        time.sleep(15)
        
'''