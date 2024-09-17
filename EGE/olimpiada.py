# import csv
# count = 0
#
# # f = open("C:/Users/OLEG/Desktop/Points.csv" , "r")
# # reader = csv.DictReader(f, delimiter=';', quotechar='"')
#
# def create_answer_dict(csv_filename):
#     with open(csv_filename, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Пропускаем заголовок
#         answer = {int(rows[0]): rows[1] for rows in reader}
#     return answer
#
# answer = create_answer_dict('C:/Users/OLEG/Desktop/Points.csv')
#
# message = input()
# def check_answer(message):
#     try:
#         task_num, user_answer = map(int, message.text.split(')'))
#     except ValueError:
#         print(message, "Неправильный формат ввода. Введите номер задания, затем ')', затем ответ.")
#         return
#
#     if task_num in answer:
#         if str(user_answer) == answer[task_num]:
#             print(message, f"Задание {task_num} - Правильно.")
#         else:
#             print(message, f"Задание {task_num} - Не правильно.")
#     else:
#         print(message, f"Задание с номером {task_num} не найдено.")


# count = 0
# number = "1"
# otvet = "3"
#
# i = input()
# m, n = i.split(")")
#
# if m == number:
#     if n == otvet:
#         count += 1
#         print ("правильно")
#     else:
#         print ("не правильно")
#     print (str(count) + " баллов набрано")


import telebot
import csv

# Создаем телеграм бота
bot = telebot.TeleBot('ВАШ_ТОКЕН')


# Создаём словарь из CSV файла.
# Мы предполагаем, что в файле в первой колонке номера вопросов, во второй - ответы.
def create_answer_dict(csv_filename):
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок
        answers = {int(rows[0]): rows[1] for rows in reader}
    return answers


# Создаем словарь ответов
answers = create_answer_dict('db.csv')  # Подставьте правильное имя файла CSV


# Добавляем обработчик сообщений
@bot.message_handler(content_types=['text'])
def check_answer(message):
    try:
        task_num, user_answer = map(int, message.text.split(')'))
    except ValueError:
        bot.reply_to(message, "Неправильный формат ввода. Введите номер задания, затем ')', затем ответ.")
        return

    if task_num in answers:
        if str(user_answer) == answers[task_num]:
            bot.reply_to(message, f"Задание {task_num} - Правильно.")
        else:
            bot.reply_to(message, f"Задание {task_num} - Не правильно.")
    else:
        bot.reply_to(message, f"Задание с номером {task_num} не найдено.")


# Запускаем бота
bot.polling()