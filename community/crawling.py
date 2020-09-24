import requests
import xmltodict
from urllib2 import Request, urlopen
def Parsing():
    url='http://www.chungbuk.go.kr/openapi-data/service/priceinfo/priceinfo'
    request = Request(url)
    response = urlopen(request)
    rescode = response.getcode()
    if rescode==200:
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code : "+rescode)

Parsing()