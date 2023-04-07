# Four Sampling Methods for A/B Test

Four sampling methods are presented.
SRS (Simple Random Sampling), Stratified Sampling, Cluster Sampling, Systematic Sampling.
Here default setting is WITHOUT replacement sampling.
Sample Size Estimation function is also in this package.

1. SRS (Simple Random Sampling)
2. Systematic Sampling
3. Stratified Sampling
4. Cluster Sampling
5. Sample Size Estimation

Required Packages
+ pandas
+ SciPy


It is inspired by Sharon L. Lohr, Sampling: Design and Analyis, 2nd edition, 2009, Routledge. Also Wikipedia is another reference.


## 1. SRS (Simple Random Sampling)


Samples of size n are chosen from the population with the same chance.  

Denote n as the sample size, and N as the size of poplation.  
Sample mean is defined as $\overline{y_{\it S}} = \frac{1}{n}\sum_{i \in S}y_i$.  
The variance of sample mean is $V(\bar{y}) = \frac{s^2}{n}(1-\frac{n}{N})$ and standard error (SE) is the square root of estimated variance of $\bar{y}$ denoted as SE($\bar{y}$).  &nbsp;   

The coefficient of variation (CV) is defined as $\frac{\sqrt{V(\bar{y})}}{E(\bar{y})}$.
&nbsp;   

Sampling weight $\pi_i$ is defined as the probility that unit $i$ is included in the sample which is the reciprocal of the inclusion probability: $w_i=\frac{1}{\pi_i}$.  
&nbsp;  

## 2. Systematic Sampling  
Sample the units by the sampling interval k. For example, starting number is 34, and the interval is 1000, and then the sample numbers are 34, 1034, 2034,... and so on. 

### 2.1. Binary Sampling
Divided data into odd numbered and even numbered and sample them with the size n. It is not optimal but simple.

## 3. Stratified Sampling  
Sample the data from partitioned sub-populations.  
At first, divide the population with size N into H strata, each stratum h with size $N_h$. ${\sum_{h}}^{H}{N_h} = N$. We sample $n_h$ from each stratum h.  
Sample mean of each stratum is defined as $\overline{y_{\it h}} = \frac{1}{n_h}\sum_{i \in S_h}y_{hj}$ and the se is $s^2_{h} = \sum_{j \in S_h}\frac{{(y_{hj} - \bar{y_h})}^2}{{n_h}-1}$.
And then $\bar{y_{str}} = {\sum_{h=1}}^{H} \frac{N_h}{N} \bar{y_h}$.  


|Source|df|Sum of Squares|
|---------------|-----|--------------------------------------------------------|
|Between strata|H-1| $SSB$ $= {\sum_{h=1}}^{H} {\sum_{j=1}}^{N_h}$ $({\bar{y}_{hU}} - \bar{{y}_U})^2$ |
|Within strata|N-H| $SSW$ $= {\sum_{h=1}}^{H}$ ${\sum_{j=1}}^{N_h}$ $(\bar{y}}_{hj} - {\bar{y}}_{hU})^2$ |
|Total|N-1| $SST$ $= {\sum_{h=1}}^{H}$ ${\sum_{j=1}}^{N_h}$ $({\bar{y}_{hj}} - {\bar{y}_{U}})^2$ |  

 
If SSB < ${\sum_{h=1}}^{H}(1- \frac{N_h}{N})S_h^2$, then Stratified Sampling always has smaller variance than SRS.


## 4. Cluster Sampling  
The population is divied into several clusters. Then, we choose few clusters, and use all the units in the clusters as samples or sample again from chosen clusters. First process is called 'one-stage' cluster sampling plan, and second is called 'two-stage' cluster sampling plan.The Clusters are also called Primary Sampling Units (psu), and the each unit in each cluster is called Secondary Sampling Units (ssu).  
&nbsp;  
Let n be the number of psus in the sample, $m_i$ be the number of ssus in the sample from psu $i$m, N be the number of psus in the population, and $M_i$ be the number of ssus in the psu $i$.  
Sample mean of psu (cluster) $i$ is defined as $\bar{y}_i = \sum_{j \in S_i}\frac{y_{ij}}{m_i}$.  
Sample variance in psu $i$ is $s^2_{i} = \sum_{j \in S_i}\frac{{(y_{ij} - \bar{y_i})}^2}{{m_i}-1}$.  
Estimated total for psu $i$ is defined as $\hat{t_i} = \sum_{j \in S_i}\frac{M_i}{m_i}y_{ij}$.  
Unbiased estimator for population total is defined as $\hat{t_{unb}} = \sum_{i \in S}\frac{N}{n}\hat{t_i}$.  
Sample variance of population total is defined as $s_t^2 = \sum_{i \in S}(\hat{t_i}-\frac{\hat{t_{unb}}}{N})^2$.  
In One-stage cluster sampling, the se of $\hat{\bar{y}}$ is $\frac{1}{M}\sqrt{(1-\frac{n}{N})\frac{s_t^2}{n}}$.  
 

|Source|df|Sum of Squares|
|---------------|-----|----------------------------------------------|
|Between psus|N-1|$SSB = {\sum_{i=1}}^{N} {\sum_{j=1}}^{M}(\bar{y}_{iU}-\bar{y}_U)^2$|
|Within ssus|N(M-1)|$SSW = {\sum_{i=1}}^{N} {\sum_{j=1}}^{M}(\bar{y}_{ij}-\bar{y}_{iU})^2$|
|Total|NM-1|$SST = {\sum_{i=1}}^{N} {\sum_{j=1}}^{M}(\bar{y}_{ij}-\bar{y}_{U})^2$|  
  
 
Intraclass (or intracluster) correlation coefficient (ICC) tells us how similar elements in the same cluster are. It provides a measure of homogeneity within the clsuters.  
ICC = 1 - $\frac{M}{M-1}\frac{SSW}{SST}$ and $-\frac{1}{M-1} \leq ICC \leq 1$.  
If the elemnts in each cluster are similar and the sum of squares are small, then ICC gets smaller value, on the other hand if the elements are not similart, and ICC gets bigger. If ICC is negative value, cluster sampling is more efficient than SRS.  
&nbsp;  
In Two-stage cluster sampling,  
Estimated total for psu $i$ is defined as $\hat{t_i} = \sum_{j \in S_i}\frac{M_i}{m_i}y_{ij}$.  
Hence, the sample weight for each element is $w_{ij} = \frac{NM_i}{nm_i}$.  


## Sample Size Estimation  
1. Specify the Tolerable Error  
$P(|\bar{y}-\overline{y_U}|\leq e) = 1 - \alpha$, where $\overline{y_U}$ is the population mean, $e$ is called margin of error in survey, usually 0.03, and significance level $\alpha$, usaully 0.05.  
2. Find an Equation  
Here we get the equation: n = $\frac{{z_{\alpha/2}^2}{S^2}}{{e^2}+\frac{{z_{\alpha/2}^2}{S^2}}{N}}$.  
Here $S^2 = \hat{p}(1-\hat{p})$ where $\hat{p}$ is the estimated proportion. Since the maximum value of $\hat{p}(1-\hat{p})$ is 1/4, we can subsitute $S^2$ as 1/4.  Furthermore, if we do not know population size N, the equation become n = $\frac{{z_{\alpha/2}^2}{S^2}}{{e^2}}$. In more simple version, n = $\frac{{z_{\alpha/2}^2}{\hat{p}(1-\hat{p})}}{{e^2}}$.




