i = 1
prod = []
name_list = []
price_list = []
quantity_list = []
unit_list = []
x = "1"
while x == "1" or x == "2":
    x = input("\nввод данных - 1; \nпоказать аналитику - 2; \nвыход - любая клавиша\n")
    if x == "1":
        name_product = input("Наименование товара: ")
        price = input("Цена товара: ")
        quantity = input("Количество: ")
        unit = input("Единицы измерения: ")
        prod.append((i, {"Название": name_product, "Цена": price, "Количество": quantity, "Ед": unit}))
        print("\n", prod)
        name_list.append(name_product)
        price_list.append(price)
        quantity_list.append(quantity)
        unit_list.append(unit)
        i += 1
    elif x == "2":
        print({"Название": name_list, "Цена": price_list, "Количество": quantity_list, "Ед": unit_list})
    else:
        break
