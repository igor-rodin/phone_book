import model.phone_item as phi
import model.phone_book as phb
import csv

def export(phone_book: list) -> str:
    rec_file = "phones.csv"
    if len(phone_book) > 0:
        with open(rec_file, mode='w', encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter = ",")
            for item in c.phone_book():
                file_writer.writerow(item)
    return rec_file


def export_record(data: phi.phone_record) -> str:
    rec_file = "{}.csv".format(data.first_name)

    if len(data) > 0:
        with open(rec_file, 'w', encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter = ",")
            file_writer.writerow(data)
    return rec_file

def import_records(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        file_reader = csv.reader(f, delimiter = ",")
        phb.phone_book.extend([phi.create_record(row[0],row[1],row[2],row[3]) for row in file_reader])
