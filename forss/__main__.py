import logging
import sys
import xml.etree.cElementTree as ET

import bs4

import rss
import web


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    url: str = "https://www.htw-berlin.de/hochschule/aktuelles/"
    feed = rss.new_feed(
        "HTW Termine",
        url,
        "Aktuelles zur HTW",
    )

    response_code, response_text = web.get_html(url)
    if response_code != 200:
        sys.exit(1)

    soup = bs4.BeautifulSoup(response_text, "html.parser")

    termine = soup.find(class_="terminkalender")

    for article in termine.find_all("article"):
        date = f'[{article.find(class_="month").text}/{article.find(class_="day").text}]'
        rss.add_article(
            feed,
            title=f'{date} {article.find("h1").text}',
            description=article.find("p").text,
            link=article.find("a").get("href"),
        )

    ET.indent(feed)

    tree = ET.ElementTree(feed)
    tree.write("termine.rss", encoding="utf-8")

    feed = rss.new_feed(
        "HTW News",
        url,
        "Aktuelles zur HTW",
    )

    soup = bs4.BeautifulSoup(response_text, "html.parser")
    news = soup.find(class_="newslist")

    for article in news.find_all("article"):
        rss.add_article(
            feed,
            title=article.find("h1").text,
            description=article.find("p").text,
            link=article.find("a").get("href"),
        )

    ET.indent(feed)

    tree = ET.ElementTree(feed)
    tree.write("news.rss", encoding="utf-8")
