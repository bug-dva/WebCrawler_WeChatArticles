# -*- coding: utf-8 -*-
from api.fetch import SogouAPI

from Queue import Queue
from threading import Thread

import json


class CrawlerThread(Thread):

    def __init__(self, queue):
        self.queue = queue
        self.sogou_api = SogouAPI()
        Thread.__init__(self)

    def run(self):
        while True:
            info = self.queue.get()
            if 'profile' in info['url']:
                articles = self.sogou_api.fetch_history_urls_from_profile(info['url'])
                f = open(u'content/%s' % info['title'], 'a')
                f.write(json.dumps(articles).encode('utf-8'))
                f.close()

                for article in articles:
                    self.queue.put({'url': article['content_url'],
                                   'title': article['title']})
            else:
                article = self.sogou_api.fetch(info['url'])
                f = open(u'content/%s.html' % info['title'], 'w')
                f.write(article.encode('utf-8'))
                f.close()
            self.queue.task_done()


class Crawler:

    def __init__(self, thread_num):
        self.queue = Queue()
        self.thread_pools = []
        self.sogou_api = SogouAPI()

        for i in range(thread_num):
            self.thread_pools.append(CrawlerThread(self.queue))
            self.thread_pools[i].setDaemon(True)
            self.thread_pools[i].start()

    def start(self):
        print 'Start to processing...'
        gzh_info = self.sogou_api.fetch_gzh_info(keyword='九章算法')
        for info in gzh_info:
            self.queue.put({'url': info['profile_url'],
                            'title': info['wechat_id']})
        self.queue.join()
        print 'Finish!'
