from math import sqrt
from scipy.stats import t
from src.dispersion import mean, variance, standard_error_of_mean


def _p_value_student_t(t_stat, df, alt_hypothesis):

    p_multiplier = 1
    
    if alt_hypothesis == "unequal":
        t_stat = abs(t_stat)
        p_multiplier = 2

    if alt_hypothesis == "less":
        t_stat = -t_stat

    if alt_hypothesis == "greater":
        t_stat = t_stat
    
    p_value = (1 - t.cdf(t_stat, df)) * p_multiplier
    return p_value


def _welch_df(var1, var2, n1, n2):

    var_mu1, var_mu2 = (var1 / n1), (var2 / n2)
    df1, df2 = (n1-1), (n2-1)
    
    numerator = (var_mu1 + var_mu2) ** 2
    denominator = (var_mu1 ** 2 / df1) + (var_mu2 ** 2 / df2)

    return numerator / denominator


def one_sample_t_test(sample, null_mean, alt_hypothesis = "unequal"):
    
    sample_mean = mean(sample)
    sample_sem = standard_error_of_mean(sample)
    t_stat = (sample_mean - null_mean) / sample_sem
    df = len(sample) - 1
    p_value = _p_value_student_t(t_stat, df, alt_hypothesis)
    
    return (t_stat, p_value, df)


def paired_t_test(sample1, sample2, alt_hypothesis = "unequal"):
    
    differences = sample1 - sample2
    return one_sample_t_test(differences, 0, alt_hypothesis)


def welch_t_test(sample1, sample2, alt_hypothesis = "unequal"):

    mu1, mu2 = mean(sample1), mean(sample2)
    nominator = mu1 - mu2

    var1, var2 = variance(sample1), variance(sample2)
    n1, n2 = len(sample1), len(sample2)
    denominator = sqrt((var1 / n1) + (var2 / n2))

    t_stat = nominator / denominator
    df = _welch_df(var1, var2, n1, n2)
    p_value = _p_value_student_t(t_stat, df, alt_hypothesis)

    return (t_stat, p_value, df)
