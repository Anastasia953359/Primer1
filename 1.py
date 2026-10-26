import random
from timer_module import GuessTimer


def get_hint(secret, guess, prev_guess):

    if guess < secret:
        direction = "Больше"
    elif guess > secret:
        direction = "Меньше"
    else:
        return "Угадал!", True

    distance = abs(secret - guess)
    if distance <= 5:
        temp = "Горячо"
    elif distance <= 15:
        temp = "Тепло"
    else:
        temp = "Холодно"

    # Сравнение с предыдущей попыткой
    if prev_guess is not None:
        prev_distance = abs(secret - prev_guess)
        if distance < prev_distance:
            trend = " Теплее"
        elif distance > prev_distance:
            trend = " Холоднее"
        else:
            trend = ""
    else:
        trend = ""

    return f"{direction}, {temp}{trend}", False


def user_guesses():
    """Пользователь угадывает число, загаданное компьютером."""
    print("\nУгадывает пользователь")
    low, high = 1, 100
    secret = random.randint(low, high)
    print(f"Компьютер загадал число от {low} до {high}.")

    timer = GuessTimer()
    timer.start()

    attempts = 0
    prev_guess = None
    while True:
        try:
            guess = int(input("Твой вариант: "))
        except ValueError:
            print("Введи целое число!")
            continue

        attempts += 1
        hint, success = get_hint(secret, guess, prev_guess)
        print(hint)

        if success:
            elapsed = timer.stop()
            print(f"\nПопыток: {attempts}")
            print(f"Время угадывания: {GuessTimer.format_time(elapsed)}")
            break

        prev_guess = guess


def computer_guesses():
    """Компьютер угадывает число, загаданное пользователем (бинарный поиск)."""
    print("\n=== Режим: Угадывает компьютер ===")
    low, high = 1, 100
    print(f"Загадай число от {low} до {high} (не говори его мне!).")
    input("Нажми Enter, когда будешь готов... ")

    timer = GuessTimer()
    timer.start()

    attempts = 0
    prev_guess = None
    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"\nПопытка {attempts}: я думаю, это {guess}")

        while True:
            answer = input("Это (б)ольше, (м)еньше или (у)гадал? ").strip().lower()
            if answer in ("б", "больше", ">"):
                low = guess + 1
                break
            elif answer in ("м", "меньше", "<"):
                high = guess - 1
                break
            elif answer in ("у", "угадал", "="):
                elapsed = timer.stop()
                print(f"\n🎯 Ура! Я угадал число {guess}!")
                print(f"Попыток: {attempts}")
                print(f"Время угадывания: {GuessTimer.format_time(elapsed)}")
                return
            else:
                print("Не понял. Введи 'б', 'м' или 'у'.")

        # (подсказка по «температуре» не нужна компьютеру — он и так сужает диапазон)

    print("Хм, ты, кажется, где-то ошибся с подсказками 😅")


def main():
    print("=" * 40)
    print("        ИГРА «УГАДАЙКА»")
    print("=" * 40)

    while True:
        print("\nВыбери режим:")
        print("1 — Я угадываю число компьютера")
        print("2 — Компьютер угадывает моё число")
        print("0 — Выход")
        choice = input("Твой выбор: ").strip()

        if choice == "1":
            user_guesses()
        elif choice == "2":
            computer_guesses()
        elif choice == "0":
            print("Пока!")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()