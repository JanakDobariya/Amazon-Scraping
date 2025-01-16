import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = 'https://www.amazon.in/s?k=mobiles&crid=1SEDW4KDKBZ9Y&sprefix=mobiles%2Caps%2C226&ref=nb_sb_noss_1'

cookies = {
    'session-id': '257-9365134-4691452',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'INR',
    'ubid-acbin': '262-0891467-4109855',
    'session-token': '"KIi1G5lmisC9DzDufGcma3CkFGzK47P6ej/5eEyplRvWBk+UBkLlBizqHIuQg9Zpd2eudY326zOSJtUP+6/uJMwQjKY3ubX+3+GXNTuZa2o+K8qoy0iWJyyusAcrFCKYpp8mCS3ksslfb2QXE+ZpVjwzD5WSg52I8sZULX9tQlWNK0tXKiyUGsIf48LGrIBH8AAwoU5cbS4spzSoE+8lwKs/E+feeO6HqleATJIW+DE="',
}

headers = {
    'authority': 'fls-eu.amazon.in',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'session-id=257-9365134-4691452; session-id-time=2082787201l; i18n-prefs=INR; ubid-acbin=262-0891467-4109855; session-token="KIi1G5lmisC9DzDufGcma3CkFGzK47P6ej/5eEyplRvWBk+UBkLlBizqHIuQg9Zpd2eudY326zOSJtUP+6/uJMwQjKY3ubX+3+GXNTuZa2o+K8qoy0iWJyyusAcrFCKYpp8mCS3ksslfb2QXE+ZpVjwzD5WSg52I8sZULX9tQlWNK0tXKiyUGsIf48LGrIBH8AAwoU5cbS4spzSoE+8lwKs/E+feeO6HqleATJIW+DE="',
    'referer': 'https://www.amazon.in/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

response = requests.get(url,cookies=cookies,headers=headers)

# response = requests.get(url,headers=headers)
a1 = []
b1 = []

print(response.status_code)

for k in range (1,21):
    print(k)
    url = f'https://www.amazon.in/s?k=mobiles&page={k}&qid=1685622711&sprefix=%2Caps%2C197&ref=sr_pg_{k}'
    print(url)
    response = requests.get(url,cookies=cookies,headers=headers)
    
    sp = bs(response.text,'html.parser')
    pr = sp.find_all("div", attrs={"class":"sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right"})


    for i in pr:
        a = i.find("span", attrs={"class":"a-size-medium a-color-base a-text-normal"}).text
        
        

        b = i.find("span", attrs={"class":"a-price-whole"})
        
        print(a)
        print(b)

        a1.append(a)

        if b == None:
            f = ' '
            b1.append(f)
        else:
            b1.append(b.text)

        print('\n')
    #/s?k=mobiles&qid=1685622476&sprefix=%2Caps%2C197&ref=sr_pg_1


print(len(a1))
print(len(b1))

df = pd.DataFrame({"Product Name":a1,"Product Price":b1})

print(df)

df.to_csv("amazone.csv")

