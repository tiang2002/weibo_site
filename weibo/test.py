import re

with open(r'weibo/templates/weibo/pic.html', 'r') as file:
    data = file.read()
data = data.replace('\n', '')
data = re.findall('<body>(.*?)</body>', data)[0]
with open(r'weibo/templates/weibo/pic.txt', 'w+') as file:
    file.write(data)
