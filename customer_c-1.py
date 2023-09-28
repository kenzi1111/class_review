# C-1.フルネームを取得できる


# customerクラスの定義
class Customer:
    # 初期設定
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    # full＿nameの定義
    def full_name(self):
        return self.first_name + " " + self.family_name


# kenの場合
ken = Customer(first_name="Ken", family_name="Tanaka")
print(ken.full_name())

# tomの場合
tom = Customer(first_name="Tom", family_name="Ford")
print(tom.full_name())
