with open("items.txt", "r", encoding="utf-8") as file:
	items = file.read().splitlines()

pistols = 0
shotgun = 0
machine_gun = 0
aromor = 0
madkit = 0

for item in items:
	if item == "пистолетные":
		pistols += 1
	elif item == "ружейные":
		shotgun += 1
	elif item == "автоматные":
		machine_gun += 1
	elif item == "броня":
		aromor += 1
	elif item == "аптечка":
		madkit += 1
	else: 
		print("Нет такого предмета")

items_total = len(items)

print("пистолетные:", pistols, pistols * 100 / items_total, "%")
print("автоматные:", machine_gun, machine_gun * 100 / items_total, "%")
print("ружейные:", shotgun, shotgun * 100 / items_total, "%")
print("броня:", aromor, aromor * 100 / items_total, "%")
print("аптечка:", madkit, madkit * 100 / items_total, "%")
