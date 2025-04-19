import os
import pandas as pd
import requests
from sphinx.application import Sphinx


_GITHUB_OWNER = "samkhalilian"
_GITHUB_REPO = "blog"
_GITHUB_TOKEN = os.getenv("GITHUB_TOKEN_SAMKHALILIAN")


# GraphQL API endpoint
url = 'https://api.github.com/graphql'


def generate_data(app: Sphinx) -> None:
    """Fetch discussions from GitHub Discussions and save to CSV."""
    # GraphQL query to fetch the first 5 discussions
    query = f"""
    {{
    repository(owner: "{_GITHUB_OWNER}", name: "{_GITHUB_REPO}") {{
        discussions(first: 10) {{
        nodes {{
            title
            url
            createdAt
            author {{
            login
            }}
        }}
        }}
    }}
    }}
    """

    headers = {
        "Authorization": f"Bearer {_GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json={"query": query}, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch GitHub Utterances comments:", response.status_code)
        return pd.DataFrame()

    data = response.json()
    discussions = data["data"]["repository"]["discussions"]["nodes"]
    rows = []
    for d in discussions:
        rows.append({
            "Id": f"`#{d['url'].split('/')[-1]} <{d['url']}>`_",
            "Title": d['title'],
            "Author": d['author']['login'],
            "Created": d['createdAt'],
           
        })

    df = pd.DataFrame(rows)
    df.sort_values(by=["Created", "Author"], ascending=[False, True], inplace=True)
    path = r"C:\Users\samkh\OneDrive\Documents\GitHub\blog\source\_data\github_discussions.csv"
    df.to_csv(path, index=False)
    # return df
        

def setup(app: Sphinx):
    """Register the extension with Sphinx"""
    app.connect("builder-inited", generate_data)
    return {"version": "0.1", "parallel_read_safe": True}
