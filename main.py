from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання
    start_date = date.today()
    end_date = start_date + timedelta(weeks=1)
    celebrates = defaultdict(list)

    for user in users:
        b_d = user.get('birthday')
        
        b_d = b_d.replace(year=start_date.year+1) if b_d.month == 1 else b_d.replace(
            year=start_date.year)
        
        if (b_d >= start_date) and (b_d < end_date):
            weekday = b_d.strftime('%A')
        
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            name = user.get('name').split(' ')[0]
            celebrates[weekday].append(name)
    
    return celebrates


if __name__ == "__main__":
    users = [
        {"name": "Jan1 Koum1", "birthday": datetime(1976, 11, 18).date()},
        {"name": "Jan2 Koum2", "birthday": datetime(1976, 11, 19).date()},
        {"name": "Jan3 Koum3", "birthday": datetime(1976, 11, 20).date()},
        {"name": "Jan4 Koum4", "birthday": datetime(1976, 11, 21).date()},
        {"name": "Jan5 Koum5", "birthday": datetime(1976, 11, 22).date()},
        {"name": "Jan6 Koum6", "birthday": datetime(1976, 11, 23).date()},
        {"name": "Jan7 Koum7", "birthday": datetime(1976, 11, 24).date()},
        {"name": "Jan8 Koum8", "birthday": datetime(1976, 11, 25).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
