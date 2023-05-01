import logging
import requests


def get_html(url: str) -> tuple[int, str]:
    logging.info(f"Making request to {url}.")
    response = requests.get(url)

    if response.status_code == requests.codes.ok:
        logging.info(f"Response status {requests.codes.ok} (OK)")
    else:
        logging.warning(f"Request failed with status code {response.status_code}.")

    return response.status_code, response.text
