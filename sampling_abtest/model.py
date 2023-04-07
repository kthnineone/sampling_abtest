import numpy as np
import pandas as pd
from scipy import stats

def srs(data, n):
    """
    Simple Random Sampling WITHOUT Replacement
    Samples of size n are chosen from the population with the same chance.
    """
    samples = data.sample(n)
    return samples

def systematic(data, sample_size, interval):
    """Sample the units by the sampling interval k. 
    For example, starting number is 34, and the interval is 1000, 
    and then the sample numbers are 34, 1034, 2034,... and so on.
    If interval is 2, samples are odd numbered samples
    or even numbered samples.
    """
    indices = list(range(0, sample_size, interval))
    samples = data.iloc[indices]
    return samples


def binary(data, sample_size):
    """divided data into odd numbered and even numbered
    and sample them with the size of sample_size.
    It is not optimal but simple.
    """
    even_indices = range(0, data.shape[0], 2)
    odd_indices = range(1, data.shape[0], 2)
    even_data = data.iloc[even_indices]
    odd_data = data.iloc[odd_indices]
    even_n = int(sample_size/2)
    odd_n = sample_size - even_n
    even_samples = even_data.sample(int(sample_size/2))
    odd_samples = odd_data.sample(odd_n)
    samples = {'a': even_samples, 'b': odd_samples}
    return samples

def make_groups(data, cate_list):
    """Make new group category to mark detailed divisions
    For example, A_alpha means the group is both in the category
    of A and alpha where A is in category group Alphabet,
    and alpha is in category group Greek, and
    cate_list = ['Alphabet', 'Greek']
    """
    assert type(cate_list) is list, 'category should be list type'
    data['new_group'] = data[cate_list[0]]
    for idx in range(1, len(cate_list)):
        data['new_group'] += '_' + data[cate_list[idx]]
    return data

def strat(data, sample_size, cate_list, min_stratum_size = None):
    """Sample the data from partitioned sub-populations.
    At first, divide the population with size N into H strata, 
    each stratum h with size N_h. The sum of N_h is N.
    
    Filter out smalle sized strata with size of min_stratum_size
    Default setting does NOT exclude any stratum
    """
    # Make new group as combined strata
    data = make_groups(data, cate_list)
    fraction = sample_size/data.shape[0]
    # filter out categories that is smaller than minimum size
    if min_stratum_size:
        cate_counts = data.groupby('new_group').size()
        cates = cate_counts[cate_counts>min_stratum_size].index.to_list()
        data = data[data['new_group'].isin(cates)]
    samples = data.groupby('new_group', 
                           group_keys=False).sample(frac=fraction)
    return samples


def cluster(data, sample_size, cluster_col, cate_list, stage='one'):
    """The population is divied into several clusters. 
    Then, we choose few clusters, and use all the units in the clusters as samples 
    or sample again from chosen clusters. 
    First process is called 'one-stage' cluster sampling plan, 
    and second is called 'two-stage' cluster sampling plan.
    The Clusters are also called Primary Sampling Units (psu), 
    and the each unit in each cluster is called Secondary Sampling Units (ssu).
    """
    data = data[data[cluster_col].isin(cate_list)]
    fraction = sample_size/data.shape[0]
    # One-stage
    if stage=='one':
        samples = data
    # Two-stage
    else:
        if sample_size >= data.shape[0]:
            print('Two-stage is impossible because the sample',
                  'size is bigger than size of clusters.','One-stage is conducted instead.')
            samples = data
        else:
            samples = data.groupby(cluster_col, 
                           group_keys=False).sample(frac=fraction)
    return samples