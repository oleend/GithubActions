# Just a reminder to import things or you will run into an error
# Example (repo must be imported)
from git import Repo
import os
import argparse
import requests


# C:\ScrappingPython\scraping
class GitOperation:
    #constructer in python
    def __init__(self,repo_url,token):
        self.repo_url = repo_url
        self.repo_dir = repo_url.split("/")[-1].split(".")[0]
        self.repo = self.clone()
        self.token = token
    #List Branches, need to refer to self repo as it is part of the constructure of class object
    def listBranch(self):
        for branch in self.repo.branches:
            print(branch)

    def createOrSwitchBranch(self, branchName):
        if (branchName in self.repo.branches):
            # To checkout to a branch:
            self.repo.git.checkout(branchName)
        else:
            # Create a new branch
            self.repo.git.branch(branchName)
            self.repo.git.checkout(branchName)
    def commitFile(self,filename):
        try:
            self.repo.index.add(filename)
            self.repo.index.commit(f'Updated {filename}')
            self.repo.remotes.origin.push()
        except FileNotFoundError:
            print('Check if the Url is correct or the commiting file is in the repo')
        except Exception as e:
            print(e)

        
    def gitLogCommits(self,branchname):
        print('git log commits for branch: ',branchname)
        commits = self.repo.iter_commits(branchname)

        for commit in commits:
            print('*'*50)
            print("Commit id: ",commit,'\nCommit stats: ', commit.stats.files,"\nCommit Author: ", commit.author,"\nCommmit Commiter: ", commit.committer,"\nCommit Message: ", commit.message, "\nCommit Date:", commit.committed_datetime,) # will print the date and time in which the commit made.
            print('*'*50)

    def list_files(self):
        print([item.path for item in self.repo.tree().traverse() if item.type == "blob"])


    def read_file(self, file_path):
        file_path = os.path.join(self.repo_dir, file_path)
        print('*'*50)
        print('Printing File Content: ')
        print('*'*50)
        with open(file_path, "r") as file:
            print(file.read())
            print('*'*50)

    def clone(self):
        if not os.path.exists(self.repo_dir):
            print('Cloning the Repository')
            try:
                Repo.clone_from(self.repo_url, self.repo_dir)
            except: 
                print('Repo Not found')
                return None
        print('Connected with the repository')  
        return(Repo(self.repo_dir))
    
    @staticmethod
    def view_issue_comments(url,headers):
        responce = requests.get(url, headers = headers)
        print("*"*20)
        comments = responce.json()
        for comment in comments:
            print('List of comments:', comment['body'])
    
    def create_issue(self, title, body):
        url = f"https://api.github.com/repos/{self.repo_url.split('/')[-2]}/{self.repo_url.split('/')[-1].split('.')[0]}/issues"
        headers = {
            "Authorization": f"token {self.token}",
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
    
    def view_issues(self, state="open"):
        url = f"https://api.github.com/repos/{self.repo_url.split('/')[-2]}/{self.repo_url.split('/')[-1].split('.')[0]}/issues?state={state}"
        
        #url = 'https://api.github.com/repos/oleend/actions/issues?state=open'
        headers = {
                "Authorization": f"token {self.token}",
                "Accept": "application/vnd.github.v3+json"
            }
        print(headers)
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200: 
            issues = response.json()
            #print(issues)
            print(f"Total {len(issues)} {state} issues found in {self.repo_url}")
            print(len(issues))
            for issue in issues:
                print("*"*8)
                
                print('Issue Comment Count', issue['comments'])
                if issue['comments'] >= 1:
                    self.view_issue_comments(issue['comments_url'], headers)
                print(f"Issue #{issue['number']}: {issue['title']}")
        else: 
            print('Something went wrong when fetching issues ' + str(response))
                

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_url", type=str, help="URL of the repository to scrape")
    parser.add_argument("--token", type=str, help="Please Provide the Github Token")
    args = parser.parse_args() 
    gitObject = GitOperation(args.repo_url, args.token)
    #print(gitObject.repo == None) 
    #object of a class or an instance of a class
    #gitObject = GitOperation(repo_url = 'C:\ScrappingPython\scraping') 
    #gitObject = GitOperation(repo_url = 'https://github.com/oleend/actions.git') 
    # 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
    if gitObject.repo:
        gitObject.listBranch()
        gitObject.createOrSwitchBranch('main')
        gitObject.commitFile('cleanCode.py')
        gitObject.list_files()
        gitObject.read_file('README.md')
        gitObject.create_issue(title="Test Issue #2", body="The body of the issue")
        gitObject.view_issues()
    #existing_repo = Repo('C:\ScrappingPython\scraping')
    #gitObject.gitLogCommits('test')
    #gitObject.gitLogCommits('development')

    # Working on inputing token and automating push
    #Then Github actions