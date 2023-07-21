import requests
from bs4 import BeautifulSoup
import urllib

def fetch(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    alllinks = []
    allimgs = []

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_elements = soup.find_all("a", class_="thumbnail-item__wrap")
        for a in a_elements:
            link_url =  a["href"]
            if link_url.startswith("/en/view/"):
                newlink_url = 'http://www.insecam.org/' + link_url
                alllinks += [newlink_url]

        div_elements = soup.find_all("div", class_="textcenter")
        for div in div_elements:
            img_elements = div.find_all("img")
            for img in img_elements:
                image_url = img["src"]
                if 'http' in image_url:
                    # print(image_url)
                    allimgs += [image_url]

        for i in range(len(alllinks)):
            print(alllinks[i] + ' : ' + allimgs[i])
            f = open("cams/result.txt", "a")
            f.write(alllinks[i] + ' : ' + allimgs[i]+'\n')
            f.close()

    else:
        print("The request failed.")

url = "http://www.insecam.org/en/bytag/Traffic/?page="

for i in range(1,24):
    fetch(url+str(i))