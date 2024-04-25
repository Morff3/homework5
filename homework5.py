my_list = ['Banana', 'Orange', 'Apple', 'Pear', 'Kiwi', 'Mango', 'Pineapple']
print(my_list)
print(my_list[0::6])
print(my_list[2:5])
my_list[2] = 'Peach'
print(my_list)

# Работа со словарями

my_dict = {'Banana' : 'Банан', 'Orange' : 'Апельсин', 'Apple' : 'Яблоко', 'Pear' : 'Груша'}
print(my_dict)
print(my_dict ['Apple'])
my_dict['Orange'] = 'Мандарин'
my_dict.update({'Pomegranate' : 'Гранат',
                'Grapefruit' : 'Грейпфрут'})
print(my_dict)