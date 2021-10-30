import random

class d4:
    displays = {
    1: """
       /\\
      /  \\
     /  1 \\
    /______\\
    """,
    2:"""
       /\\
      /  \\
     /  2 \\
    /______\\
    """,
    3:"""
       /\\
      /  \\
     /  3 \\
    /______\\
    """,
    4:"""
       /\\
      /  \\
     /  4 \\
    /______\\
    """
    }
    def __init__(self, value = random.randint(1,4)):
        self.value = value

    def roll(self):
        self.value = random.randint(1,4)

    def display(self):
        print(self.displays[self.value])

class d6:
    displays = {
    1: """
    ┌──────┐
    │      │
    │   1  │
    └──────┘
    """,
    2: """
    ┌──────┐
    │      │
    │   2  │
    └──────┘
    """,
    3: """
    ┌──────┐
    │      │
    │   3  │
    └──────┘
    """,
    4: """
    ┌──────┐
    │      │
    │   4  │
    └──────┘
    """,
    5: """
    ┌──────┐
    │      │
    │   5  │
    └──────┘
    """,
    6: """
    ┌──────┐
    │      │
    │   6  │
    └──────┘
    """
    }
    def __init__(self, value = random.randint(1,6)):
        self.value = value

    def roll(self):
        self.value = random.randint(1,6)

    def display(self):
        print(self.displays[self.value])

class d8:
    displays = {
    1: """
      /──\\
     /    \\
     \\  1 /
      \\──/
    """,
    2: """
      /──\\
     /    \\
     \\  2 /
      \\──/
    """,
    3: """
      /──\\
     /    \\
     \\  3 /
      \\──/
    """,
    4: """
      /──\\
     /    \\
     \\  4 /
      \\──/
    """,
    5: """
      /──\\
     /    \\
     \\  5 /
      \\──/
    """,
    6: """
      /──\\
     /    \\
     \\  6 /
      \\──/
    """,
    7: """
      /──\\
     /    \\
     \\  7 /
      \\──/
    """,
    8: """
      /──\\
     /    \\
     \\  8 /
      \\──/
    """
    }
    def __init__(self, value = random.randint(1,8)):
        self.value = value

    def roll(self):
        self.value = random.randint(1,8)

    def display(self):
        print(self.displays[self.value])

class d10:
    displays = {
    1: """
       /\\
      /  \\
     /  1 \\
     \\____/
    """,
    2: """
       /\\
      /  \\
     /  2 \\
     \\____/
    """,
    3: """
       /\\
      /  \\
     /  3 \\
     \\____/
    """,
    4: """
       /\\
      /  \\
     /  4 \\
     \\____/
    """,
    5: """
       /\\
      /  \\
     /  5 \\
     \\____/
    """,
    6: """
       /\\
      /  \\
     /  6 \\
     \\____/
    """,
    7: """
       /\\
      /  \\
     /  7 \\
     \\____/
    """,
    8: """
       /\\
      /  \\
     /  8 \\
     \\____/
    """,
    9: """
       /\\
      /  \\
     /  9 \\
     \\____/
    """,
    10: """
       /\\
      /  \\
     / 10 \\
     \\____/
    """
    }
    def __init__(self, value = random.randint(1,10)):
        self.value = value

    def roll(self):
        self.value = random.randint(1,10)

    def display(self):
        print(self.displays[self.value])

class d12:
    displays = {
    1: """
      /‾‾\\
     │  1 │
     │    │
      \\__/
    """,
    2: """
      /‾‾\\
     │  2 │
     │    │
      \\__/
    """,
    3: """
      /‾‾\\
     │  3 │
     │    │
      \\__/
    """,
    4: """
      /‾‾\\
     │  4 │
     │    │
      \\__/
    """,
    5: """
      /‾‾\\
     │  5 │
     │    │
      \\__/
    """,
    6: """
      /‾‾\\
     │  6 │
     │    │
      \\__/
    """,
    7: """
      /‾‾\\
     │  7 │
     │    │
      \\__/
    """,
    8: """
      /‾‾\\
     │  8 │
     │    │
      \\__/
    """,
    9: """
      /‾‾\\
     │  9 │
     │    │
      \\__/
    """,
    10: """
      /‾‾\\
     │ 10 │
     │    │
      \\__/
    """,
    11: """
      /‾‾\\
     │ 11 │
     │    │
      \\__/
    """,
    12: """
      /‾‾\\
     │ 12 │
     │    │
      \\__/
    """,
    13: """
      /‾‾\\
     │ 13 │
     │    │
      \\__/
    """,
    14: """
      /‾‾\\
     │ 14 │
     │    │
      \\__/
    """,
    15: """
      /‾‾\\
     │ 15 │
     │    │
      \\__/
    """,
    16: """
      /‾‾\\
     │ 16 │
     │    │
      \\__/
    """,
    17: """
      /‾‾\\
     │ 17 │
     │    │
      \\__/
    """,
    18: """
      /‾‾\\
     │ 18 │
     │    │
      \\__/
    """,
    19: """
      /‾‾\\
     │ 19 │
     │    │
      \\__/
    """,
    20: """
      /‾‾\\
     │ 20 │
     │    │
      \\__/
    """
    }
    def __init__(self, value = random.randint(1,20)):
        self.value = value

    def roll(self):
        self.value = random.randint(1,20)

    def display(self):
        print(self.displays[self.value])
if __name__ == '__main__':
    main()

def main():
    run = True
    dice_array = input("Please enter in the number of each dice you would like.\n",
    "[d4,d6,d8,d10,d12,d20]\n",
    "For example, if you want to roll 3 d4s, and 2 d20s, you would input\n",
    "[3,0,0,0,0,2]")
    while(run):
