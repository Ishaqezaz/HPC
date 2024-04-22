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

meansGuided, stdGuided = process('guided.txt')
meansDynamic, stdDynamic = process('dynamic.txt')
meansStatic, stdStatic = process('static.txt')


fig, ax = plt.subplots()
indices = np.arange(3)
width = 0.5

ax.bar(indices[0], meansGuided, width, yerr=stdGuided, color='b', label='1 Thread')
ax.bar(indices[1], meansDynamic, width, yerr=stdDynamic, color='r', label='32 Threads')
ax.bar(indices[2], meansStatic, width, yerr=stdStatic, color='g', label='64 Threads')

ax.set_xticks(indices)
ax.set_xticklabels(['Guided', 'Dynamic', 'Static'])
ax.set_ylabel('Bandwidth (MB/s)')
ax.set_title('Bandwidths of Copy Operations')
ax.set_yscale('log')

plt.show()
