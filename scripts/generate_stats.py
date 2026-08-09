import os
import urllib.request
import json
from datetime import datetime

username = os.environ.get("GH_LOGIN", "vikram662005")
token = os.environ.get("GITHUB_TOKEN", "")

url = f"https://api.github.com/users/{username}"

headers = {
    "User-Agent": "github-profile-generator"
}

if token:
    headers["Authorization"] = f"Bearer {token}"

request = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(request) as response:
    data = json.loads(response.read().decode())

name = data.get("name") or username
repos = data.get("public_repos", 0)
followers = data.get("followers", 0)
following = data.get("following", 0)

year = datetime.now().year

def make_svg(filename, title, value):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="500" height="120" viewBox="0 0 500 120">
    <rect width="500" height="120" fill="#000000"/>
    <text x="25" y="40" fill="#ffffff" font-family="monospace" font-size="18">{title}</text>
    <text x="25" y="85" fill="#ffffff" font-family="monospace" font-size="32">{value}</text>
</svg>"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(svg)

make_svg("stats.svg", "PUBLIC REPOSITORIES", repos)
make_svg("streak.svg", "FOLLOWERS", followers)
make_svg("langs.svg", "FOLLOWING", following)
make_svg("year.svg", "YEAR", year)

print("Profile statistics generated successfully.")
