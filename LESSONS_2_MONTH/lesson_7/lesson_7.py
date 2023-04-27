import re

text = 'AV Analytics Vidhya AV'

result = re.match(r'AV', text)
# print(result)


result = re.match(r'Analytics', text)
# print(result)


result = re.search(r'Analytics', text)
# print(result)


result = re.findall(r'AV', text)
# print(result)


result = re.findall(r'A[a-zA-Z]', text)
# print(result)


result = re.split(r' ', text)
# print(result)


result = re.sub(r' ', ':', text)
# print(result)


result = re.sub(r'[Aai]', 'hello', text)
# print(result)

# (0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(1[0-9]{3}|20[0-2][0-9])

with open('lesson_6/test_regs.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content)

    beeline_list = re.findall(r"\+996 (?:77\d|22\d)[ \d]{9}", content)
    print(beeline_list)

    megacom_list = re.findall(r"\+996 (?:55\d|99\d|75\d)[ \d]{9}", content)
    print(megacom_list)

    nur_telecom_list = re.findall(r"\+996 (?:50\d|70\d)[ \d]{9}", content)
    print(nur_telecom_list)

    fruit_list = re.findall(r'fruits\[\d+\] = [а-я"";]+', content)
    for fruit in fruit_list:
        print(fruit)

#     for line in f:
#         full_name, email, file_name, color = line.strip().split(',')
#         data_obj = Data(full_name, email, file_name, color)
#         data_list.append(data_obj)
# # 4. Затем через цикл пройтись по каждому объекту и записать в 4 разных файла все типы информации. (1й файл: Имена с фамилиями, 2й файл: почта, 3й файл: названия файлов с расширением, 4й файл: коды цветов)
#     # print(list)
# # записываем данные в разные файлы
# with open('full_names.txt', 'w') as f1, 

#      open('emails.txt', 'w') as f2, \
#      open('file_names.txt', 'w') as f3, \
#      open('colors.txt', 'w') as f4:
#     for data_obj in data_list:
#         # записываем полное имя в файл full_names.txt
#         f1.write(data_obj.full_name + '\n')
        
#         # записываем почту в файл emails.txt
#         f2.write(data_obj.email + '\n')
        
#         # записываем название файла с расширением в файл file_names.txt
#         f3.write(data_obj.file_name + '\n')
        
#         # записываем код цвета в файл colors.txt
#         f4.write(data_obj.color + '\n')
# print(data_list)