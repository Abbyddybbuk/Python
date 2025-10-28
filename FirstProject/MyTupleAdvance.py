myPriceLIst = [('Apple', 80), ('Banana', 30), ('Mango', 100), ('Grapes', 60), ('Orange', 50), ('Pineapple', 90), ('Strawberry', 150),
                ('Watermelon', 40), ('Papaya', 70), ('Avacado', 1000), ('Kiwi', 120), ('Blueberry', 200), ('Raspberry', 180)]

for (fruit, price) in myPriceLIst:#tuple unpacking in for loop
    print(f"The price of {fruit} is {price + (price * 0.1)} INR")   


def check_most_pricey(priceList):
    maxPrice = 0
    mostPriceyFruit = ""
    for (fruit, price) in priceList:
        if price > maxPrice:
            maxPrice = price
            mostPriceyFruit = fruit
        else:
            pass    
    return (mostPriceyFruit, maxPrice)    

mostPricey = check_most_pricey(myPriceLIst)
print(f"The most pricey fruit is {mostPricey[0]} with price {mostPricey[1]} INR")

fruit, price = check_most_pricey(myPriceLIst)
print(f"The MOST pricey fruit is {fruit} with price {price} INR")