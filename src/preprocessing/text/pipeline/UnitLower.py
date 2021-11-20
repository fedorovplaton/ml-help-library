"""
    Unit for text preprocessing pipeline for converting text's to lower case
"""

from typing import List
from src.preprocessing.text.pipeline.base.UnitBase import UnitBase


class UnitLower(UnitBase[List[str]]):
    """
        Unit for text preprocessing pipeline for converting text's to lower case
    """
    def __init__(self):
        super().__init__(name='Lower')

    @classmethod
    def operation(cls, data: List[str]) -> List[str]:
        """
            Convert all texts to lower case
            :param data:
            :return:
        """
        return list(map(lambda x: x.lower(), data))
