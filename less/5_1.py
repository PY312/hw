ru_en = {'монета': 'money',
         'красный': 'red',
         'кружка': "cup"}
ru_kg = {'монета': "тыйын",
         'красный':'кызыл',
         'нож':'бычак'}
kg_ru = {'акча':'деньги',
         'тамак': 'еда',
         'бала':'мальчик'}
kg_en = {'акча': 'money',
         'тамак': 'food',
         'эркек':'man'}
en_ru = {'money':'деньги',
         'red':'красный',
         'key':'ключ'}
en_kg = {'money': 'акча',
         'red': 'кызыл',
         'girl':'кыз'}

dictionary = ['English', en_kg, 'на кыргызском языке'], \
             ['English', en_ru, 'на русском языке'], \
             ['на кыргызском языке',kg_ru, 'на русском языке'] ,\
             ['на кыргызском языке',kg_en, 'English'], \
             ['на русском языке', ru_en, 'English'],\
             ['на русском языке', ru_kg, 'на кыргызском языке']


while True:
    word = input('Введите слово для перевода :')
    wordHere = False
    for i in dictionary:
        for key in i[1]:
            if key == word:
                wordHere = True
                print("Язык оригинал: " + i[0])
                print("Язык перевода: " + i[2] + '  - '+ i[1][key] )
    if wordHere == False:
        print('Такого слова нет в словаре')
        action = input('Хотите ввести новое слово словарь? Y/N ')
        if action.lower() == 'y':
            lang = input('Выберите язык оригинала en, ru, kg    ')
            if lang == 'en':
                en_ru[word] = input(f'Введите перевод к слову {word} на русском языке ')
                en_kg[word] = input(f'Введите перевод к слову {word} на кыргызском языке ')
            elif lang == 'ru':
                ru_en[word] = input(f'Введите перевод  к слову {word} на английском языке ')
                ru_kg[word] = input(f'Введите перевод к слову {word} на кыргызском языке ')
            elif lang == 'kg':
                kg_ru[word] = input(f'Введите перевод к слову {word} на русском языке ')
                kg_en[word] = input(f'Введите перевод к слову {word} на английском языке ')