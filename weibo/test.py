# import re
#
# with open(r'weibo/templates/weibo/pic.html', 'r') as file:
#     data = file.read()
# data = data.replace('\n', '')
# data = re.findall('<body>(.*?)</body>', data)[0]
# with open(r'weibo/templates/weibo/pic.txt', 'w+') as file:
#     file.write(data)
import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
print(PROJECT_ROOT + "\\weibo\\templates\\weibo\\css\\style.css")
with open(PROJECT_ROOT + "\\weibo\\templates\\weibo\\css\\style.css", 'r', encoding='utf-8') as file:
    print(file.read())
