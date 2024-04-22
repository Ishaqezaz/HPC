import matplotlib.pyplot as plt

def read_performance_data(filename):
    thread_counts = []
    execution_times = []

    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if 'threads:' in line:
                thread_count = int(line.split()[0])
                thread_counts.append(thread_count)
                # Read the next line to get the execution time
                execution_time_line = file.readline()
                execution_time = float(execution_time_line.split()[3])
                execution_times.append(execution_time)
                # Skip the standard deviation line
                file.readline()

    return thread_counts, execution_times

# Load data from file
thread_counts, execution_times = read_performance_data('results.txt')

# Calculate speed-up
base_time = execution_times[0]
speed_up = [base_time / time for time in execution_times]

# Create indices for each thread count to make sure x-axis is evenly spaced
indices = range(len(thread_counts))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(indices, speed_up, marker='o', linestyle='-', color='g')  # Use indices for x-axis positions
plt.xlabel('Number of Threads')
plt.ylabel('Speed-Up')
plt.title('Speed-Up vs. Number of Threads')
plt.xticks(indices, thread_counts)  # Set the ticks to be evenly spaced, labeled with thread counts
plt.show()
