def log(text):
    with open("D:\\Box Sync\\Literature\\_mgmt\\litcommit.log", 'a+') as f:
        f.write(text)

__repo_path__ = 'D:\\Box Sync\\Literature'

try:
    import os
    import sys
    import git

except Exception as e:
    log(' > Error: %s' % format(e))

try:
    repo = git.Repo(__repo_path__)
    repo.git.checkout('auto')

    if 'repo' in locals():
        changes = [item.a_path for item in repo.index.diff(None)] + repo.untracked_files
        changes = [change for change in changes \
                   if os.path.isfile(os.path.join(__repo_path__, change)) and change != '_mgmt/litcommit.log']

        if changes:
            log("\n\t\t Changes: %s" % format(changes))
            try:
                repo.index.add(changes)
                repo.git.commit('-m', 'Automatic commit', author='litcommit <yura.bondarenko@kuleuven.be>')
                log(" > Committed.")
            except Exception as e:
                log(" > Error: %s" % format(e))
        else:
            log(" > No changes.")
except Exception as e:
    log(' > Error: %s' % format(e))


