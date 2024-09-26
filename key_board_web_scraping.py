import bs4
import requests
import string

urls = {
    'red_k8': 'https://catalog.onliner.by/keyboards/keychron/k8pj1ru',
    'brown_k8': 'https://catalog.onliner.by/keyboards/keychron/k8pj3ru',
    'red_v3': 'https://catalog.onliner.by/keyboards/keychron/v3b1ru',
    'brown_v3': 'https://catalog.onliner.by/keyboards/keychron/v3b3ru'
}
html_class_name = 'offers-description__link offers-description__link_nodecor js-description-price-link'


def get_price(address, tag, class_name) -> tuple:
    data = requests.get(address)
    soup = bs4.BeautifulSoup(data.text, 'lxml')
    something_name = remove_non_ascii(soup.select('h1')[0].text.strip())
    if soup.find(tag, class_=class_name) is None:
        return something_name, 'Out of stock'
    something_price = remove_non_ascii(soup.find(tag, class_=class_name).text.strip()) + 'p.'
    return something_name, something_price


def remove_non_ascii(a_str):
    ascii_chars = set(string.printable)

    return ''.join(
        filter(lambda x: x in ascii_chars, a_str)
    ).strip()


def get_keyboards_info() -> str:
    result = ''
    for url in urls.values():
        name, price = get_price(url, 'a', html_class_name)
        result += f'{name}: {price}\n'
    return result
