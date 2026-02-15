name: Update Tech News

on:
  schedule:
    - cron: "0 6 * * *"   # Runs daily at 6 AM UTC
  workflow_dispatch:       # Allow manual trigger

jobs:
  update-news:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install dependencies
        run: pip install requests feedparser

      - name: Fetch latest news
        run: python update_news.py

      - name: Commit changes
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git commit -m "Update tech news"
          git push
