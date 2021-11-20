"""
    Unit for text preprocessing pipeline for converting text's to lower case
"""

from typing import List
import re

from src.preprocessing.text.pipeline.base.UnitBase import UnitBase


class UnitSplitJoinTokenizer(UnitBase[List[str]]):
    """
        Unit for text preprocessing pipeline for converting text's to lower case
    """
    re_word_pattern: str
    join_pattern: str

    @classmethod
    def __init__(cls, word_pattern: str = r"\w\w+", join_pattern: str = " "):
        super().__init__(name='SplitJoinTokenizer')
        # ToDo Platon Fedorov rewrite it with re.compile
        cls.re_word_pattern = word_pattern
        cls.join_pattern = join_pattern

    @classmethod
    def __convert__(cls, text: str) -> str:
        return cls.join_pattern.join(re.findall(cls.re_word_pattern, text, re.U))

    @classmethod
    def operation(cls, data: List[str]) -> List[str]:
        """
            Convert all texts to lower case
            :param data:
            :return:
        """
        return list(map(cls.__convert__, data))
