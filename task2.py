import csv


def get_data():
    file_list = ["info_1.txt", 'info_2.txt', 'info_3.txt']

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
                 ]
    num = 1
    for file in file_list:

        with open(file, "r", encoding='cp1251') as f:

            for line in f:

                if "Изготовитель системы" in line:
                    os_prod_list.append(add_name(line))
                if "Название ОС" in line:
                    os_name_list.append(add_name(line))
                if "Код продукта" in line:
                    os_code_list.append(add_name(line))
                if "Тип системы" in line:
                    os_type_list.append(add_name(line))
                    
    for i in range(len(os_type_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data


def add_name(line):
    return ''.join(
        line.split()[2:])


def write_to_csv(file_name):
    with open('export.csv', 'w') as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        f_writer.writerows(get_data())


write_to_csv('export.csv')
