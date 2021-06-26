class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push_front(self, item):
        self.items.append(item)

    def push_back(self, item):
        self.items.insert(0,item)

    def pop_front(self):
        return self.items.pop()

    def pop_back(self):
        return self.items.pop(0)

    def front(self):
        return self.items[-1]

    def back(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []

a_player = Deque()
b_player = Deque()

first_deck = str(input()).split()
first_deck = [int(i) for i in first_deck]

second_deck = str(input()).split()
second_deck = [int(i) for i in second_deck]

for i in first_deck:
    a_player.push_back(i)
for i in second_deck:
    b_player.push_back(i)

is_botva = False
stop = 0
while a_player.size() != 0 and b_player.size() != 0:
    stop += 1

    a_card = a_player.front()
    a_player.pop_front()

    b_card = b_player.front()
    b_player.pop_front()

    if (a_card > b_card and a_card != 9) or (a_card == 9 and b_card != 0) or (a_card == 0 and b_card == 9) : 
        a_player.push_back(a_card)
        a_player.push_back(b_card)
    else:
        b_player.push_back(a_card)
        b_player.push_back(b_card)

    if stop == 1e6:
        print("botva\n")
        is_botva = True
        break
if is_botva == False:
    if a_player.isEmpty() == False:
        print(f"first {stop}\n")
    else:
        print(f"second {stop}\n")