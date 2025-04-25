import random
import numpy as np

# Simulated dataset: [vibration, crack_length], 0 = healthy, 1 = damaged
data = [
    ([0.1, 0.2], 0),
    ([0.15, 0.25], 0),
    ([0.8, 0.9], 1),
    ([0.9, 0.85], 1),
    ([0.2, 0.3], 0),
    ([0.75, 0.8], 1),
    ([0.25, 0.4], 0),
    ([0.95, 0.95], 1)
]

# Parameters
NUM_DETECTORS = 10
THRESHOLD = 0.3  # Affinity threshold (Euclidean distance)

# Generate random detectors for class = 1 (damaged)
def generate_detectors():
    detectors = []
    while len(detectors) < NUM_DETECTORS:
        vec = [random.uniform(0, 1), random.uniform(0, 1)]
        if all(np.linalg.norm(np.array(vec) - np.array(f)) > THRESHOLD for f, label in data if label == 0):
            detectors.append(vec)
    return detectors

# Classify using detectors (if affinity < threshold → detected as damaged)
def classify(detectors, input_vec):
    for det in detectors:
        if np.linalg.norm(np.array(input_vec) - np.array(det)) < THRESHOLD:
            return 1  # Damaged
    return 0  # Healthy

# Train AIS
detectors = generate_detectors()

# Test classification
print("\n🔬 Structure Damage Classification:")
correct = 0
for features, label in data:
    pred = classify(detectors, features)
    status = "✅ Correct" if pred == label else "❌ Wrong"
    print(f"Features: {features} | Actual: {label} | Predicted: {pred} → {status}")
    correct += int(pred == label)

accuracy = (correct / len(data)) * 100
print(f"\n🎯 Accuracy: {accuracy:.2f}%")
