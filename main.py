
from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description="EgyBest Downloader")
parser.add_argument("url", help="movie to download")
parser.add_argument("-q", "--quality", type=int, help="quality to download in",
                    default=480, choices=(360, 480, 720, 1080))

args = parser.parse_args()


source = requests.get(args.url).text
soup = BeautifulSoup(source, "lxml")

qualities = soup.find("table", class_="dls_table").tbody
for row in qualities.find_all("tr"):
    if str(args.quality) in row.find_all("td")[1].text:
        url = row.find("td", class_="tar").find_all("a")[1]["href"]
        break
else:
    raise ValueError("quality not found")


print(url)