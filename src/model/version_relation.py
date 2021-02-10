class VersionRelation:
    pass


class Unknown(VersionRelation):
    LABEL = "バージョンの確認ができませんでした"
    COLOR = "orange"


class Future(VersionRelation):
    LABEL = "開発版"
    COLOR = "blue"


class Latest(VersionRelation):
    LABEL = "最新版"
    COLOR = "gray"


class OutOfDate(VersionRelation):
    LABEL = "更新してください"
    COLOR = "red"
