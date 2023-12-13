import random
def coin_toss():
    Heads = 0
    Tails = 1
    record_list = []
    flip = random.choice([Heads, Tails])
    if (flip == Heads):
        record_list = ['Heads']
    elif (flip == Tails):
        record_list = ['Tails']

    print(str(record_list))
