import requests
import json
import sys
from datetime import datetime
from pr_info import get_pr_information
from variables import organization
from variables import start_date
from variables import output_file
from headers import get_headers
from repos import get_repos_list

date_from_prs = datetime.strptime(start_date,'%d/%m/%y')


def main():
    repo_list = get_repos_list(organization)
    init_file()
    for repo in repo_list:
        page=1
        last_pr,qtty_prs=iterate_pr_list(repo,page)
        while (pending_prs(last_pr, qtty_prs)):
            page += 1
            last_pr,qtty_prs=iterate_pr_list(repo,page)


def iterate_pr_list(repo,page_index):
    prs_list = get_prs_list(organization, repo, page_index)
    if len(prs_list) == 0:
        return "1900-01-01T00:00:00Z", 0
    for pr in prs_list:
        closed_at = datetime.strptime(pr['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
        if (date_from_prs > closed_at):
            return pr['closed_at'],0
        save_pr_info(repo,pr)
    return pr['closed_at'],len(prs_list)
        

def pending_prs(last_pr_date, num_elements):
    last_date = datetime.strptime(last_pr_date, '%Y-%m-%dT%H:%M:%SZ')
    return ((num_elements == 100) & (last_date > date_from_prs))



def save_pr_info(repo_name,pull_request):
    original_stdout = sys.stdout
    created_at = datetime.strptime(pull_request['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    closed_at = datetime.strptime(pull_request['closed_at'], '%Y-%m-%dT%H:%M:%SZ')
    week_of_year = closed_at.strftime("%V")
    open_period = (closed_at - created_at)
    if (pull_request['merged_at']):
        comments,commits,additions,deletions,changed_files = get_pr_information(organization, repo_name, pull_request['number'])
        with open(output_file, 'a') as file:
            sys.stdout = file
            print(repo_name,
                pull_request['number'],
                pull_request['html_url'],
                pull_request['user']['login'],
                created_at.strftime("%m/%d/%Y"),
                closed_at.strftime("%m/%d/%Y"),
                open_period.days,
                week_of_year,
                comments,
                commits,
                additions,
                deletions,
                changed_files,
                sep=';')
        sys.stdout = original_stdout


def get_prs_list(organization, repo, page_index):
    base_url="https://api.github.com/repos/" + organization + "/"
    filters="&base=master&state=closed&per_page=100"
    print ("Working on repo: " + repo + ". Page " + str(page_index))    
    full_url=base_url+repo+"/pulls?page="+str(page_index)+filters
    return requests.get(full_url, headers=get_headers()).json()

def init_file():
    with open(output_file, 'w') as file:
        original_stdout = sys.stdout
        sys.stdout = file
        print("repo_name;\
pr_number;\
html_url;\
username;\
creation date;\
close date;\
TTL in days;\
Week of year;\
qtty of coments;\
qtty of commits;\
qtty of adds;\
qtty of dels;\
qtty of changed files"
        )
        sys.stdout = original_stdout

if __name__ == "__main__":
    main()