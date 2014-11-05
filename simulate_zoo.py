from zoo import Zoo
from animal import Animal


def get_command():
    return input('Enter command>').split(' ')


def main():
    zoo = Zoo(15, 1500)
    while True:
        full_command = get_command()
        command = full_command[0]
        if command == 'see_animals':
            zoo.see_animals()

        elif command == 'accommodate':
            species = full_command[1]
            name = full_command[2]
            age = int(full_command[3])
            gender = full_command[4]
            weight = float(full_command[5])
            zoo.accommodate(Animal(species, age, name, gender, weight))

        elif command == 'move_to_habitat':
            species = full_command[1]
            name = full_command[2]
            zoo.move_to_habitat(species, name)

        elif command == 'simulate':
            interval = full_command[1]
            period = int(full_command[2])
            zoo.simulate(interval, period)

        elif command == 'exit':
            print('Goodbye!')
            return

        else:
            print('Wrong command!')

if __name__ == '__main__':
    main()
