import requests 
import re 
import json 
from lxml import html

#example function usage


r = requests.get('https://th.wikipedia.org/wiki/ดวงจันทร์',
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})
print(r)
text = ""
name1=""
tree = html.fromstring(html=r.text)

print(tree)
for i in range(1,5):
    name0 = tree.xpath("//div[@id='mw-content-text']/div[1]")[0] 
    name1 = tree.xpath(f"//div[@id='mw-content-text']/div[1]/p[{i}]/text()") 
    name2 = tree.xpath(f"//div[@id='mw-content-text']/div[1]/p[{i}]/a/text()")
   
    
    

    count = len(name2)
    for j in range(count):
        text = text+name1[j]+name2[j]
        # if name1[j+1] == name1[-1]:
        #     text = text + name1[j+1]

bo = name0.xpath(f"./p[1]")[0]
bo = bo.xpath("./b/text()")[0]
text= ''.join(text)
text = text.replace('"','')
text = bo + text
print(text.strip())






# text = ""
# for i in range(len(name0)):
#     text = text+str(name0.text[i])+str(name0.xpath("a/text()")[i])
# print(text)

# url ="https://www.ebay.com/itm/324823435665?_trkparms=pageci%3A564d6dd9-619c-11ec-8445-eadc6850af56%7Cparentrq%3Ad81f333a17d0a77d31def7acfff5db24%7Ciid%3A1"
# info = tree.xpath("//*[@id='prcIsum']/text()")[0]
# searches = tree.xpath("//*[@id='vi_notification_new']/span/text()")[0]




# ebay = {
#     'name': name,
#     'url': url,
#     'info': info,
#     'searches': searches
# }

# def write_to_json(filename, data):
#     f = open(filename , 'w')
#     f.write(json.dumps(data))
#     f.close()

# write_to_json('ebay.json',ebay)