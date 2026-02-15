import requests, re

url = "https://newsapi.org/v2/everything"
params = {
    "q": "DevOps OR Cloud OR AI",
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 5,
    "apiKey": "YOUR_API_KEY"
}
r = requests.get(url, params=params)
articles = r.json().get("articles", [])

news_md = ""
for a in articles:
    news_md += f"- [{a['title']}]({a['url']})\n"

with open("README.md", "r") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- NEWS_SECTION_START -->(.*?)<!-- NEWS_SECTION_END -->",
    f"<!-- NEWS_SECTION_START -->\n{news_md}<!-- NEWS_SECTION_END -->",
    content,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(new_content)
