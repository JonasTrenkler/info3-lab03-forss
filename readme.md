# Forss

## Project

> This project is part of [Exercise 03](https://bkleinen.github.io/classes/ss2023/info3/labs/lab-03-pythonproject/) of the info3 course at the University of Applied Sciences, Berlin.

TODO: describe project use case and usage

## Dependencies

Forss uses [requests](https://docs.python-requests.org/en/latest/index.html) and [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) to parse a website.
To produce the feed XML file, it uses the native [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html).

To install the dependencies use [pipenv](https://pipenv.pypa.io/en/latest/). Clone the repository and use `pipenv install --dev` to create a virtual python environment and fetch all dependencies.
The `--dev` flag will also fetch [Black](https://black.readthedocs.io/en/stable/index.html) as formatter and [Pytest](https://docs.pytest.org/en/7.3.x/).

