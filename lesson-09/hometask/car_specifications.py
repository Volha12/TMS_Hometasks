"""Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает
 марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран."""
from car_class import Car


class Mercedes(Car):

    @property
    def car_info(self):
        car = "Mercedes", "E500", 2000, 0
        while car.speed != 100:
            car.speed = car.speed_up()
        print(car.speed)

