from git import Repo
import os
import requests
repo_url = 'https://github.com/oleend/actions.git'
repo_dir = repo_url.split('/')[-1].split('.')[0]
#existing_repo = Repo(repo_url)

#Prints the Repo
#print(existing_repo)

# List all branches
#for branch in existing_repo.branches:
#    print(branch)

#print("development" in existing_repo.branches)

# go into py envirmoent
# .\activate
# cd into folder
# run python file

#Pushing information


#Where we left off
#You might not need to do all of them



#existing_repo.index.add(".")
    
#existing_repo.index.commit('Testing Commiting everything')

#existing_repo.remotes.origin.push()



# commits = existing_repo.iter_commits('main')


# for commit in commits:
#     print('*'*50)
#     print("Commit id: ",commit,'\nCommit stats: ', commit.stats.files,"\nCommit Author: ", commit.author,"\nCommmit Commiter: ", commit.committer,"\nCommit Message: ", commit.message, "\nCommit Date:", commit.committed_datetime,) # will print the date and time in which the commit made.
#     print('*'*50)


def list_files():
    files = [item.path for item in list(existing_repo.tree().traverse()) if item.type == "blob"]
    return files

def read_file(file_path):
    repo_dir = repo_url.split("/")[-1].split(".")[0]
    file_path = os.path.join(repo_dir, file_path)
    print('*'*50)
    print('Printing File Content: ')
    print('*'*50)
    with open(file_path, "r") as file:
        print(file.read())

def clone():
    if not os.path.exists(repo_dir):
        print('Cloning the Repository')
        Repo.clone_from(repo_url,repo_dir)
    repo = Repo(repo_dir)
    print('Connected with the repository')    


def view_issue_comments(url,headers):
    responce = requests.get(url, headers = headers)
    print("*"*20)
    comments = responce.json()
    for comment in comments:
        print('List of comments:', comment['body'])

def create_issue( title, body):
    url = f"https://api.github.com/repos/{repo_url.split('/')[-2]}/{repo_url.split('/')[-1].split('.')[0]}/issues"
    print(url)
    headers = {
        "Authorization": "token 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",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": title,
        "body": body
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        print(f"Issue created: {response.json()['html_url']}")
    else:
        print("Failed to create issue.", response.json())


def view_issues(state="open"):
    url = f"https://api.github.com/repos/{repo_url.split('/')[-2]}/{repo_url.split('/')[-1].split('.')[0]}/issues?state={state}"
    print(url)
    #url = 'https://api.github.com/repos/oleend/actions/issues?state=open'
    headers = {
            "Authorization": f"token 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",
            "Accept": "application/vnd.github.v3+json"
        }
    print(headers)
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200: 
        issues = response.json()
        #print(issues)
        print(f"Total {len(issues)} {state} issues found in {repo_url}")
        print(len(issues))
        for issue in issues:
            print("*"*8)
            
            print('Issue Comment Count', issue['comments'])
            if issue['comments'] >= 1:
                view_issue_comments(issue['comments_url'], headers)
            print(f"Issue #{issue['number']}: {issue['title']}")
    else:
        print(f"Failed to fetch {state} issues.",response.json())



view_issues(state="open")
create_issue(title="Test Issue #2", body="The body of the issue")

# clone()
# read_file("README.md")
