class AirLine:

    def __init__(self, destination, number, time, days):
        self.destination = destination
        self.number = number
        self._type_air = 'Тушка'
        self.time = time
        self.days = days

    def dest(self):
        return self.destination

    def num(self):
        return self.number

    def type(self):
        return self._type_air

    def time_f(self):
        return self.time

    def day(self):
        return self.days


new_line = [AirLine('москва', '№47', '17:20', 'вторник'),
            AirLine('киев', '№497', '12:50', 'четверг'),
            AirLine('москва', '№89', '12:20', 'среда'),
            AirLine('вильнюс', '№784', '17:20', 'пятница'),
            AirLine('вильнюс', '№437', '12:40', 'среда'),
            AirLine('варшава', '№987', '19:20', 'понедельник'),
            AirLine('варшава', '№44', '10:30', 'суббота')]
leng = 0
ind = 0

p = input('Введите пункт назначения или день вылета: ')
while leng < len(new_line):
    leng += 1
    if new_line[ind].destination == p or new_line[ind].day() == p:
        print(new_line[ind].type(), 'за номером: ', new_line[ind].num(), ' направлением ', new_line[ind].dest(),
              ' вылетает в ', new_line[ind].time_f(), '/', new_line[ind].day())
        ind += 1
    else:
        ind += 1
