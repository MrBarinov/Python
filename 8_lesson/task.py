from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Телефонная книга:\n"
                        "1. Показать данные\n"
                        "2. Добавить запись\n"
                        "3. наути запись\n"
                        "4. Выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_rec()
            case "3":
                pass
            case "4":
                play = False
            case _:
                print("Try again!\n")


def read_records():
    global all_data, id
    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        return all_data


def show_all():
    if not all_data:
        print("Данных нет")
    else:
        print(*read_records(), sep="\n")

def add_rec():
    global id
    array = ['Фамилия','Имя','Отчество','Телефон']
    string = ''
    for  i in array:
        string += input(f"enter {i} ") + " "
    id += 1
    # print(f'{id} {string}')

    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f'{id} {string}\n')

main_menu()