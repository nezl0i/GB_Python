# 4. Реализуйте базовый класс Car.
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.go()

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} превышена')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.name} превышена')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.__get_is_policy()

    def __get_is_policy(self):
        if self.is_police:
            print('This car is policy')
        else:
            print('Ok, this car is not policy!')


town = TownCar(100, "Yellow", "Vesta")
sport = SportCar(170, "Red", "Mustang")
work = WorkCar(40, "Blue", "Niva")
police = PoliceCar(90, "White", "Bibika", True)

town.turn('Налево')
sport.turn('Направо')
work.turn('Направо')
police.turn('Налево')

sport.stop()
police.stop()
town.show_speed()
work.show_speed()
