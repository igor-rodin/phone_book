import model.phone_item as phi


def export(phone_book: list) -> str:
    rec_file = "phones.json"
    print("Export phone book to JSON")
    return rec_file


def export_record(data: phi.phone_record):
    rec_file = "{}.json".format(data.first_name)
    print(f"Export record {data} to JSON")
    return rec_file


def import_records(file_name):
    pass
