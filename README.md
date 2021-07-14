# Predicting Wine Quality
Group Members: Noelle Ferrari and Katarina Salcedo

## Motivation

Provide the Washington Winegrower's Association with a model that predicts a wine's quality score, from 1-10,  based upon it's chemical composition. The goal of our model is to help increase the Washington Winegrower's preformance in competitions. 

## Data

Our [dataset](https://www.kaggle.com/huseyinelci/wne-qualty-by-uci) contains 6497 wines and has information on 11 chemical features of each wine. These features include fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates and alcohol. 

## Methodology

Red and white wine datasets were combined and two categorical columns were added stating whether the wine was red or white. Before a baseline linear regression model was run, linear and mulitcollinearity assumptions were checked and the dataset was adjusted accordingly. From the baseline model, we went through mulitiple iterations, transforming and manipulating the data after each time, to try and increase our R-squared value, lower our RMSE and ensure all p-values were significant. 

## Results

Our baseline model has an R-squared value of 0.290 and several insignificant p-values. However, the RMSE for train and test sets are 0.732 and 0.735 respectively, indicating that this model does a reasonable job predicting quality and the model is not over- or under- fit to the data. 

![Baseline Model](https://github.com/klsalcedo/wine_analysis/blob/main/Images/Baseline%20Model.png?raw=true)

Through several iterations we were able to improve the R-squared to 0.300 and reduce RMSE to 0.727 for the train set and 0.730 for the test set. All p-values are statistically significant, and there are no collinearity issues with this model. We were not able to improve the R-squared further despite repeated attempts.

![Final Model](https://github.com/klsalcedo/wine_analysis/blob/main/Images/Final%20Model.png?raw=true)

## Conclusions 

Our final model is able to explain 30% of the variation in wine quality is a result of the wine's physiochemical properties.

## Next Steps

In order to improve predictions for this dataset, we believe that either additional data is needed to refine predictions or a different modelling technique should be used instead.
