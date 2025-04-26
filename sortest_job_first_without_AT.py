def sort_by_burst_time(processes):
    return sorted(processes, key=lambda x: x[1])


def calculate_waiting_times(processes):
    waiting_times = [0] * len(processes)
    for i in range(1, len(processes)):
        waiting_times[i] = waiting_times[i - 1] + processes[i - 1][1]
    return waiting_times

def calculate_completion_times(processes, waiting_times):
    completion_times = [0] * len(processes)
    for i in range(len(processes)):
        completion_times[i] = waiting_times[i] + processes[i][1]
    return completion_times

def calculate_turnaround_times(processes, waiting_times):
    turnaround_times = [0] * len(processes)
    for i in range(len(processes)):
        turnaround_times[i] = waiting_times[i] + processes[i][1]
    return turnaround_times


def print_process_table(processes, waiting_times, turnaround_times, completion_times):
    print("Process\t\tBT\t\tCT\t\tWT\t\tTAT")
    for i in range(len(processes)):
        pid, bt = processes[i]
        print(f"\tP{pid}\t\t{bt}\t\t{completion_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")



def calculate_and_print_averages(waiting_times, turnaround_times):
    n = len(waiting_times)
    avg_wt = sum(waiting_times) / n
    avg_tat = sum(turnaround_times) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


def sjn_scheduling(burst_times):
    processes = [(i + 1, bt) for i, bt in enumerate(burst_times)]
    sorted_processes = sort_by_burst_time(processes)

    waiting_times = calculate_waiting_times(sorted_processes)
    turnaround_times = calculate_turnaround_times(sorted_processes, waiting_times)
    completion_times = calculate_completion_times(sorted_processes, waiting_times)

    print_process_table(sorted_processes, waiting_times, turnaround_times, completion_times)
    calculate_and_print_averages(waiting_times, turnaround_times)



if __name__ == "__main__":
    burst_times = [140, 75, 320, 280, 125]

    print("=== Shortest Job Next (SJN) Scheduling ===\n")
    sjn_scheduling(burst_times)
