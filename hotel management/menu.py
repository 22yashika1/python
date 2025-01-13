#Define the menu of restaurant
menu = {
    'pizza' : 200,
    'pasta' : 150,
    'burger' : 80,
    'coffee' : 120,
    'salad' : 60,
    'pastry' : 100,
    'shakes' : 70,
    'fries' : 90,

}
#greet customers
print("welcome to the restaurant")
print("pizza : Rs. 200\npasta : Rs. 150\nburger : Rs. 80\ncoffee : Rs. 120\nsalad : Rs. 60\npastry : Rs. 100\nshakes : Rs. 70\nfries : Rs. 90")

order_total = 0 
#calculate total order price
item_1 = input("please enter the name of the item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print (f"ordered item {item_1} is not available. please order something else")

another_order = input("Do you want to add another item ? (yes/no)")
if another_order == "yes" :
    item_2 = input("please enter the name of second item : ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your order")

    else:
        print (f"ordered item {item_2} is not available. please order something else")
print(f"the total amount for order is {order_total}")


