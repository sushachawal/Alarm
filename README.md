# Alarm

## Module Requirements
Requires the following modules:
- threading
- simpleaudio
- keyboard
- time
- sys
## How it works!

Run on command line with:

```python alarm.py <time> <units>```

For example to run the alarm for 10 minutes the command would be:

```python alarm.py 10 minutes```

Currently only supports seconds and minutes only and no combination of these so ```python alarm.py 10 minutes 13 seconds``` would **not** work!

On MacOS, `keyboard` might require administrator access and if the alarm is to be kept running for a long time (overnight), `caffeinate` is recommended:

``` sudo caffeinate python alarm.py <time> <units>```

**To switch the alarm off, press spacebar on your keyboard.**

## TODO

- Implement one of the threads as a daemon so that sound effect can be played continuously (unlike the 1s it plays for now) and interrupted properly by the key press
- Implement multiple units and hours.
- Build a GUI
