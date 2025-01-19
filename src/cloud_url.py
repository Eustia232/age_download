from bs4 import BeautifulSoup

from response import get_response


def get_cloud_url(url):

    """

    :param url: 视频播放页
    :return: 云视频地址
    """


    response=get_response(url)

    if response.status_code == 200:
        # 获取网页的 HTML 内容
        html_content = response.text

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # 找到 <iframe> 标签
        iframe_tag = soup.find('iframe', id='iframeForVideo')

        # 提取 src 属性
        if iframe_tag and 'src' in iframe_tag.attrs:
            iframe_src = iframe_tag['src']
            return iframe_src
    else:
        print(f"请求失败，状态码: {response.status_code}")


if __name__ == '__main__':
    url = 'https://www.agedm.org/play/20060018/1/1'
    url2='https://www.agedm.org/play/20150017/1/1' #tt云
    url3='https://www.agedm.org/play/20230303/1/3'#西瓜
    url4='https://www.agedm.org/play/20210114/1/1'#bilibili
    url5='https://www.agedm.org/play/20110006/1/1'#腾讯
    url6='https://www.agedm.org/play/20210061/1/1'#自建云
    url7='https://www.agedm.org/play/20180017/1/1'#爱奇艺
    print(get_cloud_url(url7))
