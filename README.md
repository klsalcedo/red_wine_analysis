# Predicting Wine Quality

The goal of this project is to use a linear regression model to predict the quality of a wine based on it's chemical composition. Our [dataset](https://www.kaggle.com/huseyinelci/wne-qualty-by-uci) contains 6497 wines, 11 chemical features of each wine, and classifies each wine as erd or white. 

Our baseline model has an R-squared value of 0.290 and several insignificant p-values. However, the RMSE for train and test sets are 0.732 and 0.735 respectively, indicating that this model does a reasonable job predicting quality and the model is not over- or under- fit to the data. 

![Baseline Model](https://github.com/klsalcedo/wine_analysis/blob/main/Images/Baseline%20Model.png?raw=true)

Through several iterations we were able to improve the R-squared to 0.300 and reduce RMSE to 0.727 for the train set and 0.730 for the test set. All p-values are statistically significant, and there are no collinearity issues with this model. We were not able to improve the R-squared further despite repeated attempts.

![Final Model](https://github.com/klsalcedo/wine_analysis/blob/main/Images/Final%20Model.png?raw=true)

In order to improve predictions for this dataset, we believe that either additional data is needed to refine predictions or a different modelling technique should be used instead.