import json

from src.model.version import Version
import urllib.request
import urllib.error


class GitHubRepoRelease:
    URL_TEMPLATE: str = "https://api.github.com/repos/{}/{}/releases/latest"

    def __init__(self, owner: str, repo_name: str):
        self.owner = owner
        self.repo_name = repo_name

    @property
    def url(self) -> str:
        url = GitHubRepoRelease.URL_TEMPLATE.format(self.owner, self.repo_name)
        return url

    @property
    def version(self) -> Version:
        tag_name = self.get_latest_version_tag_name()
        version = Version(tag_name)
        return version

    def get_latest_version_tag_name(self) -> str:
        raw_data = self.__fetch_all_info()
        tag_name = raw_data["tag_name"]
        return tag_name

    def __fetch_all_info(self) -> dict:
        url = self.url

        with urllib.request.urlopen(url) as web_file:
            raw_data = web_file.read().decode()
            result = json.loads(raw_data)

        return result
