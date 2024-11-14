from smartphone import Smartphone

smartphone_1 = Smartphone('Samsung', 'Galaxy A55', '+79998887766')
smartphone_2 = Smartphone('Xiaomi', 'Redmy Note 13', '+79876543322')
smartphone_3 = Smartphone('HONOR', 'X9b', '+79117894563')
smartphone_4 = Smartphone('POCO', 'M6 Pro', '+79218885544')
smartphone_5 = Smartphone('HUAWEI', 'Pura 70', '+79317774455')
catalog =[smartphone_1, smartphone_2, smartphone_3, smartphone_4, smartphone_5]

for i in range(0, len(catalog)):
    print(catalog[i].get_smartphone())

