import model.phone_item as phi
import model.phone_book as phb
import json


def export(file_name: str, phone_book: list):
    if len(phone_book) > 0:
        with open(file_name, 'w', encoding='utf-8') as f:
            exp_book = [val._asdict() for val in phone_book]
            json.dump(exp_book, f)


def export_record(file_name: str, data: phi.phone_record):
    if len(data) > 0:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data._asdict(), f)


def import_records(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if issubclass(type(data), list):
            for dict in data:
                phb.add_record(phi.create_record(* dict.values()))
        else:
            phb.add_record(phi.create_record(* data.values()))
