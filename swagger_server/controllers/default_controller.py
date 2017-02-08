import connexion
from swagger_server.models.experiment import Experiment
from swagger_server.models.simulation import Simulation
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def exp_id_get(id):
    """
    exp_id_get
    Получить информацию о конкретном эксперименте.
    :param id: id эксперимента
    :type id: str

    :rtype: Experiment
    """
    return 'do some magic!'


def exp_id_results_get(id):
    """
    exp_id_results_get
    выдает json объект с результатами эксперимента. Эти результаты собираются от каждой симуляции в ракмах эксперимента. Пока что пускай результатом будет одно число - коэффициент доставки пакетов. Антону - тебе нужно будет рисовать графики по этим результатам.
    :param id: id эксперимента
    :type id: str

    :rtype: str
    """
    return 'do some magic!'


def exp_id_setvariables_post(id, params):
    """
    exp_id_setvariables_post
    Задать значения переменных параметров. Вызывается по нажатию кнопки Отправить на кластер.
    :param id: id эксперимента
    :type id: str
    :param params: json строка с параметрами
    :type params: str

    :rtype: str
    """
    return 'do some magic!'


def exp_id_start_get(id):
    """
    exp_id_start_get
    Запустить эксперимент (до этого должен быть подготовлен docker образ через init). Антону - Вызывается по нажатию кнопки Запустить в списке симуляций. Владу - симуляции отправляются на кластер,  число одновременно запущенных симуляций определяется доступным числом процессоров. Пока что пусть будет 2 процесса за раз.
    :param id: id эксперимента
    :type id: str

    :rtype: str
    """
    return 'do some magic!'


def exp_id_stop_get(id):
    """
    exp_id_stop_get
    Остановить эксперимент. Новые симуляции не отсылаются на кластер. Те, что уже запущены - прибиваются, если есть такая возможность.
    :param id: id эксперимента
    :type id: str

    :rtype: str
    """
    return 'do some magic!'


def exp_init_get(gitrepo):
    """
    exp_init_get
    Конструирует новый эксперимент из git репо. 1. в подготовленный docker образ делается git pull 2. собирается бинарник 3. На выходе имеем docker образ с симуляцией. Как запускать образ с параметрами ты уже разобрался
    :param gitrepo: Link to git repo (e.g. git@github.com:nzpr/ns3srv.git)
    :type gitrepo: str

    :rtype: str
    """
    return 'do some magic!'


def sim_id_get(id):
    """
    sim_id_get
    Получить информацию о конкретной симуляции.
    :param id: id симуляции
    :type id: str

    :rtype: Simulation
    """
    return 'do some magic!'


def sim_id_results_get(id):
    """
    sim_id_results_get
    выдает json объект с результатами эксперимента. Эти результаты собираются от каждой симуляции в ракмах эксперимента. Пока что пускай результатом будет одно число - коэффициент доставки пакетов. Антону - тебе нужно будет рисовать графики по этим результатам.
    :param id: id эксперимента
    :type id: str

    :rtype: str
    """
    return 'do some magic!'


def sim_id_vizconnect_get(id):
    """
    sim_id_vizconnect_get
    Поделючение к потоку данных симуляции для визуализации 
    :param id: id симуляции
    :type id: str

    :rtype: str
    """
    return 'do some magic!'
