# Four Sampling Methods for A/B Test

Four sampling methods are presented.
SRS (Simple Random Sampling), Stratified Sampling, Cluster Sampling, Systematic Sampling.
Here default setting is WITHOUT replacement sampling.

It is inspired by Sharon L. Lohr, Sampling: Design and Analyis, 2nd edition, 2009, Routledge. Also Wikipedia is another reference.

1. SRS (Simple Random Sampling) WITHOUT Replacement
2. Systematic Sampling
3. Stratified Sampling
4. Cluster Sampling

## 1. SRS (Simple Random Sampling) WITHOUT Replacement


Samples of size n are chosen from the population with the same chance.  

Denote n as the sample size, and N as the size of poplation.  
Sample mean is defined as $\overline{y_{\it S}} = \frac{1}{n}\sum_{i \in S}y_i$.  
The variance of sample mean is $V(\bar{y}) = \frac{s^2}{n}(1-\frac{n}{N})$ and standard error (SE) is the square root of estimated variance of $\bar{y}$ denoted as SE($\bar{y}$).  &nbsp;   

The coefficient of variation (CV) is defined as $\frac{\sqrt{V(\bar{y})}}{E(\bar{y})}$.
&nbsp;   

Sampling weight $\pi_i$ is defined as the probility that unit $i$ is included in the sample which is the reciprocal of the inclusion probability: $w_i=\frac{1}{\pi_i}$.  
&nbsp;  

Sample Size Estimation  
1. Specify the Tolerable Error  
$P(|\bar{y}-\overline{y_U}|\leq e) = 1 - \alpha$, where $\overline{y_U}$ is the population mean, $e$ is called margin of error in survey, usually 0.03, and significance level $\alpha$, usaully 0.05.  
2. Find an Equation  
Here we get the equation: n = $\frac{{z_{\alpha/2}^2}{S^2}}{{e^2}+\frac{{z_{\alpha/2}^2}{S^2}}{N}}$.  
Here $S^2 = \hat{p}(1-\hat{p})$ where $\hat{p}$ is the estimated proportion. Since the maximum value of $\hat{p}(1-\hat{p})$ is 1/4, we can subsitute $S^2$ as 1/4.  Furthermore, if we do not know population size N, the equation become n = $\frac{{z_{\alpha/2}^2}{S^2}}{{e^2}}$. In more simple version, n = $\frac{{z_{\alpha/2}^2}{\hat{p}(1-\hat{p})}}{{e^2}}$.

