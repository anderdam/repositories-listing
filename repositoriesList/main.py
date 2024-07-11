import os

import dotenv
from repositoriesList.GithubRepos import GithubRepos
from repositoriesList.GitlabRepos import GitLabRepos

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
dotenv.load_dotenv(dotenv_path=dotenv_path)
github_token = dotenv.get_key(dotenv_path=dotenv_path, key_to_get="GITHUB_TOKEN")
gitlab_token = dotenv.get_key(dotenv_path=dotenv_path, key_to_get="GITLAB_TOKEN")

output_dir = os.path.join(os.path.dirname(__file__), "output")

try:
    GithubRepos(token=str(github_token)).save_repositories(
        name="/home/anderdam/projects/repositoriesList/repositoriesList/output/github_repositories.txt"
    )
    GithubRepos(token=gitlab_token).print_results()
    print("Github Repositories saved.")
except Exception as e:
    print(f"Error: {e}")
    print("Could not save Github repositories.")

try:
    GitLabRepos(token=str(github_token)).save_repositories(
        name="/home/anderdam/projects/repositoriesList/repositoriesList/output/gitlab_repositories.txt"
    )
    GitLabRepos(token=str(gitlab_token)).print_results()
    print("Gitlab Repositories saved.")
except Exception as e:
    print(f"Error: {e}")
    print("Could not save Gitlab repositories.")
