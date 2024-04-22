import re
import matplotlib.pyplot as plt
import numpy as np

def process(file):
    with open(file, 'r') as file:
        data = file.read()
    pattern = r'Copy:\s+(\d+\.\d+)'
    matches = re.findall(pattern, data)
    bandwidths = [float(match) for match in matches]
    groupedBandwidth = [bandwidths[i:i+5] for i in range(0, len(bandwidths), 5)]
    means = np.mean(groupedBandwidth, axis=1)
    std = np.std(groupedBandwidth, axis=1)
    return means, std

means1, std1 = process('result1.txt')
means32, std32 = process('result32.txt')
means64, std64 = process('result64.txt')
means128, std128 = process('result128.txt')

fig, ax = plt.subplots()
indices = np.arange(4)
width = 0.5

ax.bar(indices[0], means1, width, yerr=std1, color='b', label='1 Thread')
ax.bar(indices[1], means32, width, yerr=std32, color='r', label='32 Threads')
ax.bar(indices[2], means64, width, yerr=std64, color='g', label='64 Threads')
ax.bar(indices[3], means128, width, yerr=std128, color='y', label='128 Threads')

ax.set_xticks(indices)
ax.set_xticklabels(['1 Thread', '32 Threads', '64 Threads', '128 Threads'])
ax.set_ylabel('Bandwidth (MB/s)')
ax.set_title('Bandwidths of Copy Operations')

plt.show()
