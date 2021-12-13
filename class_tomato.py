class Tomato:
    states={0:'nothing', 1:'flower', 2:'unripe', 3:'ripe'}

    def __init__(self, index):
        self._index=index
        self._state=0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state==3:
            return 'The tomato is ripe'
        else:
            return 'The tomato is not ripe'

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:
    def __init__(self, number):
        self.tomatoes=[Tomato(i) for i in range(0,number)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
       self_tomatoes=[]

class Gardener:
    def __init__(self, name, plant):
        self.name=name
        self._plant=plant

    def work(self):
        print('The gardener works')
        self._plant.grow_all()
        print('The gardener stops working')

    def harvest(self):
        print('The gardener is harvesting')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('The harvesting is finished')
        else:
            print('You are harvesting too early')

    @staticmethod
    def knowledge_base():
        print('You need to harvest when the fruits are ripe')

if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Don Pedro', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()