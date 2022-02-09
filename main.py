import re
import csv
with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
phone_r = r"(8|\+7)\s*\(?(\d+)\)?(\s|-)?(\d{3})(\s+|-)?(\d{2})(\s+|-)?(\d{2})(\s\(?(доб.)\)?\s(\d+)\)?)?"
change_phone = r"+7(\2)\4-\6-\8 \10\11"

#'это я упражналась, как свести имя и фамилию через RegEx. На regex101.com оно работает,
# но я не придумала, как это использовать в решении задания.
# names = r"([А-Я]\w+)(,|\s)([А-Я]\w+)(,|\s)([А-Я]\w+)?"
# change_names = r"\1,\3,\5"

check_dublicate ={}
new_contacts_list = []
for number, el in enumerate(contacts_list):
    el[5] = re.sub(phone_r, change_phone, el[5]).strip()
    name = (' ').join(el[0:3]).split(' ')
    el[0], el[1], el[2] = name[0], name[1], name[2]
    if not check_dublicate.get(el[0]+el[1]):
        check_dublicate[el[0]+el[1]] = number
    else:
          i = check_dublicate[el[0]+el[1]]
          el1 = contacts_list[i]
          t = zip(el, el1)
          el = list(map(lambda x: x[0] if x[0] else x[1] , t))
          new_contacts_list[i] = []
    new_contacts_list.append(el)

new_contacts_list = [el for el in new_contacts_list if el]

# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding='UTF-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contacts_list)