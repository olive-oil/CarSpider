import pandas as pd

df1 = pd.read_csv('../../data/amapTel.csv',index_col=3)
print(df1)

df1.fillna('null').round(4).to_csv# import json
# import re
# from math import ceil
#
# if __name__ == '__main__':
#     # path1 = '<strong class="red"><a class="cd60000" href="//www.che168.com/china/biaozhi/biaozhi307jinkou/a0_0msdgscncgpiltocsp1exs500/?pvareaid=103693">5.85万</a></strong>'
#     # path2 = '<strong class="red">暂无</strong>'
#     # type(path2)
#     # a = list()
#     # a.append(path2)
#     # pattern = re.compile(r'>([^<>]+?)<')
#     # for i in range(len(a)):
#     #     print(re.findall(pattern,a[i]))
#     # print(re.findall(pattern, path2))
#     #
# #     # path1.re(r'>([^<>]+?)<')
# #     # response = b'\r\n<!DOCTYPE html>\r\n\r\n<html>\r\n<head>\r\n    <meta charset="gb2312" />\r\n
#
#     # url = 'https://restapi.amap.com/v3/place/text?key=d0de733aaee4bda8f95c2b672d757024&city=500000&citylimit=true&types=010900|010901&children=1&page=0'
# #     # page_re = re.compile(r'.*page=(\d+).*')
# #     # print(page_re.match(url))
# #     # print(855/20 + 1)