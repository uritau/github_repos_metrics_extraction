import os


def get_headers():
    GH_TOKEN = os.environ['GITHUB_TOKEN']
    return {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer " + GH_TOKEN,
    "X-GitHub-Api-Version": "2022-11-28"
}