# Bilibili 收藏夹下载器

基于 you-get 实现一键下载Bilibili指定收藏夹下的视频。

## 环境要求

- `Python3` 与 `urllib` 库
- 基于 python 开发的视频下载器 `you-get` （ https://github.com/soimort/you-get ）

如果已经安装有 `python 3`，可直接通过命令行安装 `you-get`。

```
pip3 install you-get
```

## 使用方法

打开 Bilibili_fav_downloader.py ，编辑用户id，收藏夹id与下载目录，之后直接运行即可。

### 如何查看用户id与收藏夹id

进入任意一个B站收藏夹，如 https://space.bilibili.com/32708543/favlist?fid=2935220 。

其地址中，`32708543` 这一部分即为用户id，`2935220` 则为收藏夹id。

### 注意事项

1. `you-get` 会自动下载收藏夹内每个视频的所有分P。
2. 如果下载文件夹中已经存在下载好的视频文件，`you-get` 会自动跳过。
3. B站收藏夹必须被设置成公共，私有收藏夹无法下载。
