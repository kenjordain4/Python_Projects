# Alarm Notifier

A small Python program that sends a desktop notification at the times you choose, once per day. By default it reminds you at 7:00 AM and 10:00 PM ("It's 10:00 PM, time to sleep").

## Files

- `dailyalarm.py`: main program. Checks the current time every 60 seconds and sends a notification when it matches an alarm time.
- `format_time.py`: helper with `format_input_time(hour, minute)`, which converts 24-hour time to 12-hour format with AM/PM (for example `22, 0` becomes `10:00 PM`).

## Requirements

- Python 3
- The `plyer` library for desktop notifications:

```
pip install plyer
```

## How to run

From the `Alarm_notifier` folder:

```
python dailyalarm.py
```

Keep the program running: it only sends notifications while it is open.

## How it works

1. `alarm(a, b)` takes an hour (`a`, 0-23) and a minute (`b`, 0-59).
2. Every 60 seconds it compares the current time to the alarm time.
3. When they match, it sends a notification and prints `Notification sent at <time>` in the terminal.
4. It remembers the date of the last notification so it does not send the same alarm twice on the same day, and resets that memory at midnight.

## Change the alarm times

At the bottom of `dailyalarm.py`, edit the `alarms` list with `(hour, minute)` pairs in 24-hour time:

```python
alarms = [(7, 0), (22, 0)]
```

## Concepts practiced

- Functions and modules (importing `format_input_time` from another file)
- `datetime` and `date` for working with time
- Infinite loops with `time.sleep`
- Third-party libraries (`plyer`)
