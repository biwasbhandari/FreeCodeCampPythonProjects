def add_time(start, duration, starting_day=None):
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))
    if period == 'PM':
        start_hour += 12

    # Calculate total hours and minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Adjust total hours and minutes
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60

    new_period = 'AM'
    if new_hour >= 12:
        new_period = 'PM'
    if new_hour >= 24:
        new_hour -= 24
    
    if new_hour > 12:
        new_hour -= 12
        new_period = 'PM'
    elif new_hour == 12:
        new_period = 'PM'
    elif new_hour == 0:
        new_hour = 12
    
    day_change = ""
    if starting_day is not None:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        starting_day_index = days.index(starting_day.lower().capitalize())
        new_day_index = (starting_day_index + (total_minutes // (24 * 60))) % 7
        day_change = f", {days[new_day_index]}"
    
    days_later = total_minutes // (24 * 60)
    days_later_text = ""
    if days_later == 1:
        days_later_text = " (next day)"
    elif days_later > 1:
        days_later_text = f" ({days_later} days later)"
    new_time = f"{new_hour}:{new_minute:02} {new_period}{day_change}{days_later_text}"
    return new_time
        


print(add_time('3:30 PM', '2:12'))  
print(add_time('11:55 AM', '3:12'))  
print(add_time('2:59 AM', '24:00'))  
print(add_time('11:59 PM', '24:05'))  
print(add_time('8:16 PM', '466:02'))  
print(add_time('3:30 PM', '2:12', 'Monday'))  
print(add_time('2:59 AM', '24:00', 'saturDay'))  
print(add_time('11:59 PM', '24:05', 'Wednesday'))  
print(add_time('8:16 PM', '466:02', 'tuesday')) 
