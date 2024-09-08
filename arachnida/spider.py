import requests
import argparse
import sys

av = sys.argv

parser = argparse.ArgumentParser(description="Image Web Scraper")
parser.add_argument("URL", type=str, help="URL you want to scrape")
parser.add_argument("-r", help="Recursively downloads images", action="store_true")
parser.add_argument("-l", type=int, help="How DEEP is your love", default=5)
parser.add_argument("-p", type=str, help="The path where you want to download the images")
args = parser.parse_args()

print(args.p)

page = requests.get(av[1])

print(page.text)
