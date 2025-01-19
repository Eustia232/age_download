import re

from response import get_response

def get_tt_download_url(url):
    response=get_response(url)
    if response.status_code == 200:
        # 获取网页的 HTML 内容
        html_content = response.text

        # 使用 BeautifulSoup 解析 HTML
        match = re.search(r"var Vurl = '(.+?)';", html_content)
        if match:
            vurl_value = match.group(1)
            return vurl_value
        else:
            print("Vurl variable not found.")
    else:
        print(f"请求失败，状态码: {response.status_code}")


if __name__=='__main__':
    url='https://43.240.156.118:8443/m3u8/?url=age_7176A3UKffyjbm9z3qJqhUDWY31r67MsEkX1sCUUapIBDhIIdnUUGf3ob1Gb%2ByG6PvQJxyDaZ8g0R6NfsO7cOPcmOFbmOxgTYeCa%2F2XWvtp1cWAcMYTuePZdoDsqJP3nyUNlU599gOJGht%2BKD6v4v%2FdN2iebe39siVn1cqSB'
    print(get_tt_download_url(url))