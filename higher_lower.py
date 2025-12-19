# the data is stored in game_data.py file and art4
import game_data
import art4
print(art4.logo)
import random
def check(data_1,data_2):
    if data_1['follower_count'] > data_2['follower_count']:
        return data_1
    else:
        return data_2
count=0
def choose_1():
    global data_1
    data_1 = random.choice(game_data.data)
    return data_1

def choose_2():
    global data_2
    data_2 = random.choice(game_data.data)
    return data_2
data_1=choose_1()
data_2=choose_2()
while True:
    print(f"{data_1['name']} - {data_1['description']}")
    print(f"{data_2['name']} - {data_2['description']}")
    guess=str(input(f"Type 'y' if {data_1['name']} has more follower than {data_2['name']} or else 'n' "))

    if check(data_1,data_2)==data_1:
        if guess.lower()=='y':
            print("u r correct")
            count+=1
            data_2=choose_2()
        else:
            print("u lost ")
            print(count)
            break
    else:
        if guess=='y':
            print("u lost ")
            print(count)
            break
        else:
            data_1=data_2
            data_2=choose_2()
            print("u r correct")
            count+=1
    print('\n'*2)

