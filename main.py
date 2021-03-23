import requests
import pandas as pd
from lxml import html
from bs4 import BeautifulSoup
from urllib.parse import urlencode, quote_plus, unquote

URL = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade"
KEY = unquote("dqIMi/vYl2mR6ytgRoKFVb/4gs9WEVKyM+o6DDefNlImlXslZWwEYrVAxA/NaE/fMCc2/rSubecCbobfpX0ERA==")

print("지역코드를 입력하세요(법정동코드 앞 5자리)")
lawd_cd = input()
print("실거래연월을 입력하세요 (ex) 202101")
deal_ymd = input()

queryParams = '?' + urlencode(
  {
    quote_plus('ServiceKey') : KEY,
    quote_plus('LAWD_CD') : lawd_cd,
    quote_plus('DEAL_YMD') : deal_ymd
  }
)

response = requests.get(URL + queryParams).text.encode('utf-8')
soup = BeautifulSoup(response,'lxml-xml')

row = soup.findAll('item')

apt_list = []
apt_info_list = []
attributes = []

row_len = len(row)
for i in range(0,row_len):
  apt_info = row[i].findAll()

  col_len = len(apt_info)
  for j in range(0,col_len):
    if i == 0:
      attributes.append(apt_info[j].name)
    apt_info_text = apt_info[j].text
    apt_info_list.append(apt_info_text)
  apt_list.append(apt_info_list)
  apt_info_list = []



if __name__ == '__main__':
  result = pd.DataFrame(apt_list, columns=attributes)
  result.head()
  print(result)