class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    def get_cpu(self):
        return self.__cpu
    
    def set_cpu(self, cpu):
        self.__cpu = cpu
    
    def get_memory(self):
        return self.__memory
    
    def set_memory(self, memory):
        self.__memory = memory
    
    def make_computations(self):
        return self.__cpu * self.__memory
    
    def __eq__(self, other):
        return self.__memory == other.get_memory()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__memory < other.get_memory()

    def __gt__(self, other):
        return self.__memory > other.get_memory()

    def __le__(self, other):
        return self.__memory <= other.get_memory()

    def __ge__(self, other):
        return self.__memory >= other.get_memory()

    def __str__(self):
        return f'Computer [cpu={self.__cpu}, memory={self.__memory}]'


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    
    def get_sim_cards_list(self):
        return self.__sim_cards_list
    
    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    
    def call(self, sim_card_number, call_to_number):
        sim_card = self.__sim_cards_list[sim_card_number - 1]
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}')
    
    def __str__(self):
        return f'Phone [sim_cards_list={self.__sim_cards_list}]'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
    
    def use_gps(self, location):
        print(f'Проложен маршрут до локации {location}')
    
    def __str__(self):
        return f'SmartPhone [cpu={self.get_cpu()}, memory={self.get_memory()}, sim_cards_list={self.get_sim_cards_list()}]'


# Создаем объекты
computer1 = Computer(3.5, 8)
phone1 = Phone(['Beeline', 'O!', 'Megacom'])
smartphone1 = SmartPhone(2.2, 4, ['Megacom'])
smartphone2 = SmartPhone(3.0, 6, ['Beeline', 'O!'])

print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)


print(f'Результат вычислений компьютера: {computer1.make_computations()}')
phone1.call(1, '+996 777 99 88 11')
smartphone1.use_gps('Дом')
print(smartphone2 >= smartphone1) 
print(smartphone1 == smartphone2)  
print(computer1 != smartphone1)  