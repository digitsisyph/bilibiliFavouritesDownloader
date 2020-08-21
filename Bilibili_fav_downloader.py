import re
import sys
import urllib.request
from subprocess import call

import requests
from bs4 import BeautifulSoup

from config import Config


class Bili_fav:

    video_urls = []
    video_titles = []

    # get url address 获取收藏夹地址
    def __init__(self, user_id, favorites_id):
        self.favurl = f"https://rsshub.app/bilibili/fav/{user_id}/{favorites_id}"

    # load videos addresses 读取视频地址
    def load_favorites(self):
        r = requests.get(self.favurl)
        print(r.status_code)
        soup = BeautifulSoup(r.text, 'xml')
        for item in soup.find_all('item'):
            self.video_titles.append(item.title.text)
            self.video_urls.append(item.link.text)

    # report spider results 显示爬虫结果
    def report(self):
        print("已搜索到%s部视频：" % len(self.video_urls))
        i = 1
        for title in self.video_titles:
            print("%s." % i + title)
            i += 1

    # 下载视频
    def download_videos(self, output_dir=''):
        i = 1
        if output_dir == '':
            for video_url in self.video_urls:
                print("第%s/%s部视频下载中：（使用 ctrl+c 暂停下载）" %
                      (i, len(self.video_urls)))
                call(
                    f"you-get --playlist {video_url}", shell=True)
                i += 1
        else:
            for video_url in self.video_urls:
                print("第%s/%s部视频下载中：（使用 ctrl+c 暂停下载）" %
                      (i, len(self.video_urls)))
                call(
                    f"you-get --playlist -o {output_dir} {video_url}", shell=True)
                i += 1


if __name__ == '__main__':

    user_id = Config.USER_ID
    favorites_id = Config.FAV_ID
    output_dir = Config.OUTPUT_DIR
    my_fav = Bili_fav(user_id, favorites_id)
    my_fav.load_favorites()
    my_fav.report()
    my_fav.download_videos(output_dir)
