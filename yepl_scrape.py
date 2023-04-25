import requests
import random
from bs4 import BeautifulSoup
from lxml import html
import json
import html as h
import time

count=1
count1=1
restaurants_list=[]
headers = {
    'authority': 'www.yelp.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': 'hl=en_US; wdi=2|8A0A8784E46EC83C|0x1.90f968ab723ffp+30|cfff1bcac23e26b7; bse=d61636860a85435788534b83f49b8cb3; recentlocations=New+York%2C+NY%2C+United+States; xcj=1|a1kR_evWshmYNAsL8KUXvuVEdwhaReOkgks_Y7cL1lc; OptanonConsent=isGpcEnabled=1&datestamp=Tue+Apr+18+2023+15%3A14%3A55+GMT%2B0530+(India+Standard+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=c34eab08-0c3c-41bd-9dab-ce2dfab00709&interactionCount=1&landingPath=NotLandingPage&groups=BG51%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A0&AwaitingReconsent=false; location=%7B%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22latitude%22%3A+37.775123257209394%2C+%22display%22%3A+%22San+Francisco%2C+CA%22%2C+%22city%22%3A+%22San+Francisco%22%2C+%22parent_id%22%3A+371%2C+%22longitude%22%3A+-122.41931994395134%2C+%22min_longitude%22%3A+-122.51781463623047%2C+%22max_longitude%22%3A+-122.3550796508789%2C+%22zip%22%3A+%22%22%2C+%22accuracy%22%3A+4%2C+%22state%22%3A+%22CA%22%2C+%22country%22%3A+%22US%22%2C+%22unformatted%22%3A+%22San+Francisco%2C+CA%22%2C+%22max_latitude%22%3A+37.81602226140252%2C+%22address1%22%3A+%22%22%2C+%22county%22%3A+%22San+Francisco+County%22%2C+%22address2%22%3A+%22%22%2C+%22min_latitude%22%3A+37.706368356809776%2C+%22place_id%22%3A+%221237%22%2C+%22location_type%22%3A+%22locality%22%2C+%22address3%22%3A+%22%22%2C+%22borough%22%3A+%22%22%2C+%22isGoogleHood%22%3A+false%2C+%22language%22%3A+null%2C+%22neighborhood%22%3A+%22%22%2C+%22polygons%22%3A+null%2C+%22usingDefaultZip%22%3A+false%2C+%22confident%22%3A+null%7D',
    'referer': 'https://www.yelp.com/',
    'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}


def res_detauls(res_url,count,proxy_list):
    restaurants_dict={}
    review_list=[]
    proxy=proxy_list[0]
    try:
        response = requests.get(res_url,headers=headers,proxies= {"http":proxy, "https":proxy},timeout=15)
        tree=html.fromstring(response.text)
        time.sleep(10)
        name=tree.xpath('//h1[@class="css-1se8maq"]//text()')[0]
        add1=','.join(tree.xpath('//address//text()'))
        add2=','.join(tree.xpath('//p[@class=" css-gutk1c"]//text()'))
        address=add1+','+add2
        rating=tree.xpath('//div[@class=" five-stars__09f24__mBKym five-stars--large__09f24__Waiqf display--inline-block__09f24__fEDiJ  border-color--default__09f24__NPAKY"]//@aria-label')[0]

        
        #FOR ALL REVIEWS
        #===============
        # def all_review(res_url,count,proxy_list):
        #     proxy=proxy_list[0]
        #     try:
        #         params = {
        #             'rl': 'en',
        #             'q': '',
        #             'sort_by': 'relevance_desc',
        #             'start': '0',
        #         }
        #         response = requests.get(res_url+'/review_feed',headers=headers,proxies= {"http":proxy, "https":proxy},params=params,timeout=15)
        #         total_review_no=int(response.json().get('pagination').get('totalResults'))
        #         def review(res_url,count,proxy_list):
        #             proxy=proxy_list[0]
        #             try:
        #                 for start in range(0,total_review_no,10):
        #                     params = {
        #                     'rl': 'en',
        #                     'q': '',
        #                     'sort_by': 'relevance_desc',
        #                     'start': str(start),}
        #                     response = requests.get(res_url+'/review_feed',headers=headers,proxies= {"http":proxy, "https":proxy},params=params,timeout=15)
        #                     review_no=len(response.json().get('reviews'))
        #                     for xyz in range(review_no):
        #                         user_name=response.json().get('reviews')[xyz].get('user').get('markupDisplayName')
        #                         comment=response.json().get('reviews')[xyz].get('comment').get('text')
        #                         temp_dict={}
        #                         temp_dict[user_name]=h.unescape(comment.encode('ascii','ignore').decode('utf-8').replace('<br>',' ').replace('  ',' '))
        #                         review_list.append(temp_dict)
                            
        #                     time.sleep(60)
                            
        #                 restaurants_dict['Name']=name
        #                 restaurants_dict['address']=address
        #                 restaurants_dict['Rating']=rating
        #                 restaurants_dict['Reviews']=review_list
        #                 restaurants_list.append(restaurants_dict)
        #                 print(count)
        #                 with open('Yelp_data.json','w',encoding='utf-8') as f:
        #                     json.dump(restaurants_list,f,indent=2,ensure_ascii=False)
        #             except:
        #                 change()
        #                 print("Proxy changed")
        #                 review(res_url,count,proxy_list)
        #         review(res_url,count,proxy_list)
        #     except:
        #         change()
        #         print("Proxy changed")
        #         all_review(res_url,count,proxy_list)
        # all_review(res_url,count,proxy_list)
        

        
        
        # FOR FIRST 10 REVIEWS
        # ====================
        def review(res_url,count,proxy_list):
            proxy=proxy_list[0]
            try:
                for start in range(0,5,10):
                    params = {
                    'rl': 'en',
                    'q': '',
                    'sort_by': 'relevance_desc',
                    'start': str(start),}
                    response = requests.get(res_url+'/review_feed',headers=headers,proxies= {"http":proxy, "https":proxy},params=params,timeout=15)
                    review_no=len(response.json().get('reviews'))
                    for xyz in range(review_no):
                        user_name=response.json().get('reviews')[xyz].get('user').get('markupDisplayName')
                        comment=response.json().get('reviews')[xyz].get('comment').get('text')
                        temp_dict={}
                        temp_dict[user_name]=h.unescape(comment.encode('ascii','ignore').decode('utf-8').replace('<br>',' ').replace('  ',' '))
                        review_list.append(temp_dict)
                    
                    time.sleep(60)
                    
                restaurants_dict['Name']=name
                restaurants_dict['address']=address
                restaurants_dict['Rating']=rating
                restaurants_dict['Reviews']=review_list
                restaurants_list.append(restaurants_dict)
                print("Page no."+str(count1-1)+" - Result no."+str(count))
                with open('Yelp_data.json','w',encoding='utf-8') as f:
                    json.dump(restaurants_list,f,indent=2,ensure_ascii=False)
            except:
                change()
                print("Proxy changed")
                review(res_url,count,proxy_list)
        review(res_url,count,proxy_list)
    except:
        change()
        print("Proxy changed")
        res_detauls(res_url,count,proxy_list)



def linkz(page_url,count,proxy_list):
    proxy=proxy_list[0]
    try:
        response_1 = requests.get(page_url, proxies={"http":proxy, "https":proxy}, headers=headers,timeout=15)
        tree=html.fromstring(response_1.text)
        link_list=tree.xpath('//ul[@class=" undefined list__09f24__ynIEd"]//div[@class="  border-color--default__09f24__NPAKY"]//span[@class=" css-1egxyvc"]//a/@href')
        for zzz in range(2,12):
            link_ind=('https://www.yelp.com'+link_list[zzz]).index('?')
            res_url=('https://www.yelp.com'+link_list[zzz])[:link_ind]
            res_detauls(res_url,count,proxy_list)
            count+=1
    except:
        change()
        print("Proxy changed")
        linkz(page_url,count,proxy_list)




proxy_list=[
  "5.78.79.142:8080",
  "78.47.128.252:8080",
  "5.78.73.198:8080",
  "209.38.252.253:8080",
  "95.216.170.84:8080",
  "5.78.74.109:8080",
  "209.38.252.248:8080",
  "95.217.15.62:8080",
  "91.107.214.73:8080",
  "5.78.46.153:8080",
  "5.78.88.80:8080",
  "40.117.59.214:3128",
  "91.107.235.240:8080",
  "91.107.211.49:8080",
  "37.27.4.32:8080",
  "148.251.123.98:7777",
  "154.70.107.81:3128",
  "74.249.8.183:3128",
  "164.92.242.220:3128",
  "91.107.207.116:8080",
  "62.210.209.223:3128",
  "116.203.65.154:8080"
]


def change():
    first=proxy_list.pop(0)
    proxy_list.append(first)
for kkk in range(0,231,10):
    page_url='https://www.yelp.com/search?find_desc=Restaurants&find_loc=San%20Francisco%2C%20CA&start='+str(kkk)
    print('\n')
    print("Page no."+str(count1))
    print('\n')
    count1+=1
    linkz(page_url,count,proxy_list)