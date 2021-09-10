# გვაქვს 1,5,10,20 და 50 თეთრიანი მონეტები. დაწერეთ ფუნქცია, რომელსაც გადაეცემა თანხა (თეთრებში) და
# აბრუნებს მონეტების მინიმალურ რაოდენობას, რომლითაც შეგვიძლია ეს თანხა დავახურდაოთ.
# მაგ: ყველაზე მოკლე გზა 70 თეთრის დასაშლელად არის 50+20 თეთრიანი მონეტები, შესაბამისად ფუნქციამ უნდა დააბრუნოს 2.

#2
def coin_counter(change):
    min_coins = {}
    coins = [1, 5, 10, 20, 50]
    list1 = []
    for tetris in range(change + 1):
        coin_count = tetris
        for c in coins:
            if c <= tetris:
                list1.append(c)
            for j in list1:
                if min_coins[tetris - j] + 1 < coin_count:
                    coin_count = min_coins[tetris - j] + 1
        min_coins[tetris] = coin_count
    return min_coins[change]


change = int(input("შეიყვანეთ ხურდა: "))
print(coin_counter(change))