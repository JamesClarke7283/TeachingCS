import argparse

from datetime import datetime, timedelta, timezone

parser = argparse.ArgumentParser(description="Get the current time and other info")

parser.add_argument('--get-time',
                    help='Get current time', action='store_true')

parser.add_argument('--offset',
                    help='Set UTC offset', action='store', type=int)

parser.add_argument('--set-date',
                    help='Set the date in %d %m %y', action='extend', nargs=3)

args = parser.parse_args()
print(args)


if args.get_time:
    if args.offset:
        tz = timezone(timedelta(hours=args.offset))
        dt = datetime.now(tz)
    else:
        dt = datetime.now()

if args.set_date:
    int_list = list(map(int, args.set_date))
    int_list_reversed = int_list[::-1]
    dt = datetime(*int_list)
    print(dt)

print(args.set_date)
