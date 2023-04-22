from tech_news.database import create_news
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
    selector = Selector(text=html_content)
    news = dict()
    url = selector.css('link[rel="canonical"]::attr(href)').get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url::text").get()
    reading_time = (
        selector.css("li.meta-reading-time::text").get().split(" ")[0]
    )
    summary = selector.css(
        "div.entry-content:first-of-type > p:nth-of-type(1) *::text"
    ).getall()
    category = selector.css("span.label::text").get()

    news = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": "".join(summary).strip(),
        "category": category,
    }

    return news


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    html_content = fetch(url)
    updates = list()
    result = list()

    while len(updates) < amount:
        updates.extend(scrape_updates(html_content))
        html_content = fetch(scrape_next_page_link(html_content))

    for up in updates[:amount]:
        f = fetch(up)
        result.append(scrape_news(f))

    create_news(result)
    return result


if __name__ == "__main__":
    scrape = fetch("https://blog.betrybe.com/")
    print(scrape_updates(scrape))
