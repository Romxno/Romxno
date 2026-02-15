import requests, re
from datetime import datetime

API_KEY = "YOUR_NEWS_API_KEY"  # store in GitHub Secrets
categories = {
    "🔧 DevOps": "DevOps",
    "☁️ Cloud": "Cloud computing",
    "🤖 AI": "Artificial Intelligence"
}

news_md = ""
for category, query in categories.items():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3,
        "apiKey": API_KEY
    }
    r = requests.get(url, params=params)
    articles = r.json().get("articles", [])
    
    news_md += f"### {category}\n"
    for a in articles:
        title = a['title']
        link = a['url']
        desc = a.get('description', '')
        date = a.get('publishedAt', '')[:10]
        news_md += f"- [{title}]({link}) ({date})\n  > {desc}\n\n"

# Insert into README
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- NEWS_SECTION_START -->(.*?)<!-- NEWS_SECTION_END -->",
    f"<!-- NEWS_SECTION_START -->\n{news_md}<!-- NEWS_SECTION_END -->",
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
