liters = input("Enter liters : ")


def liters_to_m3(liters):
    m3 = int(liters) * 1000

    return m3


cubic_meters = liters_to_m3(liters)
if cubic_meters > 100:
    print("we can tavel")
else: print("lets get more fuel")