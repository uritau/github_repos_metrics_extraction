## Github statistics

The purpose of this project is to get a list of all the PRs MERGED to master in a period with some extra information.

The information that returns is:

| Name | Description |
| --- | --- |
| repo_name | Name of the repository |
| username | who merged the PR |
| creation date | The day that the PR was opened |
| close date | The day that the PR was closed |
| TTL in days | The number of days that the PR was opened |
| Week of year | The year of the year that the PR was closed |
| qtty of coments | The number of the comments in the PR |
| qtty of commits | The number of the commits in the PR |
| qtty of adds | The number of added lines in the PR |
| qtty of dels | The number of deleted lines in the PR |
| qtty of changed files | The number of the changed files in the PR |

# Requirements

- To have a valid github token in  `GITHUB_TOKEN` environment variable.
    It will be used to launch GETs to github, so it should have read permissions at least.


# Variables
You can define some variables inside variables.py that grants some flexibility.

### `start_date`
Probably you don't need to have all the historic information from the repos, so introduce here the starting point from which you want to get data. 
This variable is mandatory and the format is two digits "day/month/year" string.

Per example:
```
start_date = '05/02/23'
```

### `specific_repos`
By default this project gets all the repos from your organization but if you want to limit to few (or even one) repository, you can do it setting specific_repos variable.
This variable is not mandatory and the format is a list of strings.

Per example:

```
specific_repos = ['core_application','repo1','whatever']
```

### `organization`
Maybe you want to change the organization you are reading the information from.
This variable is mandatory and the format is a string.

Per example:

```
organization = 'whatever'
```

### `output_file`
Define the name of the file in which the information will be written. In other words, the destination file.

Per example:

```
output_file = 'output.txt'
```

# How to use this project?

Just launch:

``` bash
python3 ./main.py
```

... and wait some long minutes (more than 30 depending on the quantity of PRs to get!). GH is not the fastest API responding and has a throtling limit so in order to not block itself this project doesn't paralelize the requests :( 

## Expected output

A CSV file separated by semicolon.
The first line will have all the columns definition, and starting into the second line, one line per PR in the repository.


