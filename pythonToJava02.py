def area_of_circle(radius):
    pi = 3.14159
    return pi * radius ** 2

def volume_of_tire(radius, depth):
    return area_of_circle(radius) * depth

cost_per_cubic = 225.50
cost_saving_ratio = 0.10
max_saving_ratio = 0.50 ;
tire_radius = 1.2
tire_depth = 0.4

for i in range(1, 10):
    capital = i * 1000
    num_pieces = 0
    saving = cost_saving_ratio
    while capital > 0.0 :
        cost = volume_of_tire(tire_radius, tire_depth) * cost_per_cubic
        cost *= 1.0 - saving
        if saving < max_saving_ratio:
            saving = saving * (1.0 + cost_saving_ratio)
        else:
            saving = max_saving_ratio
        if cost <= capital:
            num_pieces += 1
            capital -= cost
        else:
            break
    print ("Capital : " + str(i * 1000) + " -> " + str(num_pieces) + "tires.")
