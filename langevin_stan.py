import pandas as pd
import os.path
import sys
import langevin
import pystan
import matplotlib.pyplot as plt

langevin_code = """
data {
int<lower=0> N;
real<lower=0> alpha_D;
real<lower=0> beta_D;
real<lower=0> alpha_A;
real<lower=0> beta_A;
vector[N] y;
}
parameters {
real<lower=0> D;
real<lower=0> A;
}
model {
D ~ gamma(alpha_D,beta_D);
A ~ gamma(alpha_A, beta_A);
y[1] ~ normal(0,sqrt(A));
for (n in 2:N)
    y[n] ~ normal(y[n-1]*exp(-0.01*D/A), sqrt(A*(1-exp(-0.02*D/A))));
}
"""

langevin_dat = {'N': 50,
                'alpha_A' : 0.0025,
                'beta_A' : 0.0025,
                'alpha_D' : 0.01,
                'beta_D' : 0.01,
                'y' : [0.6547612311626614,
                        0.6963454770690765,
                        0.3804548056778836,
                        0.37860871231831744,
                        0.17115054129036894,
                        0.3213176746951389,
                        0.13079710344620488,
                        0.046793966703116335,
                        -0.044230261261917744,
                        -0.09035587712108588,
                        0.08607235293617957,
                        0.29601624543231864,
                        0.1992717270655152,
                        0.34561044788806544,
                        0.3500401706519693,
                        0.4419177325793053,
                        0.39245571696094894,
                        0.567832512790599,
                        0.5344518525026463,
                        0.4564673823942968,
                        0.31922072811538016,
                        0.4391497187680327,
                        0.5049263367601124,
                        0.4237691723502714,
                        0.3769860691656745,
                        0.444306584226043,
                        0.3099131532054338,
                        0.4076768399680731,
                        0.7034648815440385,
                        0.7468381157704824,
                        0.8754962481608999,
                        0.8744954850974689,
                        0.8439523507526724,
                        0.6653710995507052,
                        0.4900747446375602,
                        0.3256164574930888,
                        0.33805340233533965,
                        0.5815203353040166,
                        0.8498019778402848,
                        0.7752119188303063,
                        0.9571739491836888,
                        1.0116382766553982,
                        1.1191947891414615,
                        1.036679418083779,
                        1.1345334126592426,
                        1.1039553155694803,
                        1.116321296459667,
                        1.1841185856779728,
                        0.967793290886198,
                        1.0865961600231002 ]}

fit = pystan.stan(model_code=langevin_code, data=langevin_dat,
                  iter=10000, chains=4)

print(fit)

fit.plot()
plt.show()