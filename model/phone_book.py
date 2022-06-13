import model.phone_item as phi

phone_book = []


def init(phone_list):
    global phone_book
    phone_book = phone_list


def add_record(item: phi.phone_item):
    phone_book.append(item)


def get_item(id: int) -> phi.phone_item:
    return phi.create_item(phone_book[id].first_name, phone_book[id].second_name, phone_book[id].description, phone_book[id].phone)


def del_item(id: int):
    phone_book.pop(id)


def change_first_name(id: int, new_val: str):
    old_item = phone_book.pop(id)
    phone_book.insert(id, phi.create_item(
        new_val, old_item.second_name, old_item.description, old_item.phone))


def change_second_name(id: int, new_val: str):
    old_item = phone_book.pop(id)
    phone_book.insert(id, phi.create_item(
        old_item.second_name, new_val, old_item.description, old_item.phone))


def change_description_name(id: int, new_val: str):
    old_item = phone_book.pop(id)
    phone_book.insert(id, phi.create_item(
        old_item.first_name, old_item.second_name, new_val, old_item.phone))


def change_phone(id: int, new_val: str):
    old_item = phone_book.pop(id)
    phone_book.insert(id, phi.create_item(
        old_item.first_name, old_item.second_name, old_item.description, new_val))


def size() -> int:
    return len(phone_book)


def is_empty() -> bool:
    return size() == 0
