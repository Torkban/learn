from smartphone import Smartphone

catalog = [Smartphone("Huawei","bn1","+79884444444"),Smartphone("Xiaomi","bn2","+79881111111"), Smartphone("iPhone","12","+79886666665"),Smartphone("Honor","bn4","+79887777777"),Smartphone("iPhone","BNM","+79889999999"),]

for i in range(0,5):
    print(catalog[i].phone_brand + " - " + catalog[i].phone_model + ". " + catalog[i].users_number)