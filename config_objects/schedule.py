import datetime as dt
from config_objects.cronjob import Cronjob


class Schedule:

    def __init__(self, current_time: str):
        try:
            self.current_time = dt.time(hour=int(current_time[:2]), minute=int(current_time[3:]))
        except ValueError:
            print("Command line argument 't' must be expressed in 24 hour format! "
                  "Values need to be between [0-23:0-59] only")
            exit()
        else:
            self.current_time = dt.time(hour=int(current_time[:2]), minute=int(current_time[3:]))
        self.schedule = []
        # Current datetime
        self.current_datetime = dt.datetime.combine(dt.datetime.today(),
                                                    time=dt.time(hour=int(current_time[:2]),
                                                                 minute=int(current_time[3:])))

    # Parse the input from the command line
    def parse_stdin(self, stdin):
        # Empty list to append all the cronjobs later on
        cron_list = []

        for line in stdin:
            tmp_list = line.split(' ')
            cronjob = Cronjob(tmp_list[0], tmp_list[1], tmp_list[2], self.current_time)
            cron_list.append(cronjob)

        for cronjob in cron_list:
            scheduled_datetime = dt.datetime.combine(dt.datetime.today(),
                                                 time=dt.time(hour=cronjob.hour, minute=cronjob.minute))
            if scheduled_datetime < self.current_datetime:
                scheduled_datetime = scheduled_datetime + dt.timedelta(days=1)

            self.schedule.append({
                'Cronjob': cronjob,
                'Day': 'Today' if scheduled_datetime.date() == self.current_datetime.date() else 'Tomorrow',
                'Time': scheduled_datetime.time()
            })

    def print_schedule(self):
        for item in self.schedule:
            print(item['Time'].strftime('%H:%M'), item['Day'], '-', item['Cronjob'].script)
