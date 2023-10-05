# Advanced Python Course

## Final Project

In this final project we will be using the dataset that is from 'Customer Personality Analysis' from kaggle that can be found here: https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis/

The project was divided in 5 stages:

### 1. Univariate analysis

The Univariate analysis is done to explore and understand better the dataset. Here we are doing some basic plotting and calculating basic stats to get a better idea of the data.

Also, here is done some correlations calculation to start getting a clearer picture of the different type of customers.

### 2. Clasify the Customers

After the univariate analysis is done, we will proceed to use classifier algorithms to clasify the customers in different type of customers.

The approach to follow is to reduce the amount of variables using 'principal component analysis' (PCA) and after that it will be use Kmeans to classify the customers.

### 3. Train a model to predict customer cluster

Now with the PCA and Class of the customers, we will proceed to train different models to evaluate which model gives a better performance.

The performance will be evaluate with a confussion matrix and not just with accuracy.

The models to train will be:
- Support Vector Machine (SVM)
- Random Forest
- Naive Bayes

### 4. Multivariate Analysis

This type of analysis is done to try to understand the classification of the customers. Now that dataset was label according to the clusters found by Kmeans, we will proceed to do the Multivariate Analysis to see if the classification gives a better idea of our customers.

### 5a. Create an API to predict customer cluster

Final stage will be to create an API that will have as input all different original parameters as input (Birth Date, Kidhome, teenhome, income, NumPurchases, etc) and the output of the API will be the prediction of the customer cluster

### 5b. Using Streamlit to predict customer cluster

Another way to predict the customer cluster will be with a web page running streamlit where the user will need to enter all different parameters to predict the customer cluster


----------------------------------------------------------

Stages from 1 to 4 will be coded in a jupyter notebook to show in a better way the steps done to achieve the result.

Stage 5a and 5b will be done in python modules that will required to run a web server to make it work.