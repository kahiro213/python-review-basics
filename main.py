# --- 条件分岐 ---
score = 85
if score >= 90:
    print("Sランク")
elif score >= 70:
    print("Aランク")
else:
    print("Bランク")

# --- ループと内包表記 ---
nums = [i**2 for i in range(1, 6)]
print("2乗:", nums)

for i in range(1, 10):
    print(f"3 × {i} = {3 * i}")

# --- 関数 ---
def average(a, b):
    return (a + b) / 2

print("平均:", average(5, 7))

# --- 辞書 ---
words = {
    "apple": "りんご",
    "banana": "バナナ",
}
print(words["apple"])

# --- enumerateとzip ---
scores = [60, 80, 75]
for i, score in enumerate(scores):
    print(f"{i}番目の点数は{score}")

products = ['PC', 'Mouse']
prices = [1000, 50]
for product, price in zip(products, prices):
    print(f"{product}の値段は{price}円")

# --- try-except ---
try:
    user_input = "abc"
    value = int(user_input)
except ValueError:
    print("整数を入力してください")

# --- class ---
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name}がワンと鳴いた")

dog = Dog("ぽち", "柴犬")
dog.bark()

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

calc = Calculator(3, 4)
print("加算:", calc.add())
print("乗算:", calc.multiply())

class EmotionChecker:
    def __init__(self, text):
        self.text = text

    def is_positive(self):
        return 'ありがとう' in self.text

e = EmotionChecker("今日もありがとう！")
print("ポジティブ？", e.is_positive())