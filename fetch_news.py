import requests
import os

def get_tech_news():
    api_key = os.getenv("NEWS_API_KEY")
    # Fetching news about DevOps, Cloud, and AI
    url = f"https://newsapi.org/v2/everything?q=DevOps+OR+Cloud+OR+AI&sortBy=publishedAt&pageSize=5&apiKey={api_key}&language=en"
    
    response = requests.get(url).json()
    articles = response.get('articles', [])
    
    content = "### 📰 Latest News (Updated Daily)\n\n"
    for art in articles:
        content += f"- **[{art['title']}]({art['url']})** \n  *{art['source']['name']} - {art['publishedAt'][:10]}*\n\n"
    return content

def update_readme(news_content):
    with open("README.md", "r") as f:
        readme = f.read()

    start_marker = ""
    end_marker = ""
    
    # Split and rebuild the README around the markers
    new_readme = readme.split(start_marker)[0] + start_marker + "\n" + news_content + "\n" + end_marker + readme.split(end_marker)[1]
    
    with open("README.md", "w") as f:
        f.write(new_readme)

if __name__ == "__main__":
    news = get_tech_news()
    update_readme(news)
