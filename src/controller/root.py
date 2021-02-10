from src.view.root import Root
from src.controller.version_checker import check_version
from src.model.version_relation import VersionRelation


class RootController:
    def __init__(self):
        pass

    def run(self):
        version_status: VersionRelation = check_version()

        view_root = Root(version_status=version_status)
        view_root.run()
