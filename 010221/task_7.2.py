# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.
from abc import ABC, abstractmethod


class AbstractBrand(ABC):
    @abstractmethod
    def tissue_required(self):
        pass

    @abstractmethod
    def _tissue_consumption(self):
        pass

    @abstractmethod
    def get_total(self):
        pass


class Brand(AbstractBrand):
    _brand_list = []

    def __init__(self, name, size):
        self._name = name
        self._size = size
        self._brand_list.append(self)

    def _tissue_consumption(self):
        pass

    @property
    def tissue_required(self):
        return self._tissue_consumption()

    def _total_tissue(self):
        return f'Общее количество ткани {sum([item.tissue_required for item in self._brand_list])} м.'

    @property
    def get_total(self):
        return self._total_tissue()


class Coat(Brand):
    @property
    def V(self):
        return self._size

    def _tissue_consumption(self):
        return round(self.V / 6.5 + 0.5, 2)

    def __str__(self):
        return f"Для {self._name} {self.V} размера необходимо {self.tissue_required} м. ткани"


class Suit(Brand):
    @property
    def H(self):
        return self._size

    def _tissue_consumption(self):
        return round(2 * self.H + 0.3, 2)

    def __str__(self):
        return f"Для {self._name}а на рост {self.H} см. необходимо {self.tissue_required} м. ткани"


coat = Coat('Пальто', 48)
suit = Suit('Костюм', 120)

print(coat)
print(suit)

print(coat.V)
print(suit.H)

print(coat.tissue_required)
print(suit.tissue_required)

print(coat.get_total)
