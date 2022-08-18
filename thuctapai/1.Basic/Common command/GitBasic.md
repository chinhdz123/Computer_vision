<h2>1.Introduction to Git<h2>
    <h4>Git is officialy defined as distributed version control system(VCS).In other words, it's a system that tracks changes to our project files   
    over time. It enables us to record project changes and go back to a specific version of the tracked files, at any given point in time. This  
    system can be used by many people to efficiently work together and collaborate on team projects, where each developer can have their own  
    version of the project, distributed on their computer. Later on, these individual versions of the project can be merged and adapted into the  
    main version of the project.<h4>

<h2>2.Setup instructions<h2>
    <h4>Git is primarily used via the command-line interface, which we can access with our
    system terminals.
    Configuring your nam & Email
        git config --global user.name "Your Name"
        git config --global user.email "YourEmail@email.com"
    Replace the values inside the quotes with your name and email address.
    Not used to log in
    used to track who made what changes<h4> 
    
<h3>3.Initializing a Repositories<h3>
    <h4>The command below will generate a hidden.git directory for your project, where Got 
    stores all internal tracking data for the curren repository: 
        git init<h4>
<h3>4.Staging and committing code<h3>
<h3>4.1.Checking the status<h3>
    <h4>While located inside the project folder in our terminal, we can type the follow command
    to check the status of our repository:
        git status
    It show us which files have been changed, which files are tracked,...<h4>
<h3>4.2.Staging files<h3>
    <h4>From the project folder, we can use the git add command to add our files to stagin
    area which allows them to be tracked.
    We can add a specific file to the staging area with the following command:
        git add file.js
    To add multiple files, we can do this:
        git add file.js, file1.py, file2.py
    Instead of having to add the files individually, we can also add all the files inside
    the project folder to the staging area:
       git add .<h4>
<h3>4.3. Making commits<h3>
    <h4>To commit the files from the staging area, we use the following commnad:
        git commit -m "Commit message"<h4>
<h3>4.4 Commit history<h3>
    <h4>To see all the commits that were made for our project, you can use the following
    command:
        git log
    To go back to a previousof your state of your project code that you commited, you can
    use the following command:
        git checkout < commit-hash>
    To go back to the latest commit ( the newest version of our project code), you can
    type this command:
        git checkout master<h4>
<h3>5.Upload local repositories to remote repositories<h3>
    <h4>git remote add origin <path-git>
    git push -u origin master<h4>
<h2>6.Synchronize from the remote repositories to the local repositories<h2>
    <h4>git pull<h4>
<h2>7.Download file from github<h2>
    <h4>git clone <path-git><h4>