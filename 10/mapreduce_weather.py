import csv
from collections import defaultdict

# Simulate MapReduce using Python functions

# Step 1: Map → extract (year, temp)
def map_function(filename):
    mapped_data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            date = row['date']
            temp = float(row['temp'])
            year = date.split('-')[0]
            mapped_data.append((year, temp))
    return mapped_data

# Step 2: Shuffle → group by year
def shuffle(mapped_data):
    grouped = defaultdict(list)
    for year, temp in mapped_data:
        grouped[year].append(temp)
    return grouped

# Step 3: Reduce → find max/min temp per year
def reduce(grouped_data):
    yearly_stats = {}
    for year, temps in grouped_data.items():
        yearly_stats[year] = {
            'max': max(temps),
            'min': min(temps),
            'avg': sum(temps)/len(temps)
        }
    return yearly_stats

# Step 4: Find coolest and hottest year
def find_extremes(stats):
    coolest = min(stats.items(), key=lambda x: x[1]['min'])
    hottest = max(stats.items(), key=lambda x: x[1]['max'])
    return coolest, hottest

# 🔁 Run the MapReduce Pipeline
def run_pipeline(filename):
    mapped = map_function(filename)
    grouped = shuffle(mapped)
    stats = reduce(grouped)
    coolest, hottest = find_extremes(stats)

    print("\n📊 Yearly Temperature Stats:")
    for year, val in stats.items():
        print(f"{year} → Max: {val['max']}°C | Min: {val['min']}°C | Avg: {val['avg']:.2f}°C")

    print(f"\n❄️ Coolest Year: {coolest[0]} → {coolest[1]['min']}°C")
    print(f"☀️ Hottest Year: {hottest[0]} → {hottest[1]['max']}°C")

# Run with your CSV
# run_pipeline('weather_data.csv')
run_pipeline('/Users/rutulbhosale/Desktop/CL-3/10/weather_data.csv')


