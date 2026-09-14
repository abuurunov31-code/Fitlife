# Константы
WATER_PER_KG_ML = 30
ML_IN_LITER = 1000
print("Привет! Я бот Fitlife. Давай познакомимся.")

user_name = input("Как тебя зовут?")

while True:
    try:
        user_age = int(input("Сколько тебе лет?"))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите целое число.")

while True:
    try:
        user_weight = float(input("Введи свой вес в кг (например,75.5): "))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите число.")

while True:
    try:
        user_height = float(
            input("Введи свой рост в метрах (например, 1.80): ")
        )
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите число.")
# --- Расчет индекса массы тела ---
bmi = round(user_weight / (user_height ** 2), 1)
water_l = round((user_weight * WATER_PER_KG_ML) / ML_IN_LITER, 1)
# --- Определение категории ИМТ ---
if bmi < 18.5:
    bmi_category = "Недостаточная масса тела"
elif 18.5 <= bmi < 25:
    bmi_category = "Нормальный вес"
elif 25 <= bmi < 30:
    bmi_category = "Избыточная масса тела"
else:
    bmi_category = "Ожирение"

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"\nТвой индекс массы тела: {bmi} {bmi_category}")
print(f"\nРекомендуемая норма воды в день: {water_l} л.")
print(f"\nРасчет окончен. Будьте здоровы, {user_name}")
