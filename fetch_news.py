def update_readme(news_content):
    with open("README.md", "r") as f:
        readme = f.read()

    start_marker = ""
    end_marker = ""
    
    # This check prevents the "ValueError" you saw
    if start_marker not in readme or end_marker not in readme:
        print("Error: Markers not found in README.md! Please add them.")
        return

    # Splitting logic
    parts = readme.split(start_marker)
    header = parts[0]
    footer = parts[1].split(end_marker)[1]
    
    new_readme = f"{header}{start_marker}\n{news_content}\n{end_marker}{footer}"
    
    with open("README.md", "w") as f:
        f.write(new_readme)
