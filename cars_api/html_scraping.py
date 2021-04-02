# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class Scraping:
    """
        Cars.com Html Scraping
    """
    def __init__(self, html):
        self._soup = BeautifulSoup(html, "lxml")

    def get_data(self, car_id: str):
        """
            get car image, color, trans type
            input
            car_id = car_id to scraping
            return
            images: list = images list
            exterior_color: str = car exterior_color
            trans: str = transmission type
        """
        images = []
        exterior_color = "None"
        trans = "None"
        list_rows = self._soup.find("a", {"id": f"listing-{car_id}"})
        if list_rows:
            images = get_image_url(list_rows)
            exterior_color, trans = get_color_trans(list_rows)
        return images, exterior_color, trans


def get_image_url(row) -> list:
    """
     get image urls
     input
     row = selected car div
     return
      images: list = images list
    """
    images = []
    meta = row.find("div", {"class": "photo-scroll-wrapper"})
    for meta_item in meta:
        if str(meta_item).strip():
            image = meta_item.get('style', meta_item.get('data-lazy-style'))
            images.append(image[image.find("(")+1: image.find(")")])
    return images


def get_color_trans(row) -> [str, str]:
    """
    get get and transmission type
    input
    row = selected car div
    return
    exterior_color: str = car exterior_color
    trans: str = transmission type
    """
    meta = row.find("ul", {"class": "listing-row__meta"}).find_all("li")
    exterior_color = ""
    trans = ""

    for meta_item in meta:
        if 'Ext. Color:' in meta_item.text:
            exterior_color = meta_item.text.replace('\n', '').replace('Ext. Color: ', '').strip()
        if 'Transmission:' in meta_item.text:
            trans = meta_item.text.replace('\n', '').replace('Transmission: ', '').strip()

    return exterior_color, trans
