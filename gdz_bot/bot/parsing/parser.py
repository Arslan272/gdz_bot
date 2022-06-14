import requests
from bs4 import BeautifulSoup

headers = {
            "Accept": "* / *",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }


response = requests.get("https://www.euroki.org/gdz/ru/algebra/11_klass/reshebnik-po-algebre-11-klass-mordkovich-denischeva-fgos-276")

soup = BeautifulSoup(response.text, 'html.parser')
for i in soup.find_all('a',{'class' : 'first_topic_headline btn btn-small btn-default'}):
    print(i.text)

for i in soup.find_all('div',{'class' : 'topic_gdzs topic_gdzs_hdln'}):
    for j in i:
        # print(j.get('href'))
        if j.get('href') is not None:
            response1 = requests.get(
                "https://www.euroki.org" + j.get('href'))
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            for photo in soup1.find_all('img', {'class' : 'gdz_image'}):

                link = photo.get('src')
                print(link)
                temp = link.split("/")
                name = temp[-1].split("?")[0]
                req = requests.get(link, allow_redirects=True, params=headers)

                open(f'../image/{name}', 'wb').write(req.content)


