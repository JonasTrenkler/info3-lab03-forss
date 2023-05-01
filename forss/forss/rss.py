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
