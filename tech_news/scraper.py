from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    else:
        return response.text if response.status_code == 200 else None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    updates = list()
    for article in selector.css("article.entry-preview"):
        url = article.css("a::attr(href)").get()
        updates.append(url)
    return updates


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next::attr(href)").get()
    if not next_page:
        return None
    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    scrape = fetch("https://blog.betrybe.com/")
    print(scrape_updates(scrape))
