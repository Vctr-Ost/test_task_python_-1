import schedule
import time
import datetime
import json
from api_usage import installs, costs, events, orders


def daily_run():

    yesterday_str = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    dt = {"date": yesterday_str}

    try:
        installs.installs_fn(dt)
        costs.costs_fn(dt)
        orders.orders_fn(dt)
        events.events_fn(dt)
        
    except json.JSONDecodeError as e:
        print(f"[INFO] No Data for {yesterday_str}\n       JSON decoding error: {e}")
    


def main():

    schedule.every().day.at('01:38').do(daily_run)      #  -2 hours (UTC)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
