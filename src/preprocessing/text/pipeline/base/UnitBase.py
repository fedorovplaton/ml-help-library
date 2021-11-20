"""
    Base model for pipeline unit
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class UnitBase(ABC, Generic[T]):
    """
        UnitBase
    """
    name: str

    @classmethod
    def __init__(cls, name: str = 'Unit name'):
        cls.name = name

    @abstractmethod
    def operation(self, data: T) -> T:
        """
            Method to operate data
            :param data:
        """
        raise NotImplementedError('You should implement "operation" method')

    @classmethod
    def print(cls) -> str:
        """
        :return: Unit name
        """
        return cls.__name__
