import os
from github import Github
from typing import Optional
from fastapi import FastAPI

g = Github(os.environ["TEST_GITHUB_TOKEN"])
app = FastAPI()

@app.get("/")
def read_root():
    return {"OK"}

@app.get("/repos/{org_name}/{repo_name}")
def read_repo(org_name: str, repo_name: str):
    print(g.get_repo(org_name + "/" + repo_name))
    return {"OK"}

@app.get("/repos")
def read_repo():
    for repo in g.get_user().get_repos():
        print(repo.name)
    return {"OK"}
