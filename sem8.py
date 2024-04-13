
def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a') as file:
        for value in contact.values():
            file.write(value+" ")
        file.write('\n')
    return True


def open_contact():
    title = ['Номер', 'Фамилия', 'Имя', 'Отчество', 'Телефон']
    with open('phonebook.txt', 'r') as file:
        print("\t".join(title) + "\n")
        for id, line in enumerate(file):
            print(id+1, "     ", line)


def find_contact():
    title = ['Номер', 'Фамилия', 'Имя', 'Отчество', 'Телефон']
    s_name = input()
    with open('phonebook.txt', 'r') as file:
        print("\t".join(title) + "\n")
        for id, line in enumerate(file):
            line = line.split()
            if s_name in line:
                print(id+1, "     ", *line)


def condition_find():
    condition = {
        '1': 'имя',
        '2': 'фамилию',
        '3': 'отчество',
        '4': 'номер телефона',
    }
    make = input()
    print('Введите', condition.get(make, -1)+":")


def main():
    isStop = -1
    while isStop != 0:
        print(f"Выберите ваше действие: \n1 Просмотр справочника\n2 Добавить контакт\n3 Найти\n4 Копирование \n5 Удаление \n0 Выход")
        isStop = int(input(">"))
        if isStop == 1:
            open_contact()
        if isStop == 2:
            add_new_contact()
        if isStop == 3:
            print(
                "Поиск контакта: \n1 по имени\n2 по фамилии\n3 по отчеству\n4 по номеру телефона")
            condition_find()
            find_contact()
        if isStop == 4:
            print("Введите порядковый номер контакта который вы хотите перенести в другой файл,\nЕсли контактов несколько, укажите их порядковые номера через пробел")
            copy_contact()
        if isStop == 5:
            print("Введите номер контакта, который нужно удалить")
            delete_contact()
        input("Нажмите Enter чтобы продолжить")


def ask_data():
    s_name = input("Введите фамилию: ")
    f_name = input("Введите имя: ")
    m_name = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")

    contact = {
        'second_name': s_name,
        'first_name': f_name,
        'middle_name': m_name,
        'phone_number': phone
    }
    return contact

def copy_contact():
    number=list(map(int, input().split()))
    with open('phonebook.txt') as source, open('my_file.txt', 'w') as destination:
        for id, line in enumerate(source):
            if (id+1) in number:
                destination.write(line)
    print('Контакты скопированы в my_file.txt')

def delete_contact():
    number=list(map(int, input().split()))
    with open('phonebook.txt','r') as source:
        lines = source.readlines()
    with open('phonebook.txt', 'w') as new_sourse:
        for id, line in enumerate(lines):
            if (id+1) not in number:
                new_sourse.write(line)
    print('Контакты удалены') 


main()

