### Lecture 6: Curve Fitting

* [Understanding Experimental Data](https://www.youtube.com/watch?v=8iQAhz7rzVs)
  * A common pattern in science and engineering is to:
    * Develop a hypothesis.
    * Design an experiment, take measurements.
    * Use computation to:
      * Evaluate the hypothesis.
      * Determine value of unknowns.
      * Predict consequences.

* [Errors in Experimental Observations](https://www.youtube.com/watch?v=FP4Hw1IEWCA)
  * The sum or random errors converges to the normal distribution (central limit theorem):
    * This is independent of what distribution the individual errors have as long as they have a finite mean and variance.
    * The individual errors do not need to be identically distributed.

* [Curve Fitting: Finding a Model that Fits the Observations](https://www.youtube.com/watch?v=SQUNkr4bQyQ)
  * Derivation that minimising the LSE gives the MLE model for the data.
  * One can use the `polyfit` function in pylab to get the parameters that minimize the LSE.

* [Which Curve should we Pick?](https://www.youtube.com/watch?v=yBRf7ajFSTU)
  * Looking at the predictive power of a model.

* [Measuring Goodness of Fit](https://www.youtube.com/watch?v=lcDQ7GqlS-M)
  * Coefficient of determination (R^2) = 1 - (sigma_errror^2 / sigma_data^2) = 1 - SSE/MV,
  represents the fraction of the variability explained by the model. Value ~1 indicates a good model.

* [Using a Model for Predictions](https://www.youtube.com/watch?v=YdT6gL3Cpss)
  
<br>

[Back to course notes](../Course_Notes.md)
