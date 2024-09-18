import os

import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.github.com/user/repos"
username = os.getenv("USER_NAME")
repo_name = os.getenv("REPO_NAME")
token = os.getenv("TOKEN")
headers = {"Authorization": f"token {token}"}


def create_repo(repo_name):
    data = {"name": repo_name}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Repository created!")
    else:
        print(f'Error! {response.json()}')


def check_repo(repo_name):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        names_list = [repo["name"] for repo in repos]
        if repo_name in names_list:
            print("Repository exists!")
            return True
        else:
            print("Repository doesn't exist!")
            return False
    else:
        print(f'Error! {response.json()}')
        return False


def delete_repo(repo_name, username):
    delete_url = f'https://api.github.com/repos/{username}/{repo_name}'
    response = requests.delete(delete_url, headers=headers)
    if response.status_code == 204:
        print(f'Repository deleted!')
    else:
        print(f'Error! {response.json()}')


create_repo(repo_name)
check_repo(repo_name)
delete_repo(repo_name, username)

