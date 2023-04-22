from tech_news.database import search_news
from datetime import datetime


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
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        date_output = date.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    search = {"timestamp": {"$regex": date_output, "$options": "i"}}
    result = list()

    for i in search_news(search):
        result.append((i["title"], i["url"]))

    return result


# Requisito 9
def search_by_category(category):
    search = {"category": {"$regex": category, "$options": "i"}}
    db = search_news(search)
    result = list()

    for news in db:
        result.append((news["title"], news["url"]))

    return result
