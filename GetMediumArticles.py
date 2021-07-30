#!/usr/bin/env python3

import requests, datetime, threading
from bs4 import BeautifulSoup

"""
This program has record of a bunch of publications on medium.com and 
their urls and uses this to fetch the top 3 articles from the previous 
day and stores them in my daily notes within my obsidian vault.
"""


class GetMediumArticles:
    def __init__(self):
        self.urls = {
            "Towards Data Science": "https://towardsdatascience.com/archive/",
            "UX Collective": "https://uxdesign.cc/archive/",
            "The Startup": "https://medium.com/swlh/archive/",
            "Mission.org": "https://medium.com/the-mission/archive/",
            "Personal Growth": "https://medium.com/personal-growth/archive/",
            "UX Planet": "https://uxplanet.org/archive/",
            "Better Programming": "https://betterprogramming.pub/",
            "Netflix": "https://netflixtechblog.com/",
        }

        self.data = {}

    def get_articles(self, publication, url):
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        date = str(yesterday.strftime("%Y/%m/%d"))

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

            article = {
                "title": title,
                "article_url": article_url,
            }

            if not self.data.get(publication):
                self.data[publication] = [article]
            else:
                self.data[publication].append(article)

    def write_to_vault(self, data):
        obsidian_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))

        with open(
            f"/Users/jackparsons/Library/Mobile Documents/iCloud~md~obsidian/Documents/🧠 Second Brain/📓 Daily Notes/{obsidian_date}.md",
            "a",
        ) as file:
            out = ""

            for publication, articles in data.items():
                out += f"## ***{publication}***\n"
                for article in articles:
                    out += f"#### [{article['title']}]({article['article_url']})\n\n"

                    # --Version without direct title links--
                    # out += f"#### {article['title']}\n Link: {article['article_url']}\n\n"

                out += "---\n\n"

            file.write(out)

    def run(self):
        threads = []

        for publication, url in self.urls.items():
            thread = threading.Thread(target=self.get_articles, args=[publication, url])
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("All Articles Found")

        self.write_to_vault(self.data)


if __name__ == "__main__":
    app = GetMediumArticles()
    app.run()
