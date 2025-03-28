---
layout: post
author: Rob Wheaton
tags: [cscc]
---

### [Machine Learning: The two steps that really matter]
When using machine learning to solve a problem, there are several steps in the process to ensure that development time is minimized while maximizing the probability that the objective will be reached:
1. Gathering data
1. Preparing that data
1. Choosing a model
1. Training
1. Evaluation
1. Hyperparameter Tuning
1. Prediction

Each of these steps is important, but there are two that are necessary to get right in order to make all the other steps easier: Preparing data and Evaluation.

When **preparing data**, it's important to validate that each field has a consistent type; make sure that numbers are not actually strings in your data or vice versa. It's also important to verify that your data does not exceed the limits of the programming language you're using to process the data. Are there "Big Ints" in your data? You'll have to account for those, or your code may crash. Excel especially has a bad habit of converting very small decimals to scientific notation, which end up being strings when you export them; validate that all numbers are in a single format.

After you've trained a model, choosing the right **evaluation** measures becomes critical to enable iterating on your model to improve it. Some of the common measures:
* **Accuracy**: How often does your model correctly classify a new piece of data? Expressed as a percentage. This is a good simple measure and easy to calculate.
* **Precision**: A measure of the usefulness of the classifier results in the test data. It's defined as the number of documents accurately classified, divided by the total number of classifications for the class. High precision means that the classifier returned significantly more relevant results than irrelevant ones. [source](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-macroprecision-metric)
* **Recall**: Indicates the percentage of correct categories in your text that the model can predict. This metric comes from averaging the recall scores of all available labels. Recall is a measure of how complete the classifier results are for the test data. [source](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-macrorecall-metric)
* The **F1 score** is derived from the Precision and Recall values. It measures the overall accuracy of the classifier. The highest score is 1, and the lowest score is 0.
* **NDCG** (normalized discounted cumulative gain) measures the effectiveness and quality of product ranking in the search, feed ranking, and document retrieval tasks. The higher the NDCG, the better the ranking. [source](https://medium.com/@mukulranjan/understanding-ndcg-885656321b3b) This measure is specific for search and recommendation systems but very useful.
