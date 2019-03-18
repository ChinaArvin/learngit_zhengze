# -*- coding:utf-8 -*-
import re

# string =  "xxxxxxxxxxxxxxxxaaaxxxxxx entry '某某内容' for ddddddd"
#
#
# result =  re.findall(".*aaa(.*).*",string)
#
# for x in result:
#
#     print x

a="ABCDEFGHIJABCDEFGHIJABCDEF/GHIJ"
b="/"
print(u"在a中查找最后一个b后面的字符:"+a[a.rfind(b)+1:])
print (a[a.rfind(b)+1:])
print "aaa"
print "branch1"