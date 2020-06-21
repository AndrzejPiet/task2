list_items = [["banan" , "marchew"] , ["mielonka", "schabowy"], [ "krawat" , "koszula" ]]
list_shops = ("warzywniak", "mięsny", "odzieżowy")
dict_shoping = dict(zip(list_shops, list_items))

number_items = []
for k , v in dict_shoping.items () :
    print ("Ide do ", k.capitalize(), " aby kupić produkty : ",v )
    number_items.append(len(v))

sum_items = sum(number_items)
print( "W sumie kupuję", sum_items,  "produktów")
print("change in git hub")
