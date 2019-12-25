#!/usr/bin/python
from scrapy import cmdline
from scrapy.cmdline import execute
# cmdline.execute("scrapy crawl amapPhone".split())
# # cmdline.execute("scrapy crawl brandAuto".split())
cmdline.execute("scrapy crawl carPrice".split())


