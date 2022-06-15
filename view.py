# Основная логика программы
import const
import settings as st
import controller as c


def init():  # Приветствие, и загрузка данных
    c.load_phone_book()


def help():
    print('Обрабатываются следующие команды:')
    print('\t /help - вывод помощи')
    print('\t /info - вывод информации о программе')
    print('\t /exit или /quit - выход из программы')
    print('\t /add  - добавить запись')
    print('\t /edit {num} - редактировать запись {num}')
    print('\t /del {num} - удалить запись {num}')
    print(
        '\t /export {num}- экспорт телефонной книги (всей или записи  {num})')
    print('\t /import - import телефонной книги')


def info():
    print('Программа для учета телефонных номеров.')
    print('Выполнена в качестве командного домашнего задания')
    print('Коллективом из 4-х человек')


def print_line(sym='-', counts=70, clr_sym=const.CYAN_CLR_SYM):
    print("{}{}{}".format(
        clr_sym[0], sym * counts, clr_sym[1]))


def print_clr_text(clr_sym: list, text):
    print("{} {} {}".format(clr_sym[0], text, clr_sym[1]))


def show_title():
    print_line('=')
    print_clr_text(const.GREEN_CLR_SYM, "\t\tТелефонная книга")
    print_line()
    print("{} {:5}{:15}{:10}{:12}{:20} {}".format(const.GREEN_CLR_SYM[0],
                                                  '#', 'Фамилия', 'Имя', 'Номер', 'Описание', const.GREEN_CLR_SYM[1]))
    print_line()


def show_footer():
    print("Действия: /help-[Доступные команды] /info-[Инфо] /exit-[Выйти]")


def show_phone_book():  # Выводим на экран всю базу
    show_title()
    for i, item in enumerate(c.phone_book()):
        print("{:<5}{:15}{:10}{:12}{:20}".format(
            i+1, item.second_name, item.first_name, item.phone_num, item.description))
    print_line()
    show_footer()
    print_line('=')


def get_input(message: str, required=False) -> str:
    if not required:
        return input(message)
    else:
        res = ""
        while res == "":
            res = get_input(f"{message}: ")
            if res == "":
                print(f"{message} не может быть пустым")
        return res


def get_record_data() -> list:
    data = []
    print("Введите данные:")
    first_name = get_input("Имя", required=True)
    data.append(first_name)

    second_name = get_input("Фамилия: ")
    data.append(second_name)

    description = get_input("Описание: ")
    data.append(description)

    phone_num = get_input("Телефон", required=True)
    data.append(phone_num)
    return data


def get_edit_data(id: int) -> list:
    data = []
    prev_data = c.get_record_data(id)
    print("Укажите новые данные (если хотите оставить старые, нажмите 'Enter'):")
    first_name = get_input(f"Имя ({prev_data[0]}): ")
    data.append(first_name or prev_data[0])

    second_name = get_input(f"Фамилия ({prev_data[1]}): ")
    data.append(second_name or prev_data[1])

    descriptioin = get_input(f"Описание ({prev_data[2]}): ")
    data.append(descriptioin or prev_data[2])

    phone_num = get_input(f"Телефон ({prev_data[3]}): ")
    data.append(phone_num or prev_data[3])
    return data


def get_edit_id(input: str) -> int:  # Возвращаем номер записи к редактированию
    input = input.split()
    return int(input[1]) - 1 if len(input) > 1 else -1


def run_app():  # Главный цикл

    init()  # Считываем всю базу из файла

    while True:
        show_phone_book()
        inp = input('>>> ')

        if inp.lower() == "/help":
            help()
        elif inp.lower() == "/info":
            info()
        elif inp.lower() == "/exit" or inp.lower() == "/quit":
            c.save_phone_book(c.phone_book())
            print_clr_text(const.YELLOW_CLR_SYM, 'Выход из программы.')
            break
        elif inp.lower() == "/add":
            record_data = get_record_data()
            c.create_record(record_data)
        elif inp.lower().startswith("/edit"):
            rec_id = get_edit_id(inp.lower())
            if rec_id == -1:
                print("Укажите номер записи для редактирования")
            else:
                if rec_id not in range(len(c.phone_book())):
                    print_clr_text(const.RED_CLR_SYM, "Такой записи нет")
                else:
                    edit_data = get_edit_data(rec_id)
                    c.change_record(rec_id, edit_data)
        elif inp.lower().startswith("/del"):
            rec_id = get_edit_id(inp.lower())
            if rec_id == -1:
                print_clr_text(const.YELLOW_CLR_SYM,
                               "Укажите номер записи для удаления")
            else:
                if rec_id not in range(len(c.phone_book())):
                    print_clr_text(const.RED_CLR_SYM, "Такой записи нет")
                else:
                    c.delete_record(rec_id)
        elif inp.lower().startswith("/export"):
            rec_id = get_edit_id(inp.lower())
            if rec_id == -1:
                format = int(get_input(
                    "В каком формате сохранить? (1 - 'JSON', 2 - 'CSV'): "))
                card_format = const.CardFormat(format)
                export_file = st.EXPORT_FILE + '.' + card_format.name.lower()
                c.export_phone_book(export_file, card_format)
                msg = 'Книга экспортирована в файл {}'.format(export_file)
                print_clr_text(const.YELLOW_CLR_SYM, msg)
            else:
                if rec_id not in range(len(c.phone_book())):
                    print_clr_text(const.RED_CLR_SYM, "Такой записи нет")
                else:
                    format = int(get_input(
                        "В каком формате сохранить? (1 - 'JSON', 2 - 'CSV'): "))
                    card_format = const.CardFormat(format)
                    export_file = st.EXPORT_FILE + '_' + \
                        c.get_record_data(rec_id)[
                            0] + '.' + card_format.name.lower()
                    c.export_record(export_file, rec_id, card_format)
                    msg = 'Запись экспортирована в файл {}'.format(export_file)
                    print_clr_text(const.YELLOW_CLR_SYM, msg)
        elif inp.lower() == "/import":
            import_file = get_input("Укажите файл для импорта", required=True)
            c.import_records(import_file)
        else:
            print_clr_text(const.RED_CLR_SYM,
                           'Неверная команда. Для помощи наберите /help')
