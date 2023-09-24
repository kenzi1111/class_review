# C-2.年齢という概念

# customerクラスの定義
class Customer:

    # 初期設定
    def __init__(self, first_name, family_name ,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # ageの定義
    def age(self):
        return self.age

#kenの年齢
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.age)  # 15 という値を返す

#tomの年齢
tom = Customer(first_name="Tom", family_name="Ford", age= 57)
print(tom.age) # 57 という値を返す

#ieyasuの年齢
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.age) # 73 という値を返す

