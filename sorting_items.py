general_items = ["Banana", "toyota", "laptop", "generator", "ticket"]
general_items.sort()

for index, item in enumerate(general_items) :
    row = f"{index + 1}.{item.capitalize()}"
    print(row)