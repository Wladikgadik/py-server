# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Experiment(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: int=None, status: int=None, varibles: str=None, created_at: str=None):
        """
        Experiment - a model defined in Swagger

        :param id: The id of this Experiment.
        :type id: int
        :param status: The status of this Experiment.
        :type status: int
        :param varibles: The varibles of this Experiment.
        :type varibles: str
        :param created_at: The created_at of this Experiment.
        :type created_at: str
        """
        self.swagger_types = {
            'id': int,
            'status': int,
            'varibles': str,
            'created_at': str
        }

        self.attribute_map = {
            'id': 'id',
            'status': 'status',
            'varibles': 'varibles',
            'created_at': 'created_at'
        }

        self._id = id
        self._status = status
        self._varibles = varibles
        self._created_at = created_at

    @classmethod
    def from_dict(cls, dikt) -> 'Experiment':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Experiment of this Experiment.
        :rtype: Experiment
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this Experiment.

        :return: The id of this Experiment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Experiment.

        :param id: The id of this Experiment.
        :type id: int
        """

        self._id = id

    @property
    def status(self) -> int:
        """
        Gets the status of this Experiment.
        0 - подготовка (клонирование, сборка бинарника), 1 - запущен, 2 - закончен, 3 - приостановлен, 4 - ошибка, не удалось подготовить эксперимент

        :return: The status of this Experiment.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """
        Sets the status of this Experiment.
        0 - подготовка (клонирование, сборка бинарника), 1 - запущен, 2 - закончен, 3 - приостановлен, 4 - ошибка, не удалось подготовить эксперимент

        :param status: The status of this Experiment.
        :type status: int
        """

        self._status = status

    @property
    def varibles(self) -> str:
        """
        Gets the varibles of this Experiment.
        Переменные параметры эксперимента в фрмате json {var1:[1,2,3],var2:[0.1,0.3] и т.п.}. Это вводит пользователь во фронтенде.

        :return: The varibles of this Experiment.
        :rtype: str
        """
        return self._varibles

    @varibles.setter
    def varibles(self, varibles: str):
        """
        Sets the varibles of this Experiment.
        Переменные параметры эксперимента в фрмате json {var1:[1,2,3],var2:[0.1,0.3] и т.п.}. Это вводит пользователь во фронтенде.

        :param varibles: The varibles of this Experiment.
        :type varibles: str
        """

        self._varibles = varibles

    @property
    def created_at(self) -> str:
        """
        Gets the created_at of this Experiment.

        :return: The created_at of this Experiment.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """
        Sets the created_at of this Experiment.

        :param created_at: The created_at of this Experiment.
        :type created_at: str
        """

        self._created_at = created_at
