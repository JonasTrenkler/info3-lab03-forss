import logging
import xml.etree.cElementTree as ET


def new_feed(
    title: str,
    link: str,
    description: str,
    **kwargs: str,
) -> ET.Element:
    root = ET.Element("rss", version="2.0")
    channel = ET.SubElement(root, "channel")

    ET.SubElement(channel, "title").text = title
    ET.SubElement(channel, "link").text = link
    ET.SubElement(channel, "description").text = description

    for k, v in kwargs.items():
        ET.SubElement(channel, k).text = v

    return root


def add_article(
    feed: ET.Element,
    title: str | None = None,
    link: str | None = None,
    description: str | None = None,
    **kwargs: str,
):
    # Sort out arguments that are None
    args = tuple(
        arg
        for arg in (
            (title, "title"),
            (link, "link"),
            (description, "description"),
        )
        if not arg[0] is None
    )

    # One arg has to be set
    if len(args) > 0:
        item = ET.SubElement(feed, "item")

        for arg in args:
            ET.SubElement(item, arg[1]).text = arg[0]

        for k, v in kwargs.items():
            ET.SubElement(item, k).text = v
    else:
        logging.error(
            "Failed to add feed: title, link and description not specified."
        )
