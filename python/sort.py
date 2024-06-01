products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

products.sort(key=lambda x: x[0])

for product in products:
    print(product)

products2 = sorted(products, key=lambda x: x[1])

print(products2)


def sort_by_price(items: list):
    def order_by_price(item: tuple):
        return item[1]
    # use the order_by_price function here
    return sorted(items, key=order_by_price)

products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

for product in sort_by_price(products):
    print(product)


def sort_by_seasons(shows):
    return sorted(shows, key=lambda show: show["seasons"], reverse=True)


shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

for show in sort_by_seasons(shows):
    print(f"{show['name']} {show['seasons']} seasons")