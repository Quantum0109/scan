# запрещенные предметы: нож, бензин, граната, пистолет

"""
Пассажиров на проверке: 5

Пассажир Питонов Василий Аспидович допущен к вылету

Пассажир Блинохватов Прохор Аскольдович допущен к вылету

В ручной клади пассажира Бабахин Капитон Кондратьевич обнаружен запрещенный предмет граната . Пассажир не допущен к вылету.

Пассажир Бескровная Таисия Ипатовна допущен к вылету

Пассажир Аскетов Демьян Захарьевич допущен к вылету


Допущено к вылету пассажиров: 4

место : 0
имя : Питонов Василий Аспидович
проверен : True
ручная кладь : ['ноутбук', 'наушники']

место : 1
имя : Блинохватов Прохор Аскольдович
проверен : True
ручная кладь : ['книга', 'четки', 'беруши']

место : 3
имя : Бескровная Таисия Ипатовна
проверен : True
ручная кладь : ['журнал', 'букет', 'горсть земли']

место : 4
имя : Аскетов Демьян Захарьевич
проверен : True
ручная кладь : []
"""

danger_item = ["нож", "бензин", "граната", "пистолет"]
passengers = [
    {
        "место": 0,
        "имя": "Питонов Василий Аспидович",
        "проверен": False,
        "ручная кладь": ["ноутбук", "наушники"]
    },
    {
        "место": 1,
        "имя": "Блинохватов Прохор Аскольдович",
        "проверен": False,
        "ручная кладь": ["книга", "четки", "беруши"]
    },
    {
        "место": 2,
        "имя": "Бабахин Капитон Кондратьевич",
        "проверен": False,
        "ручная кладь": ["семечки", "граната", "кепка"]
    },
    {
        "место": 3,
        "имя": "Бескровная Таисия Ипатовна",
        "проверен": False,
        "ручная кладь": ["журнал", "букет", "горсть земли"]
    },
    {
        "место": 4,
        "имя": "Аскетов Демьян Захарьевич",
        "проверен": False,
        "ручная кладь": []
    }
]
accepted = []
print(f"{len(passengers)} пассажиров в очереде на проверку")
for passenger in passengers:
    for item in passenger["ручная кладь"]:
        if item in danger_item:
            print ("спалися", item, passenger["имя"])
            break
    else:
        print("допущен")
        accepted.append(passenger)
print(accepted)
