from decorators import add_exclamation

@add_exclamation
def format_message(text: str) -> str:
    return text.strip()

@add_exclamation
def get_greeting(name: str) -> str:
    return f"Привіт, {name}"


if __name__ == "__main__":
    msg1 = format_message("Лабораторна робота успішно виконана")
    print(msg1)

    msg2 = format_message("Увага!")
    print(msg2)

    msg3 = get_greeting("Дмитро")
    print(msg3)
