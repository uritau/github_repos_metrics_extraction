from headers import get_headers
import requests
from variables import specific_repos

def get_repos_list(organization):
    page = 1
    repos_list = specific_repos
    if (repos_list):
        print("Using a predefined repos list.")
    else:
        repo_list_base="https://api.github.com/orgs/" + organization + "/repos?per_page=20&page="
        print ("Get all organization repositories")     
        repos = requests.get(repo_list_base + "1", headers=get_headers()).json()
        repos_list += [repo['name'] for repo in repos]

        while len(repos) == 20:
            page += 1
            repos = requests.get(repo_list_base + str(page), headers=get_headers()).json()
            repos_list += [repo['name'] for repo in repos]
    return repos_list