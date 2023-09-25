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

# C-2.年齢という概念

# customerクラスの定義


class Customer:

    # 初期設定
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # ageの定義
    # def age(self):
    #     return self.age


# kenの年齢
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.age)  # 15 という値を返す

# tomの年齢
tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.age)  # 57 という値を返す

# ieyasuの年齢
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.age)  # 73 という値を返す

# C-3.年齢に応じた適切な入場料金を計算できる

# customerクラスの定義


class Customer:

    # 初期設定
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # 年齢に応じた入場料金の定義
    def entry_fee(self):
        # こども料金
        if self.age <= 20:
            return 1000

        # おとな料金
        elif 20 < self.age < 65:
            return 1500

        # シニア料金
        else:
            return 1200


# kenの場合
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.entry_fee())  # 1000 という値を返す

# tomの場合
tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.entry_fee())  # 1500 という値を返す

# ieyasuの場合
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.entry_fee())  # 1200 という値を返す

# C-4.単一顧客情報をCSV形式で取得できる

# customerクラスの定義


class Customer:

    # 初期設定
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # full＿nameの定義
    def full_name(self):
        return self.first_name + " " + self.family_name

    # ageの定義
    # def age(self):
    #     return self.age

    # 年齢に応じた入場料金の定義
    def entry_fee(self):
        # こども料金
        if self.age < 20:
            return 1000

        # おとな料金
        elif 20 <= self.age < 65:
            return 1500

        # シニア料金
        else:
            return 1200

    # 顧客情報をCSV形式で出力する
    def info_csv(self,separator =","):
        return self.first_name + " " + self.family_name + separator + str(self.age) + separator + str(self.entry_fee())


# kenの場合
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す
# tomの場合
tom = Customer(first_name="Tom", family_name="Ford", age=57)
print(tom.info_csv())  # "Tom Ford,57,1500" という値を返す
# ieyasuの場合
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200" という値を返す


# 応用問題
# c-5.3歳以下の入場料金の無料化

class Customer:

    # 初期設定
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # full＿nameの定義
    def full_name(self):
        return self.first_name + " " + self.family_name

    # ageの定義
    # def age(self):
    #     return self.age

    # 年齢に応じた入場料金の定義
    def entry_fee(self):
        # 3歳以下は無料
        if self.age <= 3:
            return 0

        # こども料金
        if 3 <= self.age < 20:
            return 1000

        # おとな料金
        elif 20 <= self.age < 65:
            return 1500

        # シニア料金
        else:
            return 1200

    # 顧客情報をCSV形式で出力する
    def info_csv(self,separator =","):
        return self.first_name + " " + self.family_name + separator + str(self.age) + separator + str(self.entry_fee())


# 3歳以下の出力例
Bob = Customer(first_name="Bob", family_name="Tanaka", age= 3)
print(Bob.info_csv())  # Bob,Tanaka,0 という値を返す

#c-6.75歳以上の料金区分の追加

class Customer:

    # 初期設定
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # full＿nameの定義
    def full_name(self):
        return self.first_name + " " + self.family_name

    # ageの定義
    # def age(self):
    #     return self.age

    # 年齢に応じた入場料金の定義
    def entry_fee(self):
        # 3歳以下は無料
        if self.age <= 3:
            return 0

        # こども料金
        elif 3 <= self.age < 20:
            return 1000

        # おとな料金
        elif 20 <= self.age < 65:
            return 1500

        # シニア料金
        elif 65 <= self.age < 75:
            return 1200
        
        #75歳以上の顧客の料金
        else:
            return 500
            

    # 顧客情報をCSV形式で出力する
    def info_csv(self,separator=","):
        return self.first_name + " " + self.family_name + separator + str(self.age) + separator + str(self.entry_fee())


# 75歳以上の出力例
Kin = Customer(first_name="Kin", family_name="Narita", age= 100)
print(Kin.info_csv())  # Kin,Narita,100,500 という値を返す

#c-7.単一顧客の情報取得形式の追加その１

class Customer:

    # 初期設定
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # full＿nameの定義
    def full_name(self):
        return self.first_name + " " + self.family_name

    # ageの定義
    # def age(self):
    #     return self.age

    # 年齢に応じた入場料金の定義
    def entry_fee(self):
        # 3歳以下は無料
        if self.age <= 3:
            return 0

        # こども料金
        elif 3 <= self.age < 20:
            return 1000

        # おとな料金
        elif 20 <= self.age < 65:
            return 1500

        # シニア料金
        elif 65 <= self.age < 75:
            return 1200
        
        #75歳以上の顧客の料金
        else:
            return 500
            

    # 顧客情報をCSV形式で出力する
    def info_csv(self,separetar ="\t"):
        return self.first_name + " " + self.family_name + separetar + str(self.age) + separetar + str(self.entry_fee())


# 出力例
Kin = Customer(first_name="Kin", family_name="Narita", age= 100)
print(Kin.info_csv())  # Kin　Narita　100 500 という値を返す

#c-8.単一顧客の情報取得形式の追加その2

class Customer:

    # 初期設定
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # full＿nameの定義
    def full_name(self):
        return self.first_name + " " + self.family_name

    # ageの定義
    # def age(self):
    #     return self.age

    # 年齢に応じた入場料金の定義
    def entry_fee(self):
        # 3歳以下は無料
        if self.age <= 3:
            return 0

        # こども料金
        elif 3 <= self.age < 20:
            return 1000

        # おとな料金
        elif 20 <= self.age < 65:
            return 1500

        # シニア料金
        elif 65 <= self.age < 75:
            return 1200
        
        #75歳以上の顧客の料金
        else:
            return 500
            

    # 顧客情報をCSV形式で出力する
    def info_csv(self,separator = "|"):
        return self.first_name + " " + self.family_name + separator + str(self.age) + separator + str(self.entry_fee())


# 出力例
Kin = Customer(first_name="Kin", family_name="Narita", age= 100)
print(Kin.info_csv())  # Kin Narita|100|500 という値を返す