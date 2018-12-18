def log(text):
    with open("D:\\Box Sync\\Literature\\_mgmt\\litcommit.log", 'a+') as f:
        f.write(text)

log(' > ')

try:
    import os
    import sys
    import git
except Exception as e:
    log('Import Error')

__repo_path__ = 'D:\\Box Sync\\Literature'
repo = git.Repo(__repo_path__)

changes = [item.a_path for item in repo.index.diff(None)] \
    + repo.untracked_files
changes = [change for change in changes \
           if os.path.isfile(os.path.join(__repo_path__, change))
           and change != '_mgmt/litcommit.log']

if changes:
    log("Changes: %s > " % format(changes))
    repo.git.checkout('auto')
    repo.index.add(changes)
    repo.git.commit(
        '-m', 'Automatic commit',
        author = 'litcommit <yura.bondarenko@kuleuven.be>'
        )
    log("Committed.")
else:
    log("No changes.")

