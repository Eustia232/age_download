import os


from bs4 import BeautifulSoup


from response import get_response
from download import download_video
from cloud_url import get_cloud_url
from tt_download import get_tt_download_url
from usl_download import get_usl_download_url

id = '20210114'

#
def get_info(response):

    """

    :param response: 视频信息页

    :return:list类型，存储视频单独一话的信息
    元素eg：<a class="video_detail_spisode_link" href="http://www.agedm.org/play/20130006/1/1">第01话</a>
    """

    if response.status_code == 200:
        # 获取网页的 HTML 内容
        html_content = response.text

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 使用CSS选择器找到class为"a"的div下的所有li标签
        li_tags = soup.select('div.active.show ul.video_detail_episode li a')

        # 获取源类型
        div = soup.select('div.active.show')
        # 因为select返回的是列表，我们取第一个元素（因为只有一个）
        div_id=div[0]['id'] if div else None

        return li_tags,div_id
    else:
        print(f"请求失败，状态码: {response.status_code}")


def get_title(response):

    """

    :param response: 视频信息页
    :return: string类型，动漫标题
    """

    if response.status_code == 200:
        # 获取网页的 HTML 内容
        html_content = response.text

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 使用CSS选择器找到class为"a"的div下的所有li标签
        title_tags = soup.select('h2.video_detail_title')
        return title_tags[0].text.replace(' ','')
    else:
        print(f"请求失败，状态码: {response.status_code}")




def get_download_url(url,typ):
    OK_list=['playlist-source-tt','playlist-source-xigua','playlist-source-bilibili',
             'playlist-source-qq','playlist-source-qiyi']
    if typ in OK_list:
        if typ == 'playlist-source-tt':
            return get_tt_download_url(url)
        else:
            return get_usl_download_url(url)
    else:
        print(typ)
        print(url)
        return get_usl_download_url(url)



url = f'https://www.agedm.org/detail/{id}'
response = get_response(url)
title = get_title(response)
video_list,typ = get_info(response)
for i, item in enumerate(video_list,start=1):
# for i, item in enumerate(video_list[14:],start=15):
    url = f'https://www.agedm.org/play/{id}/1/{i}'
    # print(url)
    cloud_url = get_cloud_url(url)
    # print(cloud_url)
    video_url = get_download_url(cloud_url,typ)
    os.makedirs(f'D:/Downloads/Video/{title}', exist_ok=True)

    filename = f'D:/Downloads/Video/{title}/{title + item.text}.mp4'  # 保存的文件名
    download_video(video_url, filename)
