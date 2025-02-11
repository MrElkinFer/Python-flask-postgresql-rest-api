import datetime


class DateFormat():
    @classmethod
    def covert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
