from tkinter import messagebox

from config import REPO_OWNER_NAME, REPO_NAME, VERSION
from src.model.version_relation import *
from src.model.github_repo_release import GitHubRepoRelease
from src.view.messagebox import warning


def check_version():
    result: VersionRelation = __check_version()

    if result == OutOfDate:
        warning("最新版が利用できます。更新してください。")

    return result


def __check_version():
    release: GitHubRepoRelease = GitHubRepoRelease(owner=REPO_OWNER_NAME, repo_name=REPO_NAME)

    if release.version is None:
        return Unknown

    if release.version < VERSION:
        return Future

    if release.version == VERSION:
        return Latest

    if release.version > VERSION:
        return OutOfDate
