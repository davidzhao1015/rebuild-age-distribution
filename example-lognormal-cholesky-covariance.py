#==================================================================================================================
# Example: Implementing sampling from uncertainty distributions of fitted parameters of lognormal survival model
#        using Cholesky decomposition of covariance matrix
#==================================================================================================================

# The following code snippets was referred from ChatGPT and modified to fit the context of survival analysis.

# Python interpreter: 3.12.2 (base)

# Import necessary libraries
import numpy as np
from numpy.random import default_rng

# Point esimates of fitted parameters (log-scale), Late ambulatory survival model
mu_hat = 2.126
sigma_hat = -0.744

# Covariance matrix of the fitted parameters, late ambulatory survival model
cov_matrix = np.array([[0.020, 0.000],
                       [0.018, 0.033]])

# SD of mu_hat = 0.020 
# SD of sigma_hat = 0.033
# Covariance between mu_hat and sigma_hat = 0.018

rng = default_rng(seed=123)  # For reproducibility

# Mean and sigma vector on the same scale as covariance matrix
m = np.array([mu_hat, sigma_hat]) # (u, log sd)


N = 5000
Z = rng.standard_normal(size=(N, 2))  # Standard normal samples

# Cholesky decomposition of covariance matrix
L = np.linalg.cholesky(cov_matrix)

# Generate correlated samples
samples = m + Z @ L.T  # Shape (N, 2)

# Transform back to original scale
mu_samples = samples[:, 0]          # mu samples on log scale
sigma_samples = np.exp(samples[:, 1])  # sigma samples on original scale

# Display first 5 samples
for i in range(5):
    print(f"Sample {i+1}: mu = {mu_samples[i]:.4f}, sigma = {sigma_samples[i]:.4f}")