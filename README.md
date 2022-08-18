# CapstoneProject_BankingMarketing
Bank Marketing Data - Supervised &amp; Unsupervised

### Project Overview
Rico Banco is a Portuguese bank serving retail clients for over 25 years. Given
the amount of customer loyalty involved, banking is a notoriously difficult
industry to retain customers, let alone grow. An acute understanding of whom
we serve guides our marketing team to stay competitive. Rico Banco’s
leadership team has enlisted their analytics division to evolve their marketing
practices through advanced modeling with machine learning and data
visualization to build a marketing strategy that can catalyze customer growth
over the short term.

### Project Goals and Business Opportunity
Consumer preferences and requirements are always changing. Rico Banco
needs to monitor constantly its customer base. Although no two customers are
the same, considering customer segments helps us identify the broad
categories of clients we already serve or hope to serve in the future. As we begin
this analytical endeavor, we are also aware of the potential for cost and resource
optimization that are available to us. Analytical approaches to conventional
marketing practice are efficient.

### Deliverables
To build a marketing strategy to capture market share, we will provide Rico
Banco executives with a benison of deliverables to better understand its
customer base. This goals of this project are to deliver the following:
actionable insights to the leadership team, a real-time Tableau dashboard to
analyze marketing campaign results, and a Web Application that classifies
consumers as subscribers and non-subscribers.

##### Data Source
We leveraged bank marketing data sourced from the UCI Machine Learning
Repository, containing 41,188 records and 21 features relevant to a direct
marketing campaign. The dataset included demographic information,
descriptive statistics, socioeconomic indices, as well as a target variable
identifying whether the individual subscribed to the term deposit as a result of
the call.

### Methodology
Before we executed our modeling, we ran extensive Exploratory Data Analysis
(EDA) on the input data, implemented data transformations, and created new
features to make the analysis more robust. We also used an oversampling
technique to create a more balanced dataset to train the models.
We observed several modeling best practices when applying different model
types. This included supervised classification models such as logistic
regression, decision tree, random forest, Gradient Boosting, Extreme Gradient
Boosting, and deep neural networks (DNN). This allowed us to understand
relationships between our variables and identify those most meaningful to
our marketing strategy.
We used unsupervised learning methods in K-means clusters and Gower
Distance to group observations and identify underlying pattern and similarity
of our customer base. With the Principal Components Analysis (PCA), for
numeric features and Factor Analysis of Mixed Data (FAMD) for categorical
features, we reduced dimensionality and mitigated potential collinearity.

### Model Performance
![Capture](https://user-images.githubusercontent.com/43327902/185464003-1695e572-3d13-4e6d-89a0-db08bfb64637.PNG)

The table shows that all the models perform within 2% accuracy of each
other. Differences arise when observing the precision, recall, and F1 scores.
The Neural Network model performs with the highest recall while the Logistic
Regression model is performing quite poorly with regards to recall.
Our team recommends using the Neural Net model to predict future
marketing campaign success. Not only did the neural net model have high
accuracy, but it also had the highest recall weight compared with the other
models. When using models to identify which customers to target via
marketing campaigns, high recall is one of the most important measures of
success as it is essential not to miss potential customers with high likelihood
of subscribing to term deposits. It would ultimately be costlier to Rico Banco
to miss out on potential customers than it would to spend time and money
making marketing outreach to those who will not subscribe at all.

### Data Visualization Dashboards
One of the primary goals of this project is to ensure that the marketing and
leadership teams at Rico Banco have access to the insights and analytics
required to make better informed business decisions about marketing strategy
and budget. A tableau dashboard was built to support the Rico Banco teams in
tracking the real-time progress of current and future campaign performance.
![image](https://user-images.githubusercontent.com/43327902/185464191-cd21e985-8c23-4e71-85a8-cd6b73c35584.png)
https://public.tableau.com/app/profile/lisa.izquierdo/viz/498_project_dashboard/FinalStory?publish=yes

### Web Application
![image](https://user-images.githubusercontent.com/43327902/185464440-ed7064df-d2fb-4f06-b7b6-4670d7cbe84b.png)
https://shawnliu119-capstoneproject-bankingmarketin-mobileappapp-9qiu3z.streamlitapp.com/
