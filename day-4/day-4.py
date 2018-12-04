import datetime

def make_histogram(guard_shifts):
    histogram = [0] * 60
    for shift in guard_shifts:
        histogram = map(lambda x: sum(x), zip(histogram, shift))

    return list(histogram)


def main():
    with open("input") as input_file:
        raw_input = input_file.readlines()

    rows = map(
        lambda row: row.strip().replace("[", "").split("] "),
        raw_input
    )
    rows = sorted(rows, key=lambda row: row[0])

    guards = part_1(rows)
    part_2(guards)


def part_1(rows: list):
    guards = dict()

    curr_guard = None
    last_asleep_min = None

    for row in rows:
        if row[1][:5] == "Guard":
            curr_guard = int(row[1].split(" ")[1][1:])

            if curr_guard in guards:
                guards[curr_guard].append([False] * 60)
            else:
                guards[curr_guard] = [[False] * 60]
        elif row[1] == "falls asleep":
            last_asleep_min = int(row[0][-2:])
        elif row[1] == 'wakes up':
            wake_up_min = int(row[0][-2:])

            for i in range(last_asleep_min, wake_up_min):
                guards[curr_guard][-1][i] = True

    sleep_times = dict()
    for (guard, shifts) in guards.items():
        total_sleep = 0

        for shift in shifts:
            total_sleep += sum(shift)

        sleep_times[guard] = total_sleep

    most_sleepy_guard = max(sleep_times.items(), key=lambda x: x[1])[0]

    histogram = make_histogram(guards[most_sleepy_guard])

    histogram = list(histogram)
    most_sleepy_minute = histogram.index(max(histogram))

    result = most_sleepy_guard * most_sleepy_minute

    print("Part 1:")
    print(f"-> Most sleepy guard: {most_sleepy_guard}")
    print(f"-> Most sleepy minute: {most_sleepy_minute}")
    print(f"-> {most_sleepy_guard} * {most_sleepy_minute} = {result}")

    return guards

def part_2(guards):
    histograms = {id: make_histogram(shifts) for (id, shifts) in guards.items() }
    histograms = {id: (max(histogram), histogram) for (id, histogram) in histograms.items() }
    most_sleepy = max(histograms.items(), key=lambda x: x[1][0])

    most_sleepy_guard = most_sleepy[0]
    most_sleepy_minute = most_sleepy[1][1].index(most_sleepy[1][0])

    result = most_sleepy_guard * most_sleepy_minute

    print("Part 2:")
    print(f"-> Most sleepy guard: {most_sleepy_guard}")
    print(f"-> Most sleepy minute: {most_sleepy_minute}")
    print(f"-> {most_sleepy_guard} * {most_sleepy_minute} = {result}")



if __name__ == "__main__":
    main()
