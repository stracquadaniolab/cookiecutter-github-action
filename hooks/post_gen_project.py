import sys
import subprocess as sh

# initialise git
sh.run(["git", "init"], check=True)

# adding remote for push
sh.run(["git", "remote", "add", "origin", "{{cookiecutter.artifact_git}}"], check=True)

sys.exit(0)