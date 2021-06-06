# import requests
# from bs4 import BeautifulSoup
# import csv
# from time import sleep
# from random import randint
#
# file = open('mymarket.csv', 'w', newline='\n', encoding="utf-8")
# file_obj =csv.writer(file)
# file_obj.writerow(['Title', 'Address', 'Website'])
# p={'SetTypeID':2, 'Page':1}

#
# url= 'https://www.mymarket.ge/ka/shops/'
#
# while p['Page']<=5:
#     r=requests.get(url, headers={'user-agent':'Chrome\90.0.4430.212'},  params=p)
#     # print(r)
#
#
#     content = r.text
#     # print(content)
#
#
#     soup= BeautifulSoup (content, 'html.parser')
#     whole=soup.find('ul', class_='shops-list')
#     all_shops=whole.find_all('li', class_='clear-after')
#
#     for each in all_shops:
#         title=each.h3.text
#         address=each.find('p', class_='b-16').text
#         website=each.find('a', class_='b-16 hover').text
#         print(title)
#         file_obj.writerow([title, address, website])
#
#     p['Page']+=1
#     sleep(randint(12,20))
#
#
# file.close()
#





