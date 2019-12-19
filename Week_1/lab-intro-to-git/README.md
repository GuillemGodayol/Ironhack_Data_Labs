![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Introduction to Git

## Introduction

In this lab we will go through all the concepts seen in the Git class with a hands on exercise. All the class will use a GitHub account provided by the TAs, so the whole class will be modifying the same repository. This is done to replicate the experience of working under the same team.

### Prerequisites

* You should have the GitHub account details provided by the TAs.

* You should have logged into the account and cloned the repository.

If you have any doubts about the prerequisites please clarify with your instructor or teaching assistants.

### Overview of Steps

Below is a summary of the steps you will follow in this lab:

1. Create a folder with your name.
2. Create a file named about-myself.md.
3. Modify that file as requested.
4. Pull changes from the remote repository.
5. Upload your changes to the remote repository.

### Deliverables

* The folder with your name should contain the file `about-myself.md` in it with all the requeriments specified.

## Instructions

### Step 1 - Check Local Branch Status

If you work in a team, every time before you start working on the code you should check if there is any unstaged or uncommited changes in your local branch by executing `git status` within the project directory in Terminal.

In the git status output, check whether there is any **file with unstaged changes** or **untracked files**. Sometimes you may also find **files with changes to be committed**. Since we just cloned the repository, there shouldn't be any changes, but is a good practice to check the state of your local repository before making further changes.

### Step 2 - Create a folder with your name

Inside the folder `lab-intro-to-git`, your local repository, create another folder with your name. Make sure that the spaces are filled with _ instead (My_Name). Inside your folder, create a file named `about-myself.md`.

Execute the command `git status` in your terminal and you will see the following message:

```bash
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	Your_Name/
nothing added to commit but untracked files present (use "git add" to track)
```

As the promp says, Git has noticed that we have new files in our local repository and it helps us by showing us which command to use to track this new file.

We will proceed to add this new folder, which contains the about-myself.md file, with the command `git add` and execute the `git status` command, we will see the following message:

```bash
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   Your_Name/about-myself.md
```
What Git is telling us is that we have new information to commit and gives us a command to remove this file from the *Staging Area* in case we made a mistake and don't want to commit this file.
Since we do want to commit it, we will go ahead and use the command `git commit` or `git commit -m` and write a meaningful commit message.

### Step 3 - Create a new branch and modify about-myself.md 

It's a good practice to create a new branch and make all the desired changes in there and merge it with the master branch once the changes are done, since it's a good way to keep your master branch clean. This is why you will create a new branch called **feature** using the `git branch feature` command.
To change to **feature** we need to use the `git checkout feature` command. If no problem arose, you should see the following message:

```bash
Switched to branch 'feature'
```
Now, open `about-myself.md` and fill it with the following information:

```
# Who am I

* Name
* Last Name
```
If you check the status of your local repository with `git status`, you should see the following message:

```bash 
On branch feature
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   about-myself.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Go ahead and add the changes of your file to the *Staging Area*.

### Step 4 - Modifying the previous commit

Currently, you should be on the **feature** branch. We just commited the file `about-myself.md` with our name and last names, but we have decided that it was a very small amount of information and we also want to add 3 hobbies. We could just add the information and create another commit, but since we will add similar information we want to keep it all in one commit. So how do we modify previous commits? We have two options, either we revert the previous commit and add the changes or we use the `git ammend` command. We will show you how to do both and you can choose the one you prefer:

**Reverting previous commit**

First we need to see the commit history, since we want to revert to a commit before the changes were made. To do this we will use `git log`, you should see something like the following information after executing the command:

```bash
commit e39f1bf7d8e6dd6d55ac4b9b09fc3e692c8aa459 (HEAD -> feature)
Author: your user name <yourmail@gmail.com>
Date:   Mon Oct 21 06:33:15 2019 +0200

    Modify about-myself.md

commit 82fe755b0894f3f091bd948e55f6dee6b0be8ec3 (master)
Author: your user name <yourmail@gmail.com>
Date:   Mon Oct 21 06:04:18 2019 +0200

    Create new folder with about-myself.md file

commit 70570b14cf651120281c9e4968396355505aa161 (origin/master, origin/HEAD)
Author: ta-data-bcn <47005065+ta-data-bcn@users.noreply.github.com>
Date:   Mon Oct 21 05:24:02 2019 +0200

    Update README.md

commit 89768d8faeb5ad8a23f37ff75a01f24b67441e25
Author: ta-data-bcn <47005065+ta-data-bcn@users.noreply.github.com>
Date:   Mon Oct 21 05:07:53 2019 +0200

    Initial commit
```
The big string containing numbers and letters intertwined is the identifier for each commit (**SHA-1 hash**). To go back to a previous commit we need to use `git reset <commit identifier>`. This will revert the status of your local repository (your folder) to the way it was in the commit of your choosing, but it will keep the changes that you made in your folder. This means that the commit no longer exists, but the changes we made to `about-myself.md` are still there, we just need to add the information we wanted to the file, add it and commit it.

**Ammending previous commit**

If we just want to add something to our previous commit or change the commit message, we can use `git commit amend`. This command is very similar to `git commit` but instead of creating new commit it just add the information that we have in the *Staging Area* to the previous commit.
Now, open the file `about-myself.md` and write 3 hobbies of yours. You can use the following format: 

```
# Hobbies:

* 
*
*
```

Once you're done, save the changes and close the file. Now add it to the *Staging Area* using `git add` and finally use `git commit amend` to commit the changes. Now a text editor will pop up and you will see the previous commit message, you can change the commit message if you want or keep it. Once you are done, save the changes and close the editor and your previous commit will have all the new changes.

### Step 5 - Merge changes into master

Since we have done all the changes that we wanted in `about-myself.md`, we will merge our branches so that our master branch has all the work we have done so far. To do this follow these instructions:

- Change to the master branch. `git checkout`
- Open `about-myself.md`. You will see that it's a different file that the one we were modifying in the feature branch.
- Use `git merge feature`. This will incorporate all the information of the feature branch into the master branch.
- Now open `about-myself.md` again and check if all the information is there.


### Step 6 - Pushing Changes

Now that we have finished modifying our file, let's upload our changes to the remote repository. To do this, we need to use the command `git push`. Be wary, if you colleagues have pushed before you this message will display in your console:

```
Updates were rejected because the remote contains work that you do not have locally. This is usually caused by another repository pushing to the same ref. You may want to first integrate the remote changes (e.g., git pull...) before pushing again.
```
This means that you will need to use `git pull` to download the changes uploaded by your colleagues in the remote repository before uploading your own.

### Step 7 - Resolving Conflicts

Change to the **feature branch** again and make one last modification to `about-myself.md`:

- Add the place where you were born at the end of the file.
- Add and commit the changes and merge **master** with **feature**.

Before pushing, talk with you TAs to notify that you have reached this part and wait for their confirmation. They will also add something to your `about-myself.md` file that will create a conflict and you will have to solve it before being able to push to the remote repository.

