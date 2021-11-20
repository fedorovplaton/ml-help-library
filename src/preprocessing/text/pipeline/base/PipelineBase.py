"""
    Base model for pipeline
"""

from abc import ABC
from typing import TypeVar, Generic, List

from src.preprocessing.text.pipeline.base.UnitBase import UnitBase

T = TypeVar('T')


class PipelineBase(ABC, Generic[T]):
    """
        PipelineBase
    """
    name: str
    units: List[UnitBase[T]]

    @classmethod
    def __init__(cls, name: str = 'Unit name'):
        cls.name = name
        cls.units: List[UnitBase[T]] = []

    @classmethod
    def print(cls) -> str:
        """
        :return: Unit name
        """
        return cls.__name__

    @classmethod
    def set_units(cls, units: List[UnitBase[T]]) -> None:
        """
            add_units
            :param units:
        """
        cls.units = units

    @classmethod
    def execute(cls, data: T) -> T:
        """
            execute
            :param data:
            :return:
        """
        result = data

        for unit in cls.units:
            result = unit.operation(result)

        return result




