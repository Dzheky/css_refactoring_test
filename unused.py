import json
import os
# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to extract relevant metrics (FCP, LCP, Speed Index)
def extract_metrics(data):
    fcp = []
    lcp = []
    speed_index = []

    # Loop through each run and extract metrics
    for run in data:
        fcp.append(run['audits']['first-contentful-paint']['numericValue'])
        lcp.append(run['audits']['largest-contentful-paint']['numericValue'])
        speed_index.append(run['audits']['speed-index']['numericValue'])

    return {
        'fcp': fcp,
        'lcp': lcp,
        'speed_index': speed_index
    }

# Function to calculate average of a list
def calculate_average(metrics):
    return sum(metrics) / len(metrics)

# Load unoptimized and optimized results from files
unoptimized_file = os.path.join(os.path.dirname(__file__), 'static_unoptimized_results.json')
optimized_file = os.path.join(os.path.dirname(__file__), 'scoped_css', 'static_optimized_results.json')

unoptimized_data = load_json(unoptimized_file)
optimized_data = load_json(optimized_file)

# Extract metrics from both datasets
unoptimized_metrics = extract_metrics(unoptimized_data)
optimized_metrics = extract_metrics(optimized_data)

# Example: Calculate and print the average for each metric (Unoptimized)
print("Unoptimized Metrics Averages:")
print(f"FCP: {calculate_average(unoptimized_metrics['fcp']):.2f} ms")
print(f"LCP: {calculate_average(unoptimized_metrics['lcp']):.2f} ms")
print(f"Speed Index: {calculate_average(unoptimized_metrics['speed_index']):.2f} ms")

# Example: Calculate and print the average for each metric (Optimized)
print("\nOptimized Metrics Averages:")
print(f"FCP: {calculate_average(optimized_metrics['fcp']):.2f} ms")
print(f"LCP: {calculate_average(optimized_metrics['lcp']):.2f} ms")
print(f"Speed Index: {calculate_average(optimized_metrics['speed_index']):.2f} ms")
