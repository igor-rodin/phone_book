from collections import namedtuple as nt

phone_item = nt("PhoneItem", "first_name second_name description  phone")


def create_item(first_name: str, second_name: str, description: str, phone: str) -> phone_item:
    return phone_item(first_name, second_name, description, phone)
