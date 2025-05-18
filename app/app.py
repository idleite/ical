import urllib.request
from icalendar import Calendar
def main(classes, name):
  # Split classes into  a list
  classes = classes.split("-")
  classes.append("Schoolwide")
  with urllib.request.urlopen("https://calendar.google.com/calendar/ical/c_n2eqesue9fli7n97mnknl82gmk%40group.calendar.google.com/public/basic.ics") as x:
    calendar = Calendar.from_ical(x.read())
  newCalendar = Calendar()
  for classes in classes:
    classes = classes.removeprefix(" ")
    classes = classes.replace("_", " ")
    for X in calendar.subcomponents:
        if X['SUMMARY'].find(classes) !=-1:
          newCalendar.add_component(X)
        else:
          continue
  for k, v in calendar.items():
    if k != "X-WR-CALNAME":
      newCalendar.add(k,v)
  newCalendar.add("X-WR-CALNAME",f"{name}'s Custom Calendar")
  calendarData = newCalendar.to_ical()
  return calendarData