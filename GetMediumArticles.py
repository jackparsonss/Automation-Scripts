import requests, datetime, threading
from bs4 import BeautifulSoup

"""
This program has record of a bunch of publications on medium.com and 
their urls and uses this to fetch the top 3 articles from the previous 
day and stores them in my daily notes within my obsidian vault.
"""

urls = {
    # "Towards Data Science": "https://towardsdatascience.com/archive/",
    "UX Collective": "https://uxdesign.cc/archive/",
    "The Startup": "https://medium.com/swlh/archive/",
    "Mission.org": "https://medium.com/the-mission/archive/",
    "Personal Growth": "https://medium.com/personal-growth/archive/",
    "UX Planet": "https://uxplanet.org/archive/",
    "Better Programming": "https://betterprogramming.pub/",
    "Google Design": "https://medium.com/google-design/",
    "Angel List": "https://medium.com/angellist-blog/",
    "Netflix": "https://netflixtechblog.com/",
    "Web Dev Zone": "https://medium.com/web-development-zone/",
}

threads = []
data = {}
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
date = str(yesterday.strftime("%Y/%m/%d"))

obsidian_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))


def get_articles(publication, url):
    url = url + date

    print(f"Fetching Articles from {url}")

    response = requests.get(url, allow_redirects=True)

    try:
        response.raise_for_status()
    except Exception:
        print(f"No Articles Found At {url}")

    page = response.content
    soup = BeautifulSoup(page, "lxml")
    articles = soup.find_all(
        "div",
        class_="postArticle postArticle--short js-postArticle js-trackPostPresentation js-trackPostScrolls",
    )

    amount_of_articles = min(3, len(articles))

    for i in range(amount_of_articles):
        title = articles[i].find("h3", class_="graf--title")

        if title is None:
            continue

        title = title.contents[0]
        article_url = articles[i].find_all("a")[3]["href"].split("?")[0]

        data[title] = {
            "article_url": article_url,
            "publication": publication,
        }


def write_to_vault(data):
    with open(
        f"/Users/jackparsons/Library/Mobile Documents/iCloud~md~obsidian/Documents/🧠 Second Brain/📓 Daily Notes/{obsidian_date}.md",
        "a",
    ) as file:
        out = ""

        for title, info in data.items():
            out += f"##### {title} - {info['publication']} \nLink: {info['article_url']}\n\n---\n\n"

        file.write(out)


def main():
    for publication, url in urls.items():
        thread = threading.Thread(target=get_articles, args=[publication, url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All Articles Found")

    write_to_vault(data)


if __name__ == "__main__":
    main()
