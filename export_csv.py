import model.phone_item as phi
import model.phone_book as phb
import csv


def export(file_name: str, phone_book: list):
    if len(phone_book) > 0:
        with open(file_name, mode='w', encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter=",")
            file_writer.writerow(phi.phone_record._fields)
            for item in phb.phone_book:
                file_writer.writerow(item)


def export_record(file_name: str, data: phi.phone_record) -> str:
    if len(data) > 0:
        with open(file_name, 'w', encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter=",")
            file_writer.writerow(phi.phone_record._fields)
            file_writer.writerow(data)


def import_records(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter=",")
        next(file_reader)
        for row in file_reader:
            phb.add_record(phi.create_record(* row))
