class Country:
    def __init__(self, file):
        self.file = file

    @staticmethod
    def get_value(line, column_index):
        return line.split(",")[column_index].split('"')[1].strip()

    def get_lines(self):
        with open(self.file) as f:
            return f.readlines()

    def get_column_values(self, column_name):
        lines = self.get_lines()
        column_index = None
        for column in self.get_columns():
            if column_name == column.get("column_name"):
                column_index = column.get("index")
        return [
            self.get_value(lines[i], column_index)
            for i in range(1, len(lines))
        ]

    def get_columns(self):
        try:
            column_names = self.get_lines()[0]
        except Exception:
            pass
        else:
            return [
                {"index": index, "column_name": column_name}
                for index, column_name in
                enumerate(column_names.split(","))
            ]


country = Country("countriasdes of the world.csv")
print(country.get_columns())
print(country.get_column_values("Region"))
