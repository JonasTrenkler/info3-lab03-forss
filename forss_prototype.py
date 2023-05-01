""" This is a prototype for the forss program, hard-coded to the news section <https://www.htw-berlin.de/hochschule/aktuelles/>
of the University of Applied Sciences, Berlin """

import sys
import xml.etree.ElementTree as ET

import bs4
import requests

# following:

# res = requests.get(https://www.htw-berlin.de/hochschule/aktuelles/)
# try:
#    res.raise_for_status()
# except Exception as exc:
#    print("There was an error downloading the html document:", exc)
# soup = bs4.BeautifulSoup(res.text, 'html.parser')

# use a downloaded html file for testing, instead of constantly downloading one
with open("Aktuelles.html", "r") as html_page:
    soup = bs4.BeautifulSoup(html_page, "html.parser")

# print(type(soup))
# print(soup.title.string)

# extraction of the relevant parts is easy, as long as you know where to look:
newslist = soup.find(class_="newslist")
headlines = newslist.find_all("h1")
texts = newslist.find_all("p")

for headline, text in zip(headlines, texts):
    print(headline.parent.get('href'))
    print(f"{headline.text}: {text.text}")

root = ET.Element("rss", attrib={"version": "2.0"})
tree = ET.ElementTree(root)

channel = ET.SubElement(root, "channel")

title = ET.SubElement(channel, "title")
title.text = "HTW News"

channel_link = ET.SubElement(channel, "link")
channel_link.text = "https://www.htw-berlin.de/hochschule/aktuelles/"

for headline, text in zip(headlines, texts):
    item = ET.SubElement(channel, "item")

    title = ET.SubElement(item, "title")
    title.text = headline.text

    description = ET.SubElement(item, "description")
    description.text = text.text

    link = ET.SubElement(item, "link")
    link.text = headline.parent.get('href')

# prettify the output: indent the whole tree according to the elements level
ET.indent(tree)
# print(ET.tostring(root))
tree.write("feed.rss", encoding="utf-8")
