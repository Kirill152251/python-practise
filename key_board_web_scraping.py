import bs4
import requests

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
    something_name = soup.select('h1')[0].text.strip()
    if soup.find(tag, class_=class_name) is None:
        return something_name, 'Нет в наличии и под заказ'
    something_price = soup.find(tag, class_=class_name).text.strip()
    return something_name, something_price


def get_keyboards_info() -> str:
    result = ''
    for url in urls.values():
        name, price = get_price(url, 'a', html_class_name)
        result += f'{name}: {price}\n'
    return result


print(get_keyboards_info())
