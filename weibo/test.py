# import re
#
# with open(r'weibo/templates/weibo/pic.html', 'r') as file:
#     data = file.read()
# data = data.replace('\n', '')
# data = re.findall('<body>(.*?)</body>', data)[0]
# with open(r'weibo/templates/weibo/pic.txt', 'w+') as file:
#     file.write(data)
import os, csv, re
import time

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
points = []
with open(PROJECT_ROOT + r'/weibo/timeline.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    for each in reader:
        temp = []
        words = re.findall('[:]{}:(.*?)', each[0])
        if words:
            points.append(words[0])

print(points)
