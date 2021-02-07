from random import randint


class Card:
    def __init__(self):
        self.data = []
        self.in_start = 1
        self.in_stop = 9
        self.generation_card()

    def generation_card(self):
        while len(self.data) < 9:
            tmp = []
            for _ in range(2):
                tmp_el = randint(self.in_start, self.in_stop)
                if tmp_el not in tmp:
                    tmp.append(tmp_el)
            if len(tmp) == 2:
                index = randint(0, 3)
                tmp.insert(index, 0)
            elif len(tmp) == 1:
                tmp.insert(0, 0)
                tmp.insert(2, 0)
            self.data.append(tmp)
            self.in_start += 10
            if self.in_start == 80:
                self.in_stop += 11
            else:
                self.in_stop += 10
        return self.data

    @property
    def check_data(self):
        for items in self.data:
            for el in items:
                if el != 99 and el != 0:
                    return False
        return True

    @staticmethod
    def generate_score(count, min_score, max_score):
        data_score = []
        while len(data_score) < count:
            new = randint(min_score, max_score)
            if new not in data_score:
                data_score.append(new)
        return data_score

    def __contains__(self, item):
        for items in self.data:
            if item in items:
                return item in items
        return None

    def delete_item(self, num):
        for i, items in enumerate(self.data):
            for j, item in enumerate(self.data[i]):
                if item == num:
                    self.data[i][j] = 99
                    return

    def __str__(self):
        card = ''
        for i in range(3):
            for j in range(len(self.data)):
                if self.data[j][i] == 0:
                    card += '   '
                elif self.data[j][i] < 10:
                    card += f' {self.data[j][i]} '
                elif self.data[j][i] == 99:
                    card += ' - '
                else:
                    card += f'{self.data[j][i]} '
            card += '\n'
        card += '-----------------------------'
        return f'{card}'


class Game:
    def __init__(self):
        self.user_card = Card()
        self.comp_card = Card()
        self.scores = [x for x in Card().generate_score(90, 1, 90)]

    def start(self):
        print(f'------- Ваша карточка -------\n{self.user_card}')
        print(f'---- Карточка компьютера ----\n{self.comp_card}')
        pop_item = self.scores.pop()
        print(f'Текущий бочонок {pop_item}  Осталось: {len(self.scores)}')
        answer = input(f'Зачеркнуть цифру? (y/n): ')

        if answer == 'y' and pop_item not in self.user_card or \
                answer != 'y' and pop_item in self.user_card:
            return 2

        if pop_item in self.user_card:
            self.user_card.delete_item(pop_item)
            if self.user_card.check_data:
                return 1
        if pop_item in self.comp_card:
            self.comp_card.delete_item(pop_item)
            if self.comp_card.check_data:
                return 2
        return 0


game = Game()
while True:
    winners = game.start()
    if winners == 1:
        print('Поздравляю, вы выиграли!!')
        break
    elif winners == 2:
        print('Вы проиграли')
        break
