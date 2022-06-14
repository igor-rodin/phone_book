import model.phone_item as phi

phone_book = []


def init(phone_list):
    global phone_book
    phone_book = phone_list


def add_record(item: phi.phone_record):
    phone_book.append(item)


def get_record(id: int) -> phi.phone_record:
    return phi.create_record(phone_book[id].first_name, phone_book[id].second_name, phone_book[id].description, phone_book[id].phone_num)


def del_record(id: int):
    phone_book.pop(id)


def edit_record(id: int, first_name: str, second_name: str, description: str, phone_num: str):
    phone_book.pop(id)
    phone_book.insert(id, phi.create_record(
        first_name, second_name, description, phone_num))


def size() -> int:
    return len(phone_book)


def is_empty() -> bool:
    return size() == 0
