# _Inventory Prediciton_

## Synopsis

This project explores the well know problem of **time series**. I tested out different models from sarima models to LSTM neural networks for inventory prediction.

The code includes some exploration analysis, trend analysis and finally some models in ipython notebooks. These models were then rewriten into python script and built in the web app.

The purpose of the web app is to provide some insight on the data, give recommendations by introducing product names and getting recommended products based on the ones commonly bought together.

Finally it also provides predicition for items in the inventory giving you a glimpse about what the rate of consumption will be in the following weeks.

## Libraries used

- PureCSS
- Flask
- statsmodels
- seaborn

## Motivation

My primary motivation was to work on a real dataset solving a real problem from a company. Being able to provide forecasts on invetory could lead to a better stock
management since both being over and under stock means losing money. Recommendations is also a big feature because it provides both customers and salespeople a
better experience during a sale.

## File Structure

- **notebooks/** includes the ipython notebooks that I used for exploration and testing
- **website/** contains all the logic for the website

## The Data

The data was provided by _Calvek_ and it is 5 years of sales data, unfortunately this data cannot be published for privacy reasons but I will make sure to upload
some pictures of the working web app.

## Future Work

There is still a lot of room for improvement. For example making more transformations to the data. During the data exploration I found that the transformation
that had the best results was the log function, but there are many ways to stationarize and it could be worthwhile to explore more. The recommendation engine
can be expanded into a product to product recommendation using nlp over the product features and descriptions to find similar products, this is useful
when you run out of stock or if a company wants to find a similar product but from another brand.

## Screenshots

![alt tag](/screenshot.png)
