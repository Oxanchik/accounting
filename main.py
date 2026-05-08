from datetime import datetime, timedelta
import locale

# пакет humanize приводит данные в "человеческий" вид:
import humanize

from application.salary import calculate_salary
from application.db.people import get_employees


# Устанавливаем русскую локаль:
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

def format_number_with_spaces(number):
    return f"{number:,}".replace(",", " ")

def main():
    comp_date = datetime.now() - timedelta(days=365)
    human_date = humanize.naturaldate(comp_date)
    print(f"Дата и время: {comp_date}")
    print(f"Дата по-человечески: {human_date}\n")

    base_salary = 110000
    overtime_hours = 12
    overtime_rate = 6500
    salary_da = calculate_salary(base_salary, overtime_hours, overtime_rate)
    salary_da_formatted = format_number_with_spaces(salary_da)

    employees = get_employees()
    print(f"Сотрудников всего: {len(employees)}")

    name_da = "не найден"
    for employee in employees:
        print(f"- {employee['name']} ({employee['role']})")
        if employee["role"] == "Data Analyst":
            name_da = employee['name']
    print("")
    print(f"Зарплата Data Analyst ({name_da}): {salary_da_formatted} руб.")


if __name__ == '__main__':
    main()