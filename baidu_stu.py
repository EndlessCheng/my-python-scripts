# -*- coding: utf-8 -*-
from PIL import Image
import urllib
import urllib2
import re
import json
import ssl

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36"


def baidu_stu_lookup(im):
    url = "http://stu.baidu.com/n/image?fr=html5&needRawImageUrl=true&id=WU_FILE_0&name=233.png&type=image%2Fpng&lastModifiedDate=Mon+Mar+16+2015+20%3A49%3A11+GMT%2B0800+(CST)&size="    
    im.save("./query_temp_img.png")
    raw = open("./query_temp_img.png", 'rb').read()
    url += str(len(raw))
    req = urllib2.Request(url, raw, {'Content-Type': 'image/png', 'User-Agent': UA})
    resp = urllib2.urlopen(req)

    resp_url = resp.read()  # return a pure url

    url = "http://stu.baidu.com/n/searchpc?queryImageUrl=" + urllib.quote(resp_url)

    req = urllib2.Request(url, headers={'User-Agent': UA})
    resp = urllib2.urlopen(req)

    html = resp.read()

    return baidu_stu_html_extract(html)


def baidu_stu_html_extract(html):
    pattern = re.compile(r"keywords:'(.*?)'")
    matches = pattern.findall(html)
    if not matches:
    return '[UNKNOWN]'
    json_str = matches[0].replace('\\x22', '"').replace('\\\\', '\\')
    result = [item['keyword'] for item in json.loads(json_str)]
    return '|'.join(result) if result else '[UNKNOWN]'


if __name__ == '__main__':
    im = Image.open('1.jpg')
    result = baidu_stu_lookup(im)
    print result
