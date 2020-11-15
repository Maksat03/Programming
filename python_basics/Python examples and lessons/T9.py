from fuzzywuzzy import fuzz # для нечеткого сравнение
import datetime # для работы с даты
start_time = datetime.datetime.now() # переменная start_time тен программа басталгандагы уакытка
print(start_time.second) # выводить секунд переменного start_time
with open("litb-win.txt", "r") as words: # открыть litb-win.txt(словарьный состав слов) в режиме "r" читение как words
	words_read = words.read() # читаем файл(words)
	words_split = words_read.split() # разбить все слова в папке words
	words = words_split # переменная words равен на разбитое слова в файле(words)
	del words[1::2] # удалить каждую слова начиная с 2 слова и до последного слова по 2 шагам в списке(words)
a, b, v, g, d, e, jj, z, ii, k, l, m, n, p, o, r, s, t, y, f, h, c, ji, zh, ll, yi, ey, iy, ia = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] # бастапкы арыптерыне сайкес басталатын создерды сактауга арналган списка
dict_start_name = "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "п", "о", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ы", "ъ", "ь", "э", "ю", "я" # ар создын бас арыптеры
vocabulary = { "а": a, "б": b, "в": v, "г": g, "д": d, "е": e, "ё": e, "ж": jj, "з": z, "и": ii, "й": ii, "к": k, "л": l, "м": m, "н": n, "п": p, "о": o, "р": r, "с": s, "т": t, "у": y, "ф": f, "х": h, "ц": c, "ч": ji, "ш": zh, "щ": zh, "ы": yi, "ъ": ll, "ь": ll, "э": ey, "ю": iy, "я": ia } # ар арыптын басталу бойынша сакталатын создер жиыны
# ар создын бас арыптерыне сай басталатын создерды болек болек сактап кою  
for i in range(len(words)):
	for j in range(len(dict_start_name)):
		if words[i].startswith(dict_start_name[j]):
			vocabulary[dict_start_name[j]].append(words[i])
fixed_words = "" # жондетылген сойлем/создер(fixed_words) деп переменная куру чтобы кейын осыган барлык дурыс создерды тенестыретын
text = "варавр, арпмлпрл, уаыацукрваравр, арпмлпрл, уаыацукрваравр, арпмлпрл, уаыацукрваравр, арпмлпрл, уаыацукрваравр, арпмлпрл, уаыацукр" # сойлем для тестирование
text = text.split()  # разбить все слова для тестирование
err_words = []  # списка для хранение ошибочных слов
err_index = []  # списка для хранение индексов ошибочного слова

for i in range(len(text)):
	try: # пытаемся найти соответственного слова в словарном составе
		words.index(text[i])  #  ищем индекс соответственного слова
	except: # если есть ошибка
		err_index.append(i) # добавляем индекс ошибочного слова
		err_words.append(text[i])  # добавляем ошибочного слова
		print('Не найдена: ' + str(text[i])) # выводим на экран ошибочного слова
if len(err_words) != 0: # если количество ошибочных слов в списке не равен 0 ...
	ratio_values = [] # сай келген создердын значениеларын сактауга арналган переменная
	for i in range(len(err_words)):
		for j in range(len(dict_start_name)):
			if err_words[i].startswith(dict_start_name[j]):
				for k in range(len(vocabulary[dict_start_name[j]])):
					ratio_value = fuzz.ratio(err_words[i], vocabulary[dict_start_name[j]][k]) # сравневаем слова
					ratio_values.append(ratio_value) # добавляем значение сравнненого слова
				ratio_max_value = max(ratio_values)  # ищем самую высокую значению
				word_index = int(ratio_values.index(ratio_max_value)) # ищем индекс самого высокого значение
				fixed_word = vocabulary[dict_start_name[j]][word_index]  # исправленная слова соответственного индекса на индекс высокого значение
				print("Исправленное слово: " + str(fixed_word)) # выводим на экране
				err_words[i] = fixed_word # исправляем ошибочного слова
				fixed_variants = [] # списка для хранение варианттов исправленного слова
				for m in range(3):
					ratio_max_value = max(ratio_values) # ищем самую высокую значению
					word_index = int(ratio_values.index(ratio_max_value)) # ищем индекс самого высокого значение
					fixed_word = vocabulary[dict_start_name[j]][word_index] # исправленная слова соответственного индекса на индекс высокого значение
					fixed_variants.append(fixed_word) # добавляем слова в вариантты исправленного слова
					ratio_values.remove(ratio_max_value) # удаляем самую высокую значение значит следущий раз будет другое слова как так удалям самую высокую значение будет другое высокое значение
				print("Вариантты: " + str(fixed_variants[0]) + " ,    " + str(fixed_variants[1]) + " ,    " + str(fixed_variants[2]) + " ;") # выводим на экран вариантты исправленного слова
				ratio_values = []  # сай келген создердын значениеларын сактауга арналган переменнаяны босатып басынан куру
		text[err_index[i]] = err_words[i] # тестировкага арналган создын ышындегы кате созды жондеймыз
	for i in range(len(text)):
		fixed_words += text[i] + " " # жонделген сойлем/создер(fixed_words) деген переменная тен болады дурыс создерге/сойлемге 
	print("Исправленное приложение: " + str(fixed_words)) # дурыс создерды/сойлемды экранга шыгару 
end_time = datetime.datetime.now() # переменная end_time тен программа аякталганга уакытка
print(end_time.second) # программа быткендегы секундтарды экранга шыгару