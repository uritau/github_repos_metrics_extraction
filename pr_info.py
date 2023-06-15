import requests
import json
import sys

from headers import get_headers

def get_pr_information(organization, repo, pr_number):
    base_url="https://api.github.com/repos/" + organization + "/"
    filters="&per_page=100"
    page_index=1
    full_url=base_url+repo+"/pulls/"+str(pr_number)+"?page="+str(page_index)+filters
    pr_info = requests.get(full_url, headers=get_headers()).json()
    return (pr_info['comments'],
        pr_info['commits'],
        pr_info['additions'],
        pr_info['deletions'],
        pr_info['changed_files']
    )

