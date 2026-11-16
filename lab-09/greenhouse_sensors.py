
import numpy as np
np.random.seed(7)

readings = np.random.randint(20, 41, size=(6, 3))

print("Sensor Readings:")
print(readings)

mean_values = readings.mean(axis=0)

print("Mean per sensor:", mean_values)

std_values = readings.std(axis=0)

standardized = (readings - mean_values) / std_values

normalized_mean = standardized.mean(axis=0)

print("Normalized column means:", normalized_mean.round(3))

max_hours = readings.argmax(axis=0)

print("Hour of max per sensor:", max_hours)

new_readings = np.vstack([readings, mean_values])

print("New shape:", new_readings.shape)

np.random.seed(7)

new_data = np.random.randint(20, 41, size=(6, 3))

print("Reproducible:", np.array_equal(readings, new_data))
