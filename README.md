# predictive-tasks
Basic Python implementation of predictive algorithms

TODO:
- Start by implementing a basic naive algorithm (done)
- Implement random walk validation

**How to implement a time-series predictive model**
- Use autocorrelation to understand whether statistical models can be applied
    - Convert series to stationary (apply differencing if necessary, until it passes the ADF test)
    - Use ACF to test autocorrelation