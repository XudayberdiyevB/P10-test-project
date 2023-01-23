import csv


class Computer:
    def __init__(self, name, color, cost, brand_name, made_country, made_year):
        self.name = name
        self.cost = cost
        self.color = color
        self.brand_name = brand_name
        self.made_country = made_country
        self.made_year = made_year

    def get_main_info(self):
        return f"Computer name : {self.name}\n" \
               f"Computer color : {self.color}\n" \
               f"Computer cost : {self.cost}\n" \
               f"Computer Type; Brand name : {self.brand_name}\n" \
               f"Country of made Computer : {self.made_country}\n" \
               f"Computer made year : {self.made_year}\n"


class Laptop(Computer):
    def __init__(self, name, color, cost, brand_name, made_country, made_year, type_keyboard, keyboard_length):
        super().__init__(name, color, cost, brand_name, made_country, made_year)
        self.type_keyboard = type_keyboard
        self.keyboard_length = keyboard_length

    def get_laptop_info(self):
        return f"{self.get_main_info()}" \
               f"Computer keyboard type : {self.type_keyboard}\n" \
               f"Computer keyboard type(length) : {self.keyboard_length}\n"


laptop_objs = []
csv_file_path = "laptops.csv"

with open(csv_file_path) as f:
    csv_laptops_data = csv.DictReader(f)

    for laptop in csv_laptops_data:
        laptop_objs.append(
            Laptop(
                laptop.get("name"), laptop.get("price"), laptop.get("color"), laptop.get("brand"),
                laptop.get("created_year"),
                laptop.get("made_in"), laptop.get("type_keyboard"), laptop.get("keyboard_length")
            )
        )

header = ["name", "cost", "color", "brand_name", "made_year", "made_country", "type_keyboard", "keyboard_length"]

laptops_data = [
    {
        "name": "HP core i7",
        "cost": 700,
        "color": "black",
        "brand_name": "HP",
        "made_year": 2022,
        "made_country": "USA",
        "type_keyboard": "v",
        "keyboard_length": 20
    },
    {
        "name": "HP core i7",
        "cost": 700,
        "color": "black",
        "brand_name": "HP",
        "made_year": 2022,
        "made_country": "USA",
        "type_keyboard": "v",
        "keyboard_length": 20
    }
]

for laptop_data in laptops_data:
    laptop_objs.append(
        Laptop(
            laptop.get("name"), laptop.get("price"), laptop.get("color"), laptop.get("brand"),
            laptop.get("created_year"),
            laptop.get("made_in"), laptop.get("type_keyboard"), laptop.get("keyboard_length")
        )
    )

with open(csv_file_path, "a", newline="\n") as f:
    # laptops_data[0].update({"name": f"\n{laptops_data[0].get('name')}"})
    csv_writer = csv.DictWriter(f, header)
    csv_writer.writerows(laptops_data)
