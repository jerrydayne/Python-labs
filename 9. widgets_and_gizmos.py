widgets_order = int(input("how many widgets did you order for : "))
gizmo_order = int(input("how many giznos did you order : "))

widgets_total_weight = 75 * widgets_order
gizmos_total_weight = 112 * gizmo_order

total_order_weight = widgets_total_weight + gizmos_total_weight

print("This order has",total_order_weight,"grams in total")