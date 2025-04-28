def calculate_waiting_time(processes, arrival_times, burst_times, time_quantum):
    n = len(processes)
    remaining_burst = burst_times.copy()
    waiting_time = [0] * n
    t = 0  # current time
    queue = []
    visited = [False] * n

    while True:
        # Add newly arrived processes to the queue
        for i in range(n):
            if arrival_times[i] <= t and not visited[i]:
                queue.append(i)
                visited[i] = True

        if queue:
            i = queue.pop(0)
            if remaining_burst[i] > time_quantum:
                t += time_quantum
                remaining_burst[i] = remaining_burst[i] - time_quantum
            else:
                t += remaining_burst[i]
                waiting_time[i] = t - arrival_times[i] - burst_times[i]
                remaining_burst[i] = 0

            # After executing, check if new processes have arrived
            for j in range(n):
                if arrival_times[j] <= t and not visited[j]:
                    queue.append(j)
                    visited[j] = True

            # If the process is not finished, put it back into the queue
            if remaining_burst[i] > 0:
                queue.append(i)
        else:
            # No process is ready yet, CPU is idle
            t += 1

        if all(rb == 0 for rb in remaining_burst):
            break

    return waiting_time

def calculate_turnaround_time(burst_times, waiting_time):
    return [burst_times[i] + waiting_time[i] for i in range(len(burst_times))]

def round_robin(processes, arrival_times, burst_times, time_quantum):
    waiting_time = calculate_waiting_time(processes, arrival_times, burst_times, time_quantum)
    turnaround_time = calculate_turnaround_time(burst_times, waiting_time)

    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"P{processes[i]}\t{arrival_times[i]}\t\t{burst_times[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Example usage
processes = [1, 2, 3, 4]
arrival_times = [0, 1, 2, 3]
burst_times = [5, 4, 2, 1]
time_quantum = 2

round_robin(processes, arrival_times, burst_times, time_quantum)
# Output:
# Process	Arrival Time	Burst Time	Waiting Time	Turnaround Time
