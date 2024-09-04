from dispersion import mean, deviations_from_mean, variance
from math import sqrt

def covariance(sample1, sample2):

    deviations1 = deviations_from_mean(sample1)
    deviations2 = deviations_from_mean(sample2)
    products = deviations1 * deviations2
    return mean(products)

def correlation_pearson(sample1, sample2):

    cov = covariance(sample1, sample2)
    sigma1, sigma2 = sqrt(variance(sample1)), sqrt(variance(sample2))
    return cov / (sigma1 * sigma2)
    