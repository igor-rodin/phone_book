import model.phone_item as phi
import model.phone_book as phb
import json

def export(phone_book: list) -> str:
    rec_file = "phones.json"
    if len(phone_book) > 0:
        with open(rec_file, 'w', encoding='utf-8') as f:
            json.dump(phone_book, f)
    return rec_file

def export_record(data: phi.phone_record):
    rec_file = "{}.json".format(data.first_name)
    data = [data]
    if len(data) > 0:
        with open(rec_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
    return rec_file

def import_records(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        phb.phone_book.extend([phi.create_record(name, surname, descr, num) \
            for (name, surname, descr, num) in json.load(f)])

