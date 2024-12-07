import json

operations_count = 0

def display_menu():
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по ID")
    print("3. Добавить запись")
    print("4. Удалить запись по ID")
    print("5. Выйти из программы")

def load_data(filename='flowers.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data, filename='flowers.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def display_all_records():
    data = load_data()
    print("\nВсе записи:")
    for entry in data:
        print(json.dumps(entry, ensure_ascii=False, indent=4))
    global operations_count
    operations_count += 1

def display_record_by_id():
    data = load_data()
    try:
        id = int(input("Введите ID записи: "))
    except ValueError:
        print("Неверный формат ID. Попробуйте снова.")
        return

    found = False
    for index, entry in enumerate(data):
        if entry['id'] == id:
            print(f"\nЗапись найдена (позиция {index}):")
            print(json.dumps(entry, ensure_ascii=False, indent=4))
            found = True
            break

    if not found:
        print("Запись не найдена")
    global operations_count
    operations_count += 1

def add_record():
    try:
        new_entry = {
            "id": int(input("Введите ID: ")),
            "name": input("Введите общее название цветка: "),
            "latin_name": input("Введите латинское название цветка: "),
            "is_red_book_flower": input("Является ли цветок краснокнижным? (true/false): ").lower() == 'true',
            "price": float(input("Введите стоимость цветка: "))
        }
    except ValueError:
        print("Неверный формат данных. Попробуйте снова.")
        return

    data = load_data()
    data.append(new_entry)
    save_data(data)
    print("Запись добавлена")
    global operations_count
    operations_count += 1

def delete_record_by_id():
    data = load_data()
    try:
        id = int(input("Введите ID записи для удаления: "))
    except ValueError:
        print("Неверный формат ID. Попробуйте снова.")
        return

    found = False
    for index, entry in enumerate(data):
        if entry['id'] == id:
            del data[index]
            found = True
            break

    if found:
        save_data(data)
        print("Запись удалена")
    else:
        print("Запись не найдена")
    global operations_count
    operations_count += 1

while True:
    display_menu()
    choice = input("Введите номер пункта: ")

    if choice == '1':
        display_all_records()
    elif choice == '2':
        display_record_by_id()
    elif choice == '3':
        add_record()
    elif choice == '4':
        delete_record_by_id()
    elif choice == '5':
        print(f"Количество выполненных операций: {operations_count}")
        break
    else:
        print("Неправильный ввод, попробуйте снова")
