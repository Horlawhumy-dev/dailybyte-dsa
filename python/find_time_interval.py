

def find_time_before_the_bus_schedule(schedules, current):

    current_mins = (int(current.split(":")[0]) * 60) + (int(current.split(":")[1]))
    last_bus_mins = 0
    

    for schedule in schedules:

        schedule_time = (int(schedule.split(":")[0]) * 60) + (int(schedule.split(":")[1]))

        if schedule_time <= current_mins:

            last_bus_mins = schedule_time

    result = current_mins - last_bus_mins

    return -1 if result == 0 else result


schedules = ["12:30", "14:30", "19:55"]
target = "00:00"

print(find_time_before_the_bus_schedule(schedules, target))

