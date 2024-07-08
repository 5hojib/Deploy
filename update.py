from os import path, environ
from subprocess import run
from logging import error, info

UPSTREAM_REPO = environ['UPSTREAM_REPO']
UPSTREAM_BRANCH = environ['UPSTREAM_BRANCH']

if path.exists('.git'):
    run(["rm", "-rf", ".git"])

update = run([f"git init -q \
            && git config --global user.email yesiamshojib@gmail.com \
            && git config --global user.name 5hojib \
            && git add . \
            && git commit -sm update -q \
            && git remote add origin {UPSTREAM_REPO} \
            && git fetch origin -q \
            && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)
