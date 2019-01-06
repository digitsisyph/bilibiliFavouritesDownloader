import urllib.request
import re
import sys
from subprocess import call


class Bili_fav:

    video_ids = []
    video_titles = []

    # get url address 获取收藏夹地址
    def __init__(self, user_id, favorites_id):
        self.favurl ="https://api.bilibili.com/x/space/fav/arc?vmid={}&fid={}".format(user_id, favorites_id)

    # load videos addresses 读取视频地址
    def load_favorites(self):
        page = 1
        while True:
            response = urllib.request.urlopen(self.favurl+"&pn={}".format(page))
            content = response.read().decode('utf-8')
            id_results = re.findall('"aid":(\d+),', content)
            title_results = re.findall('"highlight_title":"(.*?)"', content)

            if not id_results: 
                break
            else:
                page += 1
            
            # store titles and videos ids
            self.video_titles += title_results
            for video_id in id_results:
                if video_id not in self.video_ids:
                    self.video_ids.append(video_id)

    # report spider results 显示爬虫结果
    def report(self):
        print("已搜索到%s部视频：" % len(self.video_ids))
        i = 1
        for title in self.video_titles:
            print("%s."%i + title)
            i += 1
    
    # 下载视频
    def download_videos(self, output_dir = ''):
        i = 1
        if output_dir == '':
            for video_id in self.video_ids:
                print("第%s/%s部视频下载中：（使用 ctrl+c 暂停下载）" % (i, len(self.video_ids)))
                call("you-get --playlist https://www.bilibili.com/video/av{}".format(video_id), shell=True)
                i += 1
        else: 
            for video_id in self.video_ids:
                print("第%s/%s部视频下载中：（使用 ctrl+c 暂停下载）" % (i, len(self.video_ids)))
                call("you-get --playlist -o {} https://www.bilibili.com/video/av{}".format(output_dir, video_id), shell=True)
                i += 1


if __name__ == '__main__':

    # 请输入用户id和收藏夹id
    user_id = 111111
    favorites_id = 11111
    # 请输入下载目录
    output_dir = "/Usr/...."

    my_fav = Bili_fav(user_id, favorites_id)
    my_fav.load_favorites()
    my_fav.report()
    my_fav.download_videos(output_dir)  