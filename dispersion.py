from math import ceil, sqrt


def mean(sample):
    return sum(sample) / len(sample)

def median(sample):
    
    sorted_sample = sorted(sample)
    n = len(sample)
    
    if n % 2 == 0:
        mid1 = int(n / 2)
        mid2 = mid1 + 1
        med = (sorted_sample[mid1 - 1] + sorted_sample[mid2 - 1]) / 2
        return med

    mid = ceil(n / 2)
    med = sorted_sample[mid - 1]
    return med

def deviations_from_mean(sample, mu = None):

    if mu == None:
        mu = mean(sample)
        
    deviations = sample - mu
    return deviations

def variance(sample):
    
    deviations_squared = deviations_from_mean(sample) ** 2
    return mean(deviations_squared)

def standard_error_of_mean(sample):
    
    sigma_squared = variance(sample)
    sigma = sqrt(sigma_squared)
    return sigma / sqrt(len(sample))

def mean_absolute_deviation(sample, mu = None):

    if mu == None:
        mu = mean(sample)

    absolute_deviations = abs(sample - mu)
    return mean(absolute_deviations)
