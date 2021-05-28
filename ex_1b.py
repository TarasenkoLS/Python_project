class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, my_f):
        with open(my_f, encoding="utf-8") as f:
            for line in f:
                list_date = map(int, line.split("-"))
                d, m, y = list_date
                return cls(d, m, y)

    @staticmethod
    def get_isdate(obj):
        result = "not valid date"
        days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if 1 <= obj.month <= 12:
            if (1 <= obj.day <= days_month[obj.month - 1]) and (2018 < obj.year <= 2022):
                result = "valid date"
        return f"[{obj.day}.{obj.month}.{obj.year} - {result}"


one = Date.set_date('text_1.txt')
print(Date.get_isdate(one))
