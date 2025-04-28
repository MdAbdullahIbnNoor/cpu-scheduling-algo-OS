# Taking user input for arrival time and burst time only
n = int(input("Enter the number of processes: "))
arrival = []
burst = []

# Get arrival time and burst time for each process
for i in range(n):
    a = int(input(f"Enter arrival time for P{i+1}: "))
    arrival.append(a)
    b = int(input(f"Enter burst time for P{i+1}: "))
    burst.append(b)

# Automatically assigning process numbers as P1, P2, P3, etc.
processes = [i + 1 for i in range(n)]  # P1, P2, P3, ..., Pn

# Initializing variables
rem = burst[:]
wait = [0] * n
added = [False] * n
q = []
tq = int(input("Enter time quantum: "))  # User input for time quantum
time = 0

# Round Robin Scheduling Logic
while any(rem):
    # print(f"Time: {time}, Remaining: {rem}")  # Debugging line
    for i in range(n):
        if arrival[i] <= time and not added[i]:
            q.append(i)
            added[i] = True
    if q:
        i = q.pop(0)
        # print(f"Processing: P{processes[i]}")  # Debugging line
        if rem[i] > tq:
            time += tq
            rem[i] -= tq
        else:
            time += rem[i]
            wait[i] = time - arrival[i] - burst[i]
            rem[i] = 0
        for j in range(n):
            if arrival[j] <= time and not added[j]:
                q.append(j)
    else:
        time += 1
    # print(f"Remaining Burst Times: {rem}")  # Debugging line

# Output results
for i in range(n):
    print(f"P{processes[i]} Arrival:{arrival[i]} Burst:{burst[i]} Waiting:{wait[i]}")
