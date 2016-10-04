def add_vegetable(vegetable, list_of_vegetables=[]):
    list_of_vegetables.append(vegetable)
    return list_of_vegetables

first_list = add_vegetable('carrot')
second_list = add_vegetable('banana')

print(first_list)
print(second_list)

def add_vegetable_correctly(vegetable, list_of_vegetables=None):
    if list_of_vegetables is None:
        list_of_vegetables = []
    list_of_vegetables.append(vegetable)
    return list_of_vegetables

first_list = add_vegetable_correctly('carrot')
second_list = add_vegetable_correctly('banana')

print(first_list)
print(second_list)