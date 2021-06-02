#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
import json

results = [{}, {}]

with open("my_file7.txt") as fhs:
    lines = fhs.readlines()

for line in lines:
    name, _, proceeds, expenses = line.split()
    results[0][name] = int(proceeds) - int(expenses)

results[1]['average_profit'] = round(sum(profit for _, profit in results[0].items() if profit > 0) / len(results[0]))

with open("my_file7.json", "w") as fhd:
    fhd.write(json.dumps(results))
