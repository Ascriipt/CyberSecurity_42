from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

import validators
import requests
import argparse
import random
import lxml
import sys
import os

previously_in_spider = []

parser = argparse.ArgumentParser(description="Image Web Scraper")
parser.add_argument("URL", type=str, help="URL you want to scrape")
parser.add_argument("-r", help="Recursively downloads images", action="store_true")
parser.add_argument("-l", type=int, help="How DEEP is your love", default=5)
parser.add_argument("-p", type=str, help="Path to save downloaded images [./data]", default="./data")
args = parser.parse_args()

if not validators.url(args.URL):
	sys.exit("Error: Invalid URL format.")

USER_AGENTS = [
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
]

def spyder(curr_url: str, current_depth=0):
    try:
        page = requests.get(curr_url, headers={'User-Agent': random.choice(USER_AGENTS)}, timeout=6, allow_redirects=False, stream=True)
    except requests.RequestException:
        return

    try:
        os.makedirs(args.p)
    except OSError as e:
        pass
    soup = BeautifulSoup(page.text, "lxml")

    images = soup.find_all('img')
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    image_urls = [img['src'] for img in images if 'src' in img.attrs and any(img['src'].lower().endswith(ext) for ext in valid_extensions)]

    if args.r and current_depth < args.l:
        hyperlinks = soup.find_all("a")
        hyperlinks_url = [hp['href'] for hp in hyperlinks if 'href' in hp.attrs]
        for i in hyperlinks_url:
            hp = urljoin(curr_url, i)
            baseURL = urlparse(curr_url).scheme + "://" + urlparse(curr_url).netloc
            if f"{hp}".startswith(baseURL) and not curr_url == hp:
                if not hp in previously_in_spider:
                    previously_in_spider.append(hp)
                    print(f"=========================I am in: {curr_url}, going to {hp}, the depth is {current_depth}=========================")
                    spyder(hp, current_depth + 1)

    for url in image_urls:
        image_url = urljoin(curr_url, url)
        
        try:
            image_data = requests.get(image_url, headers={'User-Agent': random.choice(USER_AGENTS)}, timeout=6, allow_redirects=False, stream=True).content
            image_name = os.path.basename(image_url)
            image_path = os.path.join(args.p, image_name)
            
            with open(image_path, 'wb') as f:
                f.write(image_data)
        
        except requests.RequestException as e:
            print(f"Failed to download {url}: {e}")

spyder(args.URL)