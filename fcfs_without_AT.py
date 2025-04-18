
def findCompletionTime(processes, n, bt, ct):
    ct[0] = bt[0]
    for i in range(1, n):
        ct[i] = ct[i - 1] + bt[i]

def findWaitingTime(processes, n, bt, wt, ct):
    for i in range(n):
        wt[i] = ct[i] - bt[i]

def findTurnAroundTime(processes, n, bt, wt, tat):
    # calculating turnaround time by adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    total_wt = 0
    total_tat = 0


    findCompletionTime(processes, n, bt, ct)

    findWaitingTime(processes, n, bt, wt, ct)

    findTurnAroundTime(processes, n, bt, wt, tat)

    print("Proc    B.T     C.T    W.T      TAT")

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f" {i + 1}\t\t{bt[i]}\t\t{ct[i]}\t\t{wt[i]}\t\t{tat[i]}")

    print(f"Average waiting time = {total_wt / n}")
    print(f"Average turn around time = {total_tat / n}")


if __name__ == "__main__":
    # process id's
    processes = [1, 2, 3]
    n = len(processes)

    # Burst time of all processes
    burst_time = [10, 5, 8]

    findavgTime(processes, n, burst_time)


