print("Привет! Я бот Fitlife. Давай познакомимся.")

user_name = input("Как тебя зовут?")
user_age = int(input("Сколько тебе лет?"))
user_weight = float(input("Введи свой вес в кг (например,75.5)"))
user_height = float(input("Введи свой рост в метрах (например,1.80)"))

# --- Расчет индекса массы тела ---
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)
water_ml = user_weight * 30
water_l = round(water_ml / 1000, 1)
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
