from scrapy.cmdline import execute
import sys
sys.argv = ['scrapy', 'crawl', 'ngo_posts']
execute()
