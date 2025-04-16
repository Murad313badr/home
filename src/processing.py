from typing import Dict, List, Union

from src.widget import get_date


operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> Union[List, str]:
    """Функция фильтрует операций в списке по ключу 'state'"""
    list_of_operation = [operation for operation in operations if operation.get("state", "UNKNOWN") == state]
    unknown_status_list = [operation for operation in operations if operation.get("state", "UNKNOWN") == "UNKNOWN"]
    if len(operations) == 0:
        return "Отсутствуют данные для обработки! Проверьте правильность ввода!"
    elif len(unknown_status_list) != 0:
        return "Статус одной или нескольких операций не указан!"
    elif len(list_of_operation) == 0:
        return "Операции с данным статусом отсутствуют"
    else:
        return list_of_operation


def sort_by_date(operations: List[Dict], flow: bool = True) -> Union[List, str]:
    """Функция сортирует операции по дате"""
    unknown_date_list: list = [operation for operation in operations if operation.get("date", "UNKNOWN") == "UNKNOWN"]
    filter_by_wrong_date_list: list = [
        operation
        for operation in operations
        if get_date(operation.get("date", "UNKNOWN")) == "Проверьте правильность ввода!"
    ]
    if len(operations) == 0:
        return "Отсутствуют данные для обработки! Проверьте правильность ввода!"
    elif len(unknown_date_list) != 0:
        return "Дата и время одной или нескольких операций не указаны!"
    elif len(filter_by_wrong_date_list) != 0:
        return "Дата и время одной или нескольких операций имеют неверный формат!"
    else:
        sort_by_date_list = sorted(operations, key=lambda operation: operation["date"], reverse=flow)
        return sort_by_date_list


list_of_operation = filter_by_state(operations, state="EXECUTED")

print(list_of_operation)

sort_by_date_list = sort_by_date(operations, flow=True)

print(sort_by_date_list)
