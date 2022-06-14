import const
import model.phone_item as phi
import model.phone_book as phb
import io_module as bd
import export_json as exp_json
import export_csv as exp_csv


def phone_book() -> list:
    return phb.phone_book


def load_phone_book():
    phone_book = [phi.create_record(name, surname, descr, num) for (
        name, surname, descr, num) in bd.load_db()]
    phb.init(phone_book)


def save_phone_book(data: list):
    bd.save_db(data)


def export_phone_book(format: const.CardFormat):

    if format == const.CardFormat.JSON:
        exp_file = exp_json.export(phone_book())
    elif format == const.CardFormat.CSV:
        exp_file = exp_csv.export(phone_book())
    else:
        print("Неизвестный формат")
    return exp_file


def export_record(id: int, format: const.CardFormat):
    if format == const.CardFormat.JSON:
        exp_file = exp_json.export_record(phb.get_record(id))
    elif format == const.CardFormat.CSV:
        exp_file = exp_csv.export_record(phb.get_record(id))
    else:
        print("Неизвестный формат")
    return exp_file


def import_records(file_name: str):
    dot_idx = file_name.find('.')
    if dot_idx == -1:
        print("Неизвестный формат")
        return

    ext = file_name[dot_idx + 1:].lower()
    if ext == 'json':
        format = const.CardFormat.JSON
        exp_json.import_records(file_name)
        print('Записи импортированы в формате {}'.format(format))
    elif ext == 'csv':
        format = const.CardFormat.CSV
        exp_csv.import_records(file_name)
        print('Записи импортированы в формате {}'.format(format))
    else:
        print("неизвестный формат - {}".format(ext))


def create_record(record_data: list):
    item = phi.create_record(*record_data)
    phb.add_record(item)


def delete_record(id: int):
    phb.del_record(id)


def change_record(id: int, record_data: list):
    phb.edit_record(id, *record_data)


def get_record_data(id: int) -> list:
    return [val for val in phb.get_record(id)]
