def get_pet_shop_name(dictionary_name):
    return dictionary_name["name"]

def get_total_cash(dictionary_name):
    return dictionary_name["admin"]["total_cash"]

def add_or_remove_cash(dictionary_name, difference):
    dictionary_name["admin"]["total_cash"] += difference

def get_pets_sold(dictionary_name):
    return dictionary_name["admin"]["pets_sold"]

def increase_pets_sold(dictionary_name, num_of_pets_sold):
    dictionary_name["admin"]["pets_sold"] += num_of_pets_sold

def get_stock_count(dictionary_name):
    return len(dictionary_name["pets"])

def get_pets_by_breed(dictionary_name, breed):
    pets_of_breed = []
    for pet in dictionary_name["pets"]:
        if pet["breed"] == breed:
            pets_of_breed.append(pet["name"])
    return pets_of_breed

def find_pet_by_name(dictionary_name, name_to_find):
    for pet in dictionary_name["pets"]:
        if pet["name"] == name_to_find:
            pet_list = pet
            return pet_list

def remove_pet_by_name(dictionary_name, pet_to_remove):
    for pet in dictionary_name["pets"]:
        if pet["name"] == pet_to_remove:
            dictionary_name["pets"].remove(pet)

def add_pet_to_stock(dict_1, dict_2):
    dict_1["pets"].append(dict_2)

def get_customer_cash(customer_index):
    return customer_index["cash"]

def remove_customer_cash(customer_index, cash_to_remove):
    customer_index["cash"] -= cash_to_remove

def get_customer_pet_count(customer_index):
    return len(customer_index["pets"])

def add_pet_to_customer(customer_index, pet_to_add):
    customer_index["pets"].append(pet_to_add)

# Optional tasks
def customer_can_afford_pet(customer_index, pet_to_check):
    if customer_index["cash"] >= pet_to_check["price"]:
        return True
    else:
        return False

# Integration tests
def sell_pet_to_customer(pet_stock, pet_to_sell, customer_index):
    # if the pet being checked doesn't exist in the stock list, the type will be None
    if type(pet_to_sell) == dict:
        if customer_can_afford_pet(customer_index, pet_to_sell) == True:
            add_pet_to_customer(customer_index, pet_to_sell)
            increase_pets_sold(pet_stock, 1)
            remove_customer_cash(customer_index, pet_to_sell["price"])
            add_or_remove_cash(pet_stock, pet_to_sell["price"])
            remove_pet_by_name(pet_stock, pet_to_sell["name"])