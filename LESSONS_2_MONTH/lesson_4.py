# RPG - Role Play Game

import random

total_rounds = 0


CRITICAL_DAMAGE = "CRITICAL_DAMAGE"
HEAL = "HEAL"
BOOST = "BOOST"


class GameEntity:
    def __init__(self, name, health, damage) -> None:
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        if value <= 0:
            self.__health = 0
        else:
            self.__health = value
    
    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self) -> str:
        return f"{self.name} health: {self.health} damage: {self.damage}"
    


class Boss(GameEntity):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage)



class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability_type) -> None:
        super().__init__(name, health, damage)
        self.__super_ability_type = super_ability_type

    @property
    def super_ability_type(self):
        return self.__super_ability_type

    @super_ability_type.setter
    def super_ability_type(self, value):
        self.__super_ability_type = value

    def apply_super_power(self, boss: Boss, heroes: list):
        pass
    

class Warrior(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, CRITICAL_DAMAGE)

    def apply_super_power(self, boss: Boss, heroes: list):
        coef = random.randint(0, 5)
        boss.health -= self.damage*coef
        message = f"Warrior {self.name}, hits criticaly: {self.damage*coef}" \
            if coef else "Не нанес критический урон"
        print(message) 


class Medic(Hero):
    def __init__(self, name, health, damage, heal_point) -> None:
        super().__init__(name, health, damage, HEAL)
        self.__heal_point = heal_point

    def apply_super_power(self, boss: Boss, heroes: list):
        print(f"Medic {self.name}: {self.__heal_point} healed")
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_point


class Magic(Hero):
    def __init__(self, name, health, damage) -> None:
        super().__init__(name, health, damage, BOOST)

    def apply_super_power(self, boss: Boss, heroes: list):
        boost = random.randint(1, 5)
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.damage += boost
        print(f"Magic {self.name}: {boost} boosted")



def is_game_finished(boss: Boss, heroes: list):
    if boss.health <= 0:
        print("Heroes WON!")
        return True
    
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
    
    if all_heroes_dead:
        print("Boss WON!")

    return all_heroes_dead



def print_statistic(boss: Boss, heroes: list):
    print(f"________ {total_rounds} ROUND ________")
    print(boss)
    for hero in heroes:
        print(hero)


def boss_hit(boss: Boss, heroes: list):
    for hero in heroes:
        if hero.health > 0 and boss.health > 0:
            hero.health -= boss.damage

def heroes_hit(boss: Boss, heroes: list):
    for hero in heroes:
        if hero.health > 0 and boss.health > 0:
            boss.health -= hero.damage

def heroes_power(boss: Boss, heroes: list):
    boss_ability = random.choice([CRITICAL_DAMAGE, BOOST, HEAL])
    print(f"Boss blocked {boss_ability}")
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss_ability != hero.super_ability_type:
            hero.apply_super_power(boss, heroes)

def play_round(boss: Boss, heroes: list):
    print_statistic(boss, heroes)
    global total_rounds
    total_rounds += 1
    boss_hit(boss, heroes)
    heroes_hit(boss, heroes)
    heroes_power(boss, heroes)
    


def start():
    boss = Boss("Antaras", 1000, 50)

    warrior = Warrior("Varvar", 260, 5)
    warrior_2 = Warrior("Terminator", 290, 10)
    medic = Medic("Aibolit", 220, 5, 15)
    medic_2 = Medic("Dr. Haos", 240, 10, 10)
    magic = Magic("Wisard", 290, 20)

    heroes = [warrior, medic, medic_2, magic, warrior_2]

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)
       

    print_statistic(boss, heroes)


start()