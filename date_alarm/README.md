This python script should be run via a cron job to check events that matches a certain date.
If current date matches an event, it will send a notification via notify-send with a delay of 5 sec as default.

`./date_alarm.py --calendar=/path/to/calendar`

The calendar file should contain all dates in the same format as presented in the calendar.example
