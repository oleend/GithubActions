# Automating Git Operations using Python, Intergrating it with git actions

This is Python code that perform various Git operations like: `listing branches', creating or switching branches, committing files to branches, listing files, reading file content, cloning a repository, viewing issue comments, creating an issue, and 'viewing issues.`


<ul>


<li>It also uses Python's argparse module to parse command-line arguments and store them as instance variables.</li>

<li>Lastly, this code is used in conjunction with GitHub Actions to automate Git operations and integrate with various other workflows.</li>
</ul>

## <b>Here is the code with explanations of each method:</b>

<ol>
<li>The _init_ method is a constructor that initializes the class properties with the repository URL and the token. The repo_dir property is set as the last part of the URL, without the .git extension, which will be used as the directory name where the local repository will be cloned.</li>
<br>

<li>The clone method clones the remote repository to the local directory if it doesn't exist. If the cloning process fails, it returns None.</li>
<br>
<li>The listBranch method lists all the branches in the local repository.</li>
<br>
<li>The createOrSwitchBranch method creates a new branch if it doesn't exist, or switches to an existing branch.</li>
<br>
<li>The commitFile method stages a file for commit, commits it with a message, and pushes the commit to the remote repository. If the file is not found, an error message is printed.</li>
<br>
<li>The gitLogCommits method prints the commits made in a specific branch.</li>
<br>
<li>The list_files method prints all the files in the repository.</li>
<br>
<li>The read_file method reads a file from the local repository and prints its content.</li>
<br>
<li>The view_issue_comments method prints the comments made on a specific issue.</li>
<br>
<li>The create_issue method creates a new issue in the repository with a given title and body.</li>
<br>
<li>The view_issues method lists all the issues in the repository with their comments. The state parameter can be set to "open" or "closed" to list the issues in the respective state.</li>
</ol>



## Running
py clean.py  https://github.com/oleend/GithubActions.git --token "token-code" --option "Which Function to run"

