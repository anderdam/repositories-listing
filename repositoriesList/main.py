import os

import dotenv
from repositoriesList.GithubRepos import GithubRepos

# from repositoriesList.GitlabRepos import GitLabRepos
from repositoriesList.SaveRepos import SaveRepos

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
dotenv.load_dotenv(dotenv_path=dotenv_path)
github_token = dotenv.get_key(dotenv_path=dotenv_path, key_to_get="GITHUB_TOKEN")

output_dir = os.path.join(os.path.dirname(__file__), "output")

# save_gitlab = SaveRepos(
#         limit=GitLabRepos(token=github_token).check_rate_limit(),
#         repos=GitLabRepos(token=github_token).get_gitlab_repositories())

try:
    save_github = SaveRepos(
        limit=GithubRepos(token=str(github_token)).check_rate_limit(),
        repos=GithubRepos(token=str(github_token)).get_github_repositories(),
        name=f"{output_dir}/github_repositories.txt",
    )
    print("GitHub repositories saved.")
except Exception as e:
    print(f"Error: {e}")
    print("Could not save GitHub repositories.")
