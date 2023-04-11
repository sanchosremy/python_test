# Git Hub workflow<a name="git-hub-workflow"></a>

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=1 -->

- [Git Hub workflow](#git-hub-workflow)
  - [GitHub sequence diagram](#github-sequence-diagram)

<!-- mdformat-toc end -->

## GitHub sequence diagram<a name="github-sequence-diagram"></a>

```mermaid
sequenceDiagram
    participant upstream as upstream <br/> https://github.com/sanchosremy/Git_Test
    participant local_git as local git <br/>C:\Users\Christian\Desktop\Projects\Git_Test\.git\
    participant local_folder as local folder <br/>C:\Users\Christian\Desktop\Projects\Git_Test\


    local_folder->>local_folder : modify files
    Note right of local_folder : - modify file <br/> - add file <br/> - delete file

    local_folder->>local_git : git add
    Note right of local_folder : - If you add new file add command tell git track this file
    local_folder->>local_git : git commit
    Note right of local_folder : - commit file from local folder (modifyed or deleted) to local git

    local_git->>local_git : git log

    local_git->>upstream : git push
    Note right of local_git : - move changes<br/>from local git to upstream

    upstream->>local_git : git fetch -v --progress "origin"
    Note right of upstream : - git fetch is a primary command used to download contents from a remote repository

    upstream->>local_git : git rebase
    Note right of local_git : - move changes<br/>from local git to upstream

    local_git->>upstream : git push

```
