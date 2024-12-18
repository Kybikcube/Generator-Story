import random

templates = [
    "Однажды [существительное] [глагол] в [место], где [существительное] [глагол] [прилагательное] [существительное].",
    "В далекой-далекой галактике [существительное] [глагол] [прилагательное] [существительное], чтобы [глагол] [существительное].",
    "Детектив [имя] расследует загадочное исчезновение [существительное], которое, возможно, связано с [прилагательное] [существительное].",
    "В мире, где [прилагательное] [существительное] [глагол] [прилагательное] [существительное], [имя] должен [глагол] [существительное].",
    "История о том, как [имя] [глагол] [прилагательное] [существительное] и обнаружил, что [существительное] [глагол] [прилагательное] [существительное].",
    "В далеком [время года] [имя] [глагол] [прилагательное] [существительное] и встретил [существительное], которое [глагол] [прилагательное] [существительное].",
    "В мире, где [существительное] [глагол] [прилагательное] [существительное], [имя] должен [глагол] [существительное], чтобы [глагол] [существительное].",
    "Однажды [имя] [глагол] [прилагательное] [существительное] и обнаружил, что [существительное] [глагол] [прилагательное] [существительное].",
    "В далеком [время года] [имя] [глагол] [прилагательное] [существительное] и встретил [существительное], которое [глагол] [прилагательное] [существительное].",
    "В мире, где [существительное] [глагол] [прилагательное] [существительное], [имя] должен [глагол] [существительное], чтобы [глагол] [существительное]."
]

# Списки слов
nouns = ["кот", "пирог", "ракета", "детектив", "пришелец", "машина", "книга", "дерево", "город", "океан"]
verbs = ["прыгал", "танцевал", "исследовал", "съел", "загадал", "летал", "читал", "рисовал", "строил", "плавал"]
adjectives = ["красный", "быстрый", "странный", "огромный", "волшебный", "маленький", "яркий", "темный", "светлый", "холодный"]
places = ["магазин", "парк", "космос", "замок", "лаборатория", "лес", "гора", "пляж", "город", "деревня"]
names = ["Шерлок Холмс", "Доктор Ватсон", "Джейн Марпл", "Эркюль Пуаро", "Агата Кристи", "Гарри Поттер", "Джон Доу", "Лили Эванс", "Роуэн Аткинсон"]
seasons = ["зимой", "весной", "летом", "осенью"]

template = random.choice(templates)

story = template.replace("[существительное]", random.choice(nouns))
story = story.replace("[глагол]", random.choice(verbs))
story = story.replace("[прилагательное]", random.choice(adjectives))
story = story.replace("[место]", random.choice(places))
story = story.replace("[имя]", random.choice(names))
story = story.replace("[время года]", random.choice(seasons))

print(story)