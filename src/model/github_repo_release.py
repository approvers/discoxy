from typing import Optional
import json

import urllib.request
import urllib.error

from src.model.version import Version
from src.view.messagebox import warning


class GitHubRepoRelease:
    URL_TEMPLATE: str = "https://api.github.com/repos/{}/{}/releases/latest"

    def __init__(self, owner: str, repo_name: str):
        self.owner = owner
        self.repo_name = repo_name
        self.fetched_data: Optional[dict] = None

        self.fetch_data()

    @property
    def url(self) -> str:
        url = GitHubRepoRelease.URL_TEMPLATE.format(self.owner, self.repo_name)
        return url

    @property
    def data(self) -> Optional[dict]:
        if self.fetched_data is None:
            return None

        return self.fetched_data

    @property
    def latest_version_tag(self) -> Optional[str]:
        if self.data is None:
            return None

        tag_name = self.data["tag_name"]
        return tag_name

    @property
    def version(self) -> Optional[Version]:
        tag_name = self.latest_version_tag
        version = Version.from_str(version_str=tag_name)
        return version

    def fetch_data(self) -> None:
        url = self.url

        try:
            with urllib.request.urlopen(url) as web_file:
                raw_data = web_file.read().decode()
                result = json.loads(raw_data)

                self.fetched_data = result

        except Exception as e:
            warning(
                "GitHubへ接続できませんでした。\nインターネットへの接続を確認してくだい。\n"
                "発生した例外:\n{}".format(e)
            )
