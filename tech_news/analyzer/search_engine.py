from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    search = {"title": {"$regex": title, "$options": "i"}}
    db = search_news(search)
    result = list()

    for news in db:
        result.append((news["title"], news["url"]))

    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
