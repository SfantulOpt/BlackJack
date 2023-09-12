import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(rank, suit))

    def shuffle(self):
        return random.shuffle(self.allcards)

    def deal_one(self):
        return self.allcards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.how_many = 0

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_card(self, new_card):
        if new_card.rank == 'Ace' and new_card.value + self.how_many > 21:
            self.how_many += 1
        else:
            self.how_many += new_card.value
        self.all_cards.append(new_card)

    def __str__(self):
        return f'{self.name} has {self.how_many} points'


class Bani:
    def __init__(self):
        self.money = 0
        self.moneytobet = 0

    def deposit(self):
        while True:
            add = input('How much money do you want to deposit: ')
            try:
                add = int(add)
            except ValueError:
                print("You're answer must be a digit")
                continue
            if add == 0:
                print('You have to deposit money in order to play!')
                continue
            else:
                self.money += add
                break

    def bet_money(self):
        while True:
            a = input('How much do you want to bet? ')
            try:
                a = int(a)
            except ValueError:
                print("You're answer must be a number.")
                continue
            if a == 0:
                print('You have to bet money in order to play!')
                continue
            else:
                if a > self.money:
                    print("You don't have enough money to bet!")
                    continue
                else:
                    self.moneytobet = a
                    self.money = self.money - self.moneytobet
                    break



class Dealer:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.how_many = 0
        self.money = 0
        self.latest_card = 0

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_card(self, new_card):
        if new_card.rank == 'Ace' and new_card.value + self.how_many > 21:
            self.how_many += 1
            self.all_cards.append(new_card)
            self.latest_card = 1
        else:
            self.how_many += new_card.value
            self.all_cards.append(new_card)
            self.latest_card = new_card.value

    def __str__(self):
        if game_on == False:
            return f'{self.name} has {self.how_many} points'
        elif len(self.all_cards) == 1:
            return f'{self.name} has {self.how_many} points'
        else:
            return f'{self.name} has {self.how_many - self.latest_card} points'


BlackJack_on = True
print('Welcome to BlackJack')
nume = input("What is you're name?\n")
account = Bani()

while BlackJack_on:

    pachet = Deck()
    pachet.shuffle()
    player1 = Player(nume)
    dealer = Dealer('Dealer')
    dealer.add_card(pachet.deal_one())
    player1.add_card(pachet.deal_one())
    dealer_will = ''
    while True:
        bet = input(f"Do you want to deposit more money or withdraw? Your current balance is {account.money} dollars.\n").lower()
        if bet == 'withdraw' and account.money != 0:
            print(f'You have left the casino with {account.money} dollars.')
            quit()
        elif bet == 'withdraw' and account.money == 0:
            print("You don't have any money to withdraw.")
        elif bet == 'yes':
            account.deposit()
            break
        elif bet == 'no' and account.money == 0:
            print('You have to deposit in order to bet!')
        elif bet == 'no' and account.money != 0:
            break
        else:
            print("You're answer must be yes/no")

    account.bet_money()

    while True:
        answear = input('Are you ready to play? ')
        if answear.lower() == 'yes':
            game_on = True
            break
        elif answear.lower() == 'no':
            quit()
        else:
            print("You're answer must be yes/no")

    while game_on:
        num = random.randint(0,100)
        if dealer.how_many > 19:
            dealer_will = 'Stand'
        elif dealer.how_many > player1.how_many and not dealer.how_many < 11:
            dealer_will = 'Stand'
        else:
            dealer_will = 'Hit'

        print(dealer)
        if len(dealer.all_cards) == 1:
            for card in dealer.all_cards:
                print(card)
        else:
            dealer_cards_except_last_card = dealer.all_cards[:-1]
            for card in dealer_cards_except_last_card:
                print(card)
            print('Last card is hidden.')



        print(player1)
        for card in player1.all_cards:
            print(card)
        while True:
            action = input('Stand/Hit ').lower()

            if action == 'stand' or action == 'hit':
                break
            else:
                continue


        if action == 'stand':
            if dealer_will == 'Stand' and dealer.how_many > player1.how_many:
                print(f'Dealer will {dealer_will}.')
                print('Dealer wins!')
                print(f'Dealers hand was:')
                for card in dealer.all_cards:
                    print(card)
                dealer.money += account.moneytobet
                game_on = False
                break

        if dealer_will == 'Hit' and action == 'hit':
            print(f'Dealer will {dealer_will}.')
            dealer.add_card(pachet.deal_one())
            player1.add_card(pachet.deal_one())
        elif dealer.how_many == player1 and action == 'Stand':
            if num % 2 == 0:
                print(f'Dealer will Hit.')
                dealer.add_card(pachet.deal_one())
            else:
                print('Dealer will Stand.')
                print("It's a tie!")
                account.money += account.moneytobet
                game_on = False
                break
        elif dealer_will == 'Stand' and action == 'hit':
            print(f'Dealer will {dealer_will}.')
            player1.add_card(pachet.deal_one())
        elif action == 'stand' and dealer_will == 'Hit':
            print(f'Dealer will {dealer_will}.')
            dealer.add_card(pachet.deal_one())

        if player1.how_many > 21:
            print(player1)
            print('Dealer wins!')
            print(f'Dealers hand was:')
            for card in dealer.all_cards:
                print(card)
            dealer.money += account.moneytobet
            game_on = False
            break
        if dealer.how_many > 21:
            game_on = False
            print(dealer)
            print('Player wins!')
            account.money += account.moneytobet * 2
            break


