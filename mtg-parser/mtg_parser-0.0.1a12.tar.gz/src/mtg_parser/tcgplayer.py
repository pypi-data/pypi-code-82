#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from mtg_parser.utils import get_scryfall_url


__all__ = []


def parse_deck(src):
    deck = None
    if _can_handle(src):
        deck = _parse_deck(_download_deck(src))
    return deck


def _can_handle(src):
    return (
        isinstance(src, str)
        and
        re.match(r'https://.*?tcgplayer.com', src)
    )


def _download_deck(src):
    return requests.get(src).text


def _parse_deck(deck):
    soup = BeautifulSoup(deck, features='html.parser')

    for subdeck in soup.find_all('div', class_='subdeck'):
        subdeck_name = next(
            subdeck
            .find('h3', class_='subdeck__name')
            .stripped_strings
        )

        for group in subdeck.find_all('div', class_='subdeck-group'):
            group_name = group.find('h4', class_='subdeck-group__name')
            if group_name:
                group_name = next(group_name.stripped_strings)

            tags = list(_get_tags(subdeck_name, group_name))

            for card in group.find_all('a', class_='subdeck-group__card'):
                quantity = (
                    card
                    .find('span', class_='subdeck-group__card-qty')
                    .get_text(strip=True)
                )
                card_name = (
                    card
                    .find('span', class_='subdeck-group__card-name')
                    .get_text(strip=True)
                )
                card = {
                    'quantity': quantity,
                    'card_name': card_name,
                    'scryfall_url': get_scryfall_url(card_name),
                    'tags': tags,
                }
                yield card


def _get_tags(subdeck_name, group_name):
    if subdeck_name and subdeck_name.lower() == 'command zone':
        yield 'commander'
    if group_name:
        yield group_name.lower()
