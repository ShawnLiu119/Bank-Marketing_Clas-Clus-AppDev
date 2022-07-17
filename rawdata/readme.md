
This data set contains records relevant to a direct marketing campaign of a Portuguese banking institution. The marketing campaign was executed through phone calls. Often, more than one call needs to be made to a single client before they either decline or agree to a term deposit subscription. The classification goal is to predict if the client will subscribe (yes/no) to the term deposit (variable y).

This is a modified version of the classic bank marketing data set originally shared in the UCI Machine Learning Repository. There are four datasets available on UCI's repository:
1) bank-additional-full.csv with all examples (41188) and 20 inputs, ordered by date (from May 2008 to November 2010), very close to the data analyzed in [Moro et al., 2014]
2) bank-additional.csv with 10% of the examples (4119), randomly selected from 1), and 20 inputs.
3) bank-full.csv with all examples and 17 inputs, ordered by date (older version of this data set with less inputs).
4) bank.csv with 10% of the examples and 17 inputs, randomly selected from 3 (older version of this data set with less inputs).
Note: The smallest datasets are provided to test more computationally demanding machine learning algorithms (e.g., SVM).

This data set is a copy of data set no. 1 (bank-additional-full.csv) from the list above with one input feature (representing duration of phone call) removed. The following is a note from the variable description in the original data set:

duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.

The duration feature is excluded in this data set to prevent data leakage.

Contents
Input variables:

bank client data:
1 - age (numeric)
2 - job : type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
3 - marital : marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
4 - education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
5 - default: has credit in default? (categorical: 'no','yes','unknown')
6 - housing: has housing loan? (categorical: 'no','yes','unknown')
7 - loan: has personal loan? (categorical: 'no','yes','unknown')

related with the last contact of the current campaign:
8 - contact: contact communication type (categorical: 'cellular','telephone')
9 - month: last contact month of year (categorical: 'jan', 'feb', 'mar', …, 'nov', 'dec')
10 - dayofweek: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')

other attributes:
11 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
12 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
13 - previous: number of contacts performed before this campaign and for this client (numeric)
14 - poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')

social and economic context attributes:
15 - emp.var.rate: employment variation rate - quarterly indicator (numeric)
16 - cons.price.idx: consumer price index - monthly indicator (numeric)
17 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)
18 - euribor3m: euribor 3 month rate - daily indicator (numeric)
19 - nr.employed: number of employees - quarterly indicator (numeric)

Output variable (desired target):

20 - y - has the client subscribed a term deposit? (binary: 'yes','no')
