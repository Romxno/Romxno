import requests
import os

def get_tech_news():
    api_key = os.getenv("NEWS_API_KEY")
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

    # DO NOT LEAVE THESE EMPTY
    start_marker = ""
    end_marker = ""
    
    if start_marker not in readme or end_marker not in readme:
        print("❌ Error: Markers not found! Make sure you added them to README.md")
        return

    header = readme.split(start_marker)[0]
    footer = readme.split(end_marker)[1]
    
    new_readme = f"{header}{start_marker}\n{news_content}\n{end_marker}{footer}"
    
    with open("README.md", "w") as f:
        f.write(new_readme)

if __name__ == "__main__":
    news = get_tech_news()
    update_readme(news)
