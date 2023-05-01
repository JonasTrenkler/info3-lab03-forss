import logging
import xml.etree.cElementTree as ET

import bs4

import rss


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    feed = rss.new_feed(
        "HTW Termine",
        "https://www.htw-berlin.de/hochschule/aktuelles/",
        "Aktuelles zur HTW",
    )

    with open("Aktuelles.html", "r") as html_page:
        soup = bs4.BeautifulSoup(html_page, "html.parser")

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
