# Generate Dataset:
import numpy as np

# Generate heights and weights data
np.random.seed(0)  # for reproducibility
heights = np.random.normal(170, 10, 50)  # mean=170, std=10
weights = np.random.normal(70, 5, 50)    # mean=70, std=5

# Combine heights and weights into a dataset
dataset = np.column_stack((heights, weights))
# Descriptive Statistics:

# Calculate mean, median, std, and range for both variables
heights_mean = np.mean(heights)
heights_median = np.median(heights)
heights_std = np.std(heights)
heights_range = np.max(heights) - np.min(heights)

weights_mean = np.mean(weights)
weights_median = np.median(weights)
weights_std = np.std(weights)
weights_range = np.max(weights) - np.min(weights)
# Probability:
# Probability of a person being taller than 175 cm
probability_taller_than_175 = np.sum(heights > 175) / len(heights)
# Distributions:

import matplotlib.pyplot as plt

# Plot histograms
plt.hist(heights, bins=10, color='blue', alpha=0.5, label='Heights')
plt.hist(weights, bins=10, color='green', alpha=0.5, label='Weights')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Heights and Weights')
plt.legend()
plt.show()


# Inferential Statistics - Central Limit Theorem (CLT):

sample_means = [np.mean(np.random.choice(heights, size=30)) for _ in range(1000)]
plt.hist(sample_means, bins=30, color='orange', alpha=0.7)
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.title('Distribution of Sample Means')
plt.show()

# Confidence Intervals (CI):

import scipy.stats as stats

# Calculate confidence interval for heights
ci_heights = stats.norm.interval(0.95, loc=np.mean(heights), scale=np.std(heights)/np.sqrt(len(heights)))
# Hypothesis Testing:

# For example, testing if the mean height is different from 170 cm
t_statistic, p_value = stats.ttest_1samp(heights, 170)
Interpret the results and decide whether to reject the null hypothesis.