from typing import List


class Version:
    def __init__(self, version_str: str):
        self.version_str = version_str

    @property
    def int_list(self):
        version_str = self.version_str
        return Version.version_str_to_list(version_str)

    @staticmethod
    def version_str_to_list(version_str: str) -> List[int]:
        split = version_str.split(".")

        version_int_list: List[int] = []

        for part in split:
            version_int_list.append(int(part))

        return version_int_list

    @staticmethod
    def __compare_versions(x, y):

        if len(x.int_list) > len(y.int_list):
            return ValueRelations.LARGER
        if len(x.int_list) < len(y.int_list):
            return ValueRelations.SMALLER

        for x_int, y_int in zip(x.int_list, y.int_list):
            if x_int > y_int:
                return ValueRelations.LARGER
            if x_int < y_int:
                return ValueRelations.SMALLER

        return ValueRelations.EQUAL

    def __lt__(self, other):
        result = Version.__compare_versions(self, other)
        return result == ValueRelations.SMALLER

    def __eq__(self, other):
        result = Version.__compare_versions(self, other)
        return result == ValueRelations.EQUAL

    def __le__(self, other):
        return (self == other) or (self < other)

    def __ne__(self, other):
        return not(self == other)

    def __gt__(self, other):
        return not(self == other) and not(self < other)

    def __ge__(self, other):
        return not(self < other)

    def __str__(self):
        return self.version_str


class ValueRelations:
    LARGER = 1
    EQUAL = 0
    SMALLER = -1
