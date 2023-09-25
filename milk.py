
def min_jars(milk_amount, jars):
    if milk_amount == 0:
        return 0
    if milk_amount < 0:
        return float('inf')
    min_count = float('inf')
    for jar in jars:
        count = min_jars(milk_amount - jar, jars)
        if count != float('inf'):
            min_count = min(min_count, count + 1)
    return min_count

def get_min_jars(milk_amount):
    jars = [20, 50, 70]
    count = min_jars(milk_amount, jars)
    if count == float('inf'):
        return "Sorry !!! Cannot measure the required volume"
    return count

milk_amount = int(input("Enter the required quantity of milk in millilitres: "))
print(get_min_jars(milk_amount))
