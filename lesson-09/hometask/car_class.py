"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
отображение скорости, задния ход (изменение знака скорости)."""


class Car:

    def __init__(self, brand, model, year, speed=int(0)):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5

    def car_stop(self):
        self.speed = 0

    def current_speed(self):
        print(self.speed)

    def reverse_gear(self):
        self.speed = -abs(self.speed)


