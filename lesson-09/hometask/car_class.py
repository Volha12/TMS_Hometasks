"""Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
отображение скорости, задния ход (изменение знака скорости)."""


class Car:

    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def speed_up(self) -> object:
        speed_change = self.speed + 5
        return speed_change

    def speed_down(self):
        speed_change = self.speed - 5
        return speed_change

    def car_stop(self):
        self.speed = 0
        speed_change = self.speed
        return speed_change

    def current_speed(self):
        current_speed = self.speed
        return f"{current_speed}"

    def reverse_gear(self):
        speed_change = -abs(self.speed)
        return speed_change





