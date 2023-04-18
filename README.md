# Automating Git Operations using Python, Intergrating it with git actions


This is Python code that perform various Git operations like: `listing branches', creating or switching branches, committing files to branches, listing files, reading file content, cloning a repository, viewing issue comments, creating an issue, and 'viewing issues.`



This code uses GitPython library to interact with Git repository and requests library to interact with GitHub API.

It also uses Python's argparse module to parse command-line arguments and store them as instance variables.

Lastly, this code is used in conjunction with GitHub Actions to automate Git operations and integrate with various other workflows.

Here is the code with explanations of each method:

This code provides several methods that allow performing Git operations on a remote repository.

The _init_ method is a constructor that initializes the class properties with the repository URL and the token. The repo_dir property is set as the last part of the URL, without the .git extension, which will be used as the directory name where the local repository will be cloned.

The clone method clones the remote repository to the local directory if it doesn't exist. If the cloning process fails, it returns None.

The listBranch method lists all the branches in the local repository.

The createOrSwitchBranch method creates a new branch if it doesn't exist, or switches to an existing branch.

The commitFile method stages a file for commit, commits it with a message, and pushes the commit to the remote repository. If the file is not found, an error message is printed.

The gitLogCommits method prints the commits made in a specific branch.

The list_files method prints all the files in the repository.

The read_file method reads a file from the local repository and prints its content.

The view_issue_comments method prints the comments made on a specific issue.

The create_issue method creates a new issue in the repository with a given title and body.

The view_issues method lists all the issues in the repository with their comments. The state parameter can be set to "open" or "closed" to list the issues in the respective state.




## Running
py clean.py  https://github.com/oleend/GithubActions.git --token "token-code" --option "Which Function to run"

## Running With Github Actions
change the "option" via python-app.yml and push this to the repository
