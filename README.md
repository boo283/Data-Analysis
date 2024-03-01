# Data-Analysis - Motorbike's Price Prediction
Our project is support my learning project at UIT.
Focusing on:
![image](https://github.com/boo283/Data-Analysis/assets/134665760/4ec94b3a-6869-4038-96f9-c678ffb4b74b)

- Crawl data: Get motorbike data from classic-trader.com by using Request + BeautifulSoup (Python)
- Clean data: Fill missing and format data.
- Normalize and scale data with reasonable method.
- Visualize data: supported by matplotlib associated with creating a dashboard by Python script in PowerBI. We designed some charts: histogram, pie chart, bubble chart, boxplot,... for analysing purpose.
- Create data model and train: After selecting variables that affect the dependent variable by Pearson Coefficient and ANOVA analysis, we built our model with pipeline:
    + 90% dataset for training set.
    + Scale numeric features by using StandardScaler()
    + Encode categorical features by using OneHotEncoder()
    + Choose PolynomialFeatures(degree = 3) and Ridge Regression (alpha = 85)
- Test model, adjust and make evaluation:
    + R2 Score:0.765
    + Root mean squared error: 4787.83
    + ![image](https://github.com/boo283/Data-Analysis/assets/134665760/24f31cd1-4f87-4b80-af0b-8c47b4dd80ce)


