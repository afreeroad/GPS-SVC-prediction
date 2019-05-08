# GPS-SVC-prediction
Predicting the target country, from a set of economic preferences. 

This notebook utilizes the 'individual.dta' datset from the Global Preferences Survey, found here: https://www.briq-institute.org/global-preferences/downloads

The dataset has been engineered and appended to utilizing the 'WBData' API from the World Bank. Columns identifying and corresponding to the geographical 'region' as well as the relative 'income' level of each represented country are added to the dataset. 

As evidenced in the title, the model developed here utilizes the Support Vector Classification (SVC) model. Details can be found here: https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html

The model is then trained on the input data utilizing each of the economic preferences of 'patience', 'risktaking', 'posrecip', 'negrecip', 'altruism' and 'trust'. The whole of the dataset comprises almost 80,000 individuals (rows). We then attempt to predict the origin country of an individual by randomly selecting an individual (row) and inputting those variables into the 'clf.predict()' function. 
