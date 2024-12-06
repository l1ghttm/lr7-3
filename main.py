import json

operations_count = 0

while True:
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")

    choice = input("Введите номер пункта: ")

    if choice == '1':
        with open('flowers.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print("\nВсе записи:")
            for entry in data:
                print(json.dumps(entry, ensure_ascii=False, indent=4))
        operations_count += 1

    elif choice == '2':
        id = int(input("Введите ID записи: "))
        with open('flowers.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            found = False
            for index, entry in enumerate(data):
                if entry['id'] == id:
                    print(f"\nЗапись найдена (позиция {index}):")
                    print(json.dumps(entry, ensure_ascii=False, indent=4))
                    found = True
                    break
            if not found:
                print("Запись не найдена")
        operations_count += 1

    elif choice == '3':
        new_entry = {
            "id": int(input("Введите ID: ")),
            "name": input("Введите общее название цветка: "),
            "latin_name": input("Введите латинское название цветка: "),
            "is_red_book_flower": input("Является ли цветок краснокнижным? (true/false): ").lower() == 'true',
            "price": float(input("Введите стоимость цветка: "))
        }
        with open('flowers.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            data.append(new_entry)
        with open('flowers.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Запись добавлена")
        operations_count += 1

    elif choice == '4':
        id = int(input("Введите ID записи для удаления: "))
        with open('flowers.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            found = False
            for index, entry in enumerate(data):
                if entry['id'] == id:
                    del data[index]
                    found = True
                    break
            if found:
                with open('flowers.json', 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                print("Запись удалена")
            else:
                print("Запись не найдена")
        operations_count += 1

    elif choice == '5':
        print(f"Количество выполненных операций: {operations_count}")
        break

    else:
        print("Неправильный ввод, попробуйте снова")
