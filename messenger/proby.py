from flask import Flask

messages = [
    {
        "text": "Как дела",
        "sender": "Михаил",
        "time": "19:20"
    },
    {
        "text": "Дела - отлично",
        "sender": "Василий",
        "time": "19:21"
    }
]


def add_message(text, sender):  # Объявим функцию, которая добавит сообщение в список
    new_message = {
        "text": text,
        "sender": sender,
        "time": "23:59"  # ToDO: указать правильное время/дату
    }
    messages.append(new_message)  # Добавляем новое сообщение в список


def print_message(message):  # Объявляем функцию, которая будет печатать одно сообщение
    print(f"[{message['sender']}]: {message['text']} / {message['time']} ")


add_message("а еще долго будет идти?", "Марина")
add_message("Запятую надо убрать ", "Vova")

for message in messages:
    print_message(message)

#  ПЛАН
#  1. Создали внутреннюю возможность хранить сообщения, добавлять новые и читать чат
#  2. Подключить визуальный интерфейс к этим внутренним возможностями
#     - Превратить наш код в веб-сервер. Flask
#     - Создать интерфейс и подключить его к веб-серверу