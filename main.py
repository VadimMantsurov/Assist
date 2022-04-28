def command():
    return input("Введите команду: \n Привет \n Пока \n вычислить \n будильник \n погода \n")

def do_this_command(message):
    message = message.lower()

    if "Привет" in message:
        say_message ("Привет друг")
    elif "Пока" in message:
        say_message("Пока")
        exit()

    elif "будильник" in message:
        import alarm

    elif "вычислить" in message:
        say_going= input("Введите действие: \n построить график функции \n преобразование функции \n")
        say_going = say_going.lower()

        if "построить график функции" in say_going:
            import Fun
        elif "преобразование функции" in say_going:
            import Fun_convert

    elif "погода" in message:
        import Weather

    else:
        say_message("Unknown command")

def say_message(message):

    print(message)
if __name__ == "__main__":
    while True:
        command = command()
        do_this_command(command)