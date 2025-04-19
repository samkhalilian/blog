import os
import pandas as pd
import requests
from sphinx.application import Sphinx


# Replace with your GitHub repository details
_GITHUB_OWNER = "samkhalilian"
_GITHUB_REPO = "blog"
_GITHUB_ISSUES_API_URL = f"https://api.github.com/repos/{_GITHUB_OWNER}/{_GITHUB_REPO}/issues/comments"
_GITHUB_TOKEN = os.getenv("_GITHUB_TOKEN_SAMKHALILIAN")


def generate_data(app: Sphinx) -> None:
    """Fetch issues comments from GitHub Issues and save to CSV."""
    headers = {"Accept": "application/vnd.github.v3+json"}

    response = requests.get(_GITHUB_ISSUES_API_URL, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch GitHub Utterances comments:", response.status_code)
        return pd.DataFrame()

    comments = response.json()

    data = []
    for comment in comments:
        url_repo = "/".join(comment['html_url'].split("/")[:5])
        project = url_repo.split("/")[-2]
        repo = url_repo.split("/")[-1]
        if comment['html_url'].startswith(url_repo + "/issues/"):        
            data.append({
                "|:thumbsup:|": comment["reactions"]["+1"],
                # "Repo": f"`{repo} <{url_repo}>`_",
                "Id": f"`#{comment['html_url'].split('#')[0].split('/')[-1]} <{comment['html_url']}>`_",
                "Title": comment["body"],
                "Author": comment["user"]["html_url"],  
                "Created": comment["created_at"],
            })

    df = pd.DataFrame(data)
    df.sort_values(by=["|:thumbsup:|", "Created"], ascending=[False, True], inplace=True)
    print(df.head(2))
    path = r"C:\Users\samkh\OneDrive\Documents\GitHub\blog\source\_data\github_issues.csv"
    df.to_csv(path, index=False)
    # return df


def setup(app: Sphinx):
    """Register the extension with Sphinx"""
    app.connect("builder-inited", generate_data)
    return {"version": "0.1", "parallel_read_safe": True}
