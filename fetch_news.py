def update_readme(news_content):
    with open("README.md", "r") as f:
        readme = f.read()

    # ADD THE TEXT INSIDE THESE QUOTES
    start_marker = ""
    end_marker = ""
    
    if start_marker not in readme or end_marker not in readme:
        print("❌ Error: Markers not found! Make sure you added them to README.md")
        return

    # Split the file safely
    header = readme.split(start_marker)[0]
    footer = readme.split(end_marker)[1]
    
    # Reassemble with the new news in the middle
    new_readme = f"{header}{start_marker}\n{news_content}\n{end_marker}{footer}"
    
    with open("README.md", "w") as f:
        f.write(new_readme)

if __name__ == "__main__":
    latest_news = get_tech_news()
    print(f"DEBUG: News fetched: {latest_news[:100]}...") # This shows in your logs
    if len(latest_news.strip()) > 30: # Only update if we actually got news
        update_readme(latest_news)
    else:
        print("⚠️ No news found to update.")
