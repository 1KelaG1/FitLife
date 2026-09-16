import sys

# Принудительно UTF-8 (важно для Windows)
sys.stdout.reconfigure(encoding='utf-8')

# ---------- ЦВЕТА И СТИЛИ (ANSI escape-коды) ----------
# Эти переменные — «ручки» разных цветов. Вставляются в print() через f-строки.
RESET = "\033[0m"      # сброс всех стилей (обычный текст)
BOLD = "\033[1m"       # жирный текст
CYAN = "\033[96m"      # ярко-голубой
GREEN = "\033[92m"     # ярко-зелёный
YELLOW = "\033[93m"    # ярко-жёлтый
MAGENTA = "\033[95m"   # ярко-пурпурный (розовый)
DIM = "\033[2m"        # приглушённый (сероватый)

# ---------- ГОТОВАЯ ЛИНИЯ-РАЗДЕЛИТЕЛЬ ----------
# 50 символов "─" в голубом цвете. Используется много раз ниже.
LINE = f"{CYAN}{'─' * 50}{RESET}"


# ---------- ШАГ 1: ЗАГОЛОВОК И ВВОД ИМЕНИ ----------
print()
print(f"{CYAN}{'═' * 50}{RESET}")  # верхняя двойная линия
print(
    f"{BOLD}{MAGENTA}     📋  АНКЕТА ЗДОРОВЬЯ — ШАГ 1 ИЗ 4{RESET}"
)  # заголовок шага
print(f"{CYAN}{'═' * 50}{RESET}")  # нижняя двойная линия
print(
    f"{DIM}  Подсказка: имя можно вводить в любом регистре{RESET}"
)  # подсказка
print(LINE)  # тонкая линия

# Ввод имени: strip() убирает пробелы по краям, title() делает «Иван» из «иван»
user_name = input(f"{BOLD}{GREEN}  ➤ Ваше имя:{RESET} ").strip().title()


# ---------- ШАГ 2: ВВОД ВОЗРАСТА ----------
print(LINE)
print(f"{BOLD}{MAGENTA}     📋  АНКЕТА ЗДОРОВЬЯ — ШАГ 2 ИЗ 4{RESET}")
print(f"{DIM}  Подсказка: целое число, например 25{RESET}")
print(LINE)

# int() — превращает строку в целое число
user_age = int(input(f"{BOLD}{GREEN}  ➤ Ваш возраст (лет):{RESET} "))


# ---------- ШАГ 3: ВВОД ВЕСА ----------
print(LINE)
print(f"{BOLD}{MAGENTA}     📋  АНКЕТА ЗДОРОВЬЯ — ШАГ 3 ИЗ 4{RESET}")
print(f"{DIM}  Подсказка: можно с точкой, например 70.5{RESET}")
print(LINE)

# float() — превращает строку в число с плавающей точкой
user_weight = float(input(f"{BOLD}{GREEN}  ➤ Ваш вес (кг):{RESET} "))


# ---------- ШАГ 4: ВВОД РОСТА ----------
print(LINE)
print(f"{BOLD}{MAGENTA}     📋  АНКЕТА ЗДОРОВЬЯ — ШАГ 4 ИЗ 4{RESET}")
print(f"{DIM}  Подсказка: в метрах, например 1.75{RESET}")
print(LINE)

# Рост в метрах (важно: не в сантиметрах, иначе формула ИМТ даст чушь)
user_height = float(input(f"{BOLD}{GREEN}  ➤ Ваш рост (м):{RESET} "))


# ---------- ЗАВЕРШЕНИЕ ВВОДА ----------
print(LINE)
print(f"{BOLD}{GREEN}  ✅  Все данные получены! Считаю...{RESET}")
print(LINE)


# ---------- РАСЧЁТЫ ----------
# ИМТ = вес / рост². round(..., 1) — округление до 1 знака после точки.
bmi = round(user_weight / (user_height ** 2), 1)

# Норма воды: 30 мл на 1 кг веса → переводим в литры делением на 1000
water_l = round(user_weight * 30 / 1000, 1)


# ---------- КАТЕГОРИЯ ИМТ ----------
# Определяем, в какую категорию попал ИМТ, и подбираем цветной маркер
if bmi < 18.5:
    bmi_category, bmi_emoji = "Недостаточный вес", "🔵"
elif bmi < 25:
    bmi_category, bmi_emoji = "Норма", "🟢"
elif bmi < 30:
    bmi_category, bmi_emoji = "Избыточный вес", "🟡"
else:
    bmi_category, bmi_emoji = "Ожирение", "🔴"


# ---------- ПРОГРЕСС-БАР ВОДЫ ----------
# Длина шкалы — 30 символов. Условно считаем 3 литра = 100%.
bar_length = 30
# сколько ячеек закрасить
filled = int(min(water_l / 3, 1) * bar_length)
# заполненные + пустые
bar = "█" * filled + "░" * (bar_length - filled)


# ---------- ОТЧЁТ ----------
print()
print(f"{CYAN}{'═' * 50}{RESET}")
print(f"{BOLD}{MAGENTA}        📋  ОТЧЁТ О ЗДОРОВЬЕ  📋{RESET}")
print(f"{CYAN}{'═' * 50}{RESET}")
# имя
print(f"  👤  {BOLD}Пользователь:{RESET}  {user_name}")
# возраст
print(f"  🎂  {BOLD}Возраст:     {RESET}  {user_age} лет")
# вес
print(f"  ⚖️   {BOLD}Вес:         {RESET}  {user_weight} кг")
# рост
print(f"  📏  {BOLD}Рост:        {RESET}  {user_height} м")
# разделитель
print(f"{CYAN}{'─' * 50}{RESET}")
# ИМТ + категория
print(
    f"  {bmi_emoji}  {BOLD}ИМТ:{RESET}          "
    f"{bmi}  ({bmi_category})"
)
# норма воды
print(f"  💧  {BOLD}Норма воды:{RESET}  {water_l} л в день")
# прогресс-бар
print(f"      [{GREEN}{bar}{RESET}]  {water_l} / 3.0 л")
# нижняя линия
print(f"{CYAN}{'═' * 50}{RESET}")
# финал
print(f"{BOLD}{GREEN}  ✅  Расчёт окончен. Будьте здоровы! 💪{RESET}")
print(f"{CYAN}{'═' * 50}{RESET}")
print()
