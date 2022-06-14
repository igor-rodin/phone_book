from collections import namedtuple as nt

phone_record = nt(
    "PhoneRecord", "first_name second_name description  phone_num")


def create_record(first_name: str, second_name: str, description: str, phone_num: str) -> phone_record:
    return phone_record(first_name, second_name, description, phone_num)
