import bisect
import re

class Guard:
    number_of_times_asleep_in_each_minute = None # because of the way Python works, we must instantiate this dict outside of the class
    minute_most_asleep = 0
    number_of_times_asleep_in_most_slept_minute = 0

def main():
    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        events = []

        for line in lines:
            bisect.insort(events, line)
        
        # find the guard who is most frequently asleep on any particular minute
        guards = {}

        guard = None
        start_sleep_time = None

        for event in events:
            action = event[19:-1]

            if action[:5] == "Guard":
                m = re.search(r"Guard #(\d+) begins shift", action)
                guard = int(m.group(1))
                if not guard in guards:
                    guards[guard] = Guard()
                    guards[guard].number_of_times_asleep_in_each_minute = {} # we must instantiate this here because otherwise it overwrites the dict in other class instances
                    for i in range(60):
                        guards[guard].number_of_times_asleep_in_each_minute[i] = 0
            elif action == "falls asleep":
                start_sleep_time = int(event[15:17])
            elif action == "wakes up":
                end_sleep_time = int(event[15:17])

                for i in range(start_sleep_time, end_sleep_time):
                    guards[guard].number_of_times_asleep_in_each_minute[i] += 1
                    if guards[guard].number_of_times_asleep_in_each_minute[i] > guards[guard].number_of_times_asleep_in_most_slept_minute:
                        guards[guard].number_of_times_asleep_in_most_slept_minute = guards[guard].number_of_times_asleep_in_each_minute[i]
                        guards[guard].minute_most_asleep = i

        # most_sleepy_guard = max(guards.items(), key=lambda a: a[1].total_minutes_asleep)
        # print(most_sleepy_guard[0] * max(most_sleepy_guard[1].number_of_times_asleep_in_each_minute.items(), key=lambda a: a[1])[0])

        most_consistent_sleeper = max(guards.items(), key=lambda a: a[1].number_of_times_asleep_in_most_slept_minute)
        print(most_consistent_sleeper[0] * most_consistent_sleeper[1].minute_most_asleep)

if __name__ == "__main__":
    main()
