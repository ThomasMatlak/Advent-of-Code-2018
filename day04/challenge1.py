import bisect
import re

class Guard:
    number_of_times_asleep_in_each_minute = None # because of the way Python works, we must instantiate this dict outside of the class
    total_minutes_asleep = 0

def main():
    with open("input.txt", "r") as inputfile:
        lines = inputfile.readlines()

        events = []

        for line in lines:
            bisect.insort(events, line)
        
        # find the guard with the most minutes asleep, and which minute they are most frequently asleep
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
                sleep_time = end_sleep_time - start_sleep_time

                guards[guard].total_minutes_asleep += sleep_time

                for i in range(start_sleep_time, end_sleep_time):
                    guards[guard].number_of_times_asleep_in_each_minute[i] += 1

        most_sleepy_guard = max(guards.items(), key=lambda a: a[1].total_minutes_asleep)

        print(most_sleepy_guard[0] * max(most_sleepy_guard[1].number_of_times_asleep_in_each_minute.items(), key=lambda a: a[1])[0])

if __name__ == "__main__":
    main()
