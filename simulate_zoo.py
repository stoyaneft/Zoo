from zoo import Zoo
from animal import Animal


def get_command():
    return input().split(' ')


def period_in_days(interval, period):
    if interval == 'days':
        days_in_interval = 1
    elif interval == 'weeks':
        days_in_interval = 7
    elif interval == 'months':
        days_in_interval = 30
    else:
        days_in_interval = 365
    return days_in_interval * period


def main():
    zoo = Zoo(15, 1500)
    full_command = get_command()
    command = full_command[0]

    if command == 'see_animals':
        zoo.see_animals

    elif command == 'accommodate':
        species = full_command[1]
        name = full_command[2]
        age = full_command[3]
        gender = full_command[4]
        weight = full_command[5]
        zoo.accommodate(Animal(species, age, name, gender, weight))

    elif command == 'move_to_habitat':
        species = full_command[1]
        name = full_command[2]
        zoo.move_to_habitat(species, name)

    elif command == 'simulate':
        interval = full_command[1]
        period = full_command[2]
        days = period_in_days(interval, period)
        zoo.simulate(days)

if __name__ == '__main__':
    main()
