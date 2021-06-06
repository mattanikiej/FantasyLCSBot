import datetime


class Day:
    def __init__(self):
        # mon, tues, wed, thu, fri, sat, sun
        self.days = [False, False, False, False, False, False, False]

    # These utility functions have repeated code,
    # but it's much easier to work with in other docs if they're written like this

    def check_monday(self):
        """
        Checks if the current day of week is a Monday
        :return: True if today is Monday, False otherwise
        """
        weekday = datetime.datetime.today().weekday()
        if weekday == 0:
            if not self.days[0]:
                # set Monday to True
                self.days[0] = True
                return True

            # resets rest of week to be False
            for i in range(7):
                # sets Monday to True
                if i == 0:
                    self.days[i] = True
                else:
                    self.days[i] = False
        return False

    def check_tuesday(self):
        """
        Checks if the current day of week is a Tuesday
        :return: True if today is Tuesday, False otherwise
        """
        weekday = datetime.datetime.today().weekday()
        if weekday == 1:
            if not self.days[1]:
                # set Monday to True
                self.days[1] = True
                return True

            # resets rest of week to be False
            for i in range(7):
                # sets Tuesday to True
                if i == 1:
                    self.days[i] = True
                else:
                    self.days[i] = False
        return False

    def check_friday(self):
        """
        Checks if the current day of week is a Friday
        :return: True if today is Friday, False otherwise
        """
        weekday = datetime.datetime.today().weekday()
        if weekday == 4:
            if not self.days[4]:
                # set Friday to True
                self.days[4] = True
                return True

            # resets rest of week to be False
            for i in range(7):
                # sets Friday to True
                if i == 5:
                    self.days[i] = True
                else:
                    self.days[i] = False
        return False

    def check_saturday(self):
        """
        Checks if the current day of week is a Saturday
        :return: True if today is Saturday, False otherwise
        """
        weekday = datetime.datetime.today().weekday()
        if weekday == 5:
            if not self.days[5]:
                # set Saturday to True
                self.days[5] = True
                return True

            # resets rest of week to be False
            for i in range(7):
                # sets Saturday to True
                if i == 5:
                    self.days[i] = True
                else:
                    self.days[i] = False
        return False

    def check_sunday(self):
        """
        Checks if the current day of week is a Sunday
        :return: True if today is Sunday, False otherwise
        """
        weekday = datetime.datetime.today().weekday()
        if weekday == 6:
            if not self.days[6]:
                # set Sunday to True
                self.days[6] = True
                return True

            # resets rest of week to be False
            for i in range(7):
                # sets Sunday to True
                if i == 6:
                    self.days[i] = True
                else:
                    self.days[i] = False
        return False
