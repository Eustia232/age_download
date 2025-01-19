import requests
from fake_useragent import UserAgent


def get_response(url):
    headers = {
        'User-Agent': UserAgent().random
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)
        # Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }

    response = requests.get(url, headers=headers)
    return response


if __name__=='__main__':
    url='https://www.agedm.org/detail/20150017'
    res=get_response(url)
    print(res.text)