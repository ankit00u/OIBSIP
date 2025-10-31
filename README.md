# Customer Segmentation Analysis

Auto-generated project scaffold from uploaded CSV (ifood_df.csv).

Detected columns (sample): Income, Kidhome, Teenhome, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Complain, Z_CostContact, Z_Revenue, Response, Age, Customer_Days, marital_Divorced, marital_Married, marital_Single, marital_Together, marital_Widow, education_2n Cycle, education_Basic, education_Graduation, education_Master, education_PhD, MntTotal, MntRegularProds, AcceptedCmpOverall

Auto-selected features: Income, Teenhome, Recency, MntWines

Files:
- notebooks/Customer_Segmentation.ipynb : Jupyter notebook template (run locally)
- scripts/segmentation.py : script template to run clustering
- data/marketing_data.csv : the uploaded dataset (keep here)
- images/preview_scatter.png : lightweight preview scatter (if available)

How to run:
1. pip install -r requirements.txt
2. Open the notebook and run cells interactively to perform clustering and visualization.
3. Or run: python scripts/segmentation.py (may be heavy for large datasets)

Notes:
- This scaffold intentionally avoids running heavy clustering steps in the generator environment.
- Edit features in notebook/script if you prefer different columns.
