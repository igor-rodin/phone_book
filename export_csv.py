import model.phone_item as phi


def export(phone_book: list) -> str:
    rec_file = "phones.csv"
    print("Export phone book to CSV")
    return rec_file


def export_record(data: phi.phone_record) -> str:
    rec_file = "{}.csv".format(data.first_name)
    print(f"Export record {data} to CSV")
    return rec_file


def import_records(file_name):
    pass
