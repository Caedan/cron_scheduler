import datetime as dt


class Cronjob:

    def __init__(self, minute: [int, str], hour: [int, str], script: str, current_time: dt.time):
        # If hour equals '*' XOR minute equals '*'
        if bool(hour == '*') != bool(minute == '*'):
            # If asterisk is given, cronjob will fire every minute
            if minute == '*':
                # If minute is equals to current_time.minute and if , then fire next minute
                if current_time.hour == hour:
                    self.minute = int(current_time.minute)
                else:
                    self.minute = 0
            else:
                self.minute = int(minute)

            # If asterisk is given, cronjob will fire every hour
            if hour == '*':
                if current_time.minute <= self.minute:
                    self.hour = int(current_time.hour)
                else:
                    # If current_time.hour exceeds range [0-23] set hour to midnight
                    self.hour = int(current_time.hour + 1) if current_time.hour != 23 else 0
            else:
                self.hour = int(hour)
        # Else if both minute & hour are not '*'
        elif bool(hour != '*') and bool(minute != '*'):
            self.minute = int(minute)
            self.hour = int(hour)
        # Both minute & hour are '*'
        else:
            self.minute = int(current_time.minute)
            self.hour = int(current_time.hour)

        if script[-1] == '\n':
            self.script = script[:-1]
        else:
            self.script = script
