import requests, re, feedparser
from datetime import datetime

# RSS feeds for each category
rss_urls = {
    "🔧 DevOps": "https://devops.com/feed/",
    "☁️ Cloud": "https://cloudblogs.microsoft.com/feed/",
    "🤖 AI": "https://ai.googleblog.com/feeds/posts/default"
}

news_md = ""
for category, url in rss_urls.items():
    feed = feedparser.parse(url)
    news_md += f"### {category}\n"
    for entry in feed.entries[:3]:  # latest 3 posts
        title = entry.title
        link = entry.link
        summary = re.sub(r'\s+', ' ', entry.summary)[:200]  # short snippet
        date = entry.get("published", "")[:16]  # trim date
        news_md += f"- [{title}]({link}) ({date})\n  > {summary}...\n\n"

# Update README.md
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
