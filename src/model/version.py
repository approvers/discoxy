from typing import List

from src.model.value_relation import *


class Version:
    def __init__(self, version_str: str):
        if type(version_str) != str:
            raise RuntimeError(
                "Invalid parameter has passed.\n"
                "Expected `str`, got `{}` type parameter.\n".format(type(version_str)) +
                "If there is possibility that not `str` type parameter is passed,"
                "Consider use `Version.from_str()` instead."
            )

        self.version_str = version_str

    @staticmethod
    def from_str(version_str: str):
        if version_str is None:
            return None

        return Version(version_str)

    @property
    def int_list(self):
        version_str = self.version_str
        return Version.version_str_to_list(version_str)

    @staticmethod
    def version_str_to_list(version_str: str) -> List[int]:
        if version_str is None:
            return None

        split = version_str.split(".")

        version_int_list: List[int] = []

        for part in split:
            version_int_list.append(int(part))

        return version_int_list

    @staticmethod
    def __compare_versions(x, y):
        if len(x.int_list) > len(y.int_list):
            return Larger
        if len(x.int_list) < len(y.int_list):
            return Smaller

        for x_int, y_int in zip(x.int_list, y.int_list):
            if x_int > y_int:
                return Larger
            if x_int < y_int:
                return Smaller

        return Equal

    def __lt__(self, other):
        result = Version.__compare_versions(self, other)
        return result == Smaller

    def __eq__(self, other):
        result = Version.__compare_versions(self, other)
        return result == Equal

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
