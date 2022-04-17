from aaaaa.static_method import Date1

class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

class SlashDates(Dates):
    def getDate(self):
        return Date1.toDashDate(self.date)

date = Dates('1-8-2021')
newdate = SlashDates('1/8/2021')

if(date.getDate() == newdate.getDate()):
    print('Dates are Equal')
else:
    print('Dates are Unequal')