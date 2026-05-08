def calculate_salary(base_salary, overtime_hours, overtime_rate, tax=0.13):
    """
    Расчет зарплаты

    Args:
    base_salary - базовая ставка
    overtime_hours - количество сверхурочных часов
    overtime_rate - ставка за час сверхурочной работы
    tax - налог. По умолчанию 13%

    """
    overtime = overtime_hours * overtime_rate
    gross = base_salary + overtime
    net = int(gross * (1 - tax))
    return net