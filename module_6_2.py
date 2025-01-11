class Vehicle:  # транспорт
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'cherry red']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f'{Vehicle.get_model(self)} \n{Vehicle.get_horsepower(self)} \n{Vehicle.get_color(self)} '
            f'\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in Vehicle._COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

print()

vehicle2 = Sedan('Елена', 'Фольксваген Джетта 5', 'red', 102)
vehicle2.print_info()
vehicle2.set_color('Pink')
vehicle2.set_color('CHERRY RED')
vehicle2.owner = 'Мария'
vehicle2.print_info()




