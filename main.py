#!/usr/bin/env python3
import sys
import argparse
from config_objects.schedule import Schedule


def main():
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('t', help='Indicate the current time in HH:MM format (24 hour format)')
    # Execute parse_args()
    args = parser.parse_args()

    # Create Schedule to parse cronjobs from stdin
    schedule = Schedule(args.t)
    schedule.parse_stdin(sys.stdin)
    # Print out Cronjob Schedule
    schedule.print_schedule()


if __name__ == "__main__":
    main()
