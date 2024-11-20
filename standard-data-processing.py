
ford_object = {
    "make": "Ford",
    "model": "Fiesta",
}

car_objects = []

car_objects.append(ford_object)
car_objects.append({ "make": "Ferrari", "model": "F40"})

for car in car_objects:
    print(car["make"])

car_objects[1]["make"] = "Porsche"

for car in car_objects:
    print(car["make"])

print(len(car_objects.len))

