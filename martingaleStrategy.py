import random
import sys

sys.setrecursionlimit(10000000)
balance = 1000000000000.0
betMoney = 0.1
counter = 0

def randomChooser(guess, trials):
    global counter, balance, betMoney
    
    if counter == trials:
        return
    
    a = random.randint(0, 1)
    if(betMoney > balance):
        print(f"You don't have {betMoney} liras.")
        return

    if guess == a:
        balance += betMoney
        print(f"{counter + 1}. tur: Kazandınız, {(betMoney):.2f} lira kazandınız. Toplam bakiye: {balance:.2f} lira")
        betMoney = 1
    else:
        balance -= betMoney
        print(f"{counter + 1}. tur: Kaybettiniz, {betMoney:.2f} lira kaybettiniz. Toplam bakiye: {balance:.2f} lira")
        betMoney *= 2
        if counter+1 == trials:
            counter -= 1
    
    counter += 1
    return randomChooser(guess, trials)

def repeater():
    global balance, betMoney, counter
    balance = 1000000000000.0
    betMoney = 0.1
    counter = 0
    oldBalance = balance
    print(f"Başlangıçta bakiyeniz: {balance:.2f} lira")
    randomChooser(1, 100)
    if(balance - oldBalance > 0):
        print(f"Toplamda {(balance - oldBalance):.2f} lira kazandınız!")
        repeater()
    else:
        print(f"Toplamda {(balance - oldBalance):.2f} lira kaybettiniz...")
        return
    print(f"Güncel bakiyeniz: {balance:.2f} lira")

repeater()