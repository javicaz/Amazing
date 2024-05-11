<h1>Amazon Product Analysis & Recommendation System</h1>

<p>Welcome to my data science project! In this project, we'll be analyzing a dataset of over 1,000 products listed on Amazon and building a recommendation system for these products.

The dataset includes details such as product name, category, price, rating, and user reviews . The goal is to understand customer preferences, identify purchasing patterns, and develop a recommendation system to suggest products to users based on their interests. </p>

<p>The project will consist of the following steps:</p>

<ul>
- Data collection: From the Amazon products dataset from Kaggle.

- Data preparation: Clean and preprocess the dataset for analysis.
</ul>

<p>Exploratory data analysis: Analyze the data to understand the distribution of products by categories, customer ratings, and reviews.

Data visualization: Visualize the data to identify trends and patterns.<p>

Simples recommendation system: Develop a recommendation system using machine learning algorithms to suggest products to users based on their interests and previous purchases.
<ul>
-Data collection

The dataset that will be used has information on over 1000 products sold by Amazon, like their names, categories, prices, ratings, and reviews. We're going to be digging into this data and figuring out what it all means, and how we can use it to help Amazon and its customers.

My girlfriend and myself started to sell on for Amazon, and I hope to use this dataset to analyze this data and understand which products are popular and which aren't, to price and market things better. As we as finding ideal customers and products. 

So, I'm going to be exploring this dataset, doing data analysis and visualization and even building a recommendation system based on the data. 

<ul>
Data description:

<li>product_id - Product ID</li>

<li>product_name - Name of the Product</li>

<li>category - Category of the Product</li>

<li>discounted_price - Discounted Price of the Product</li>

<li>actual_price - Actual Price of the Product</li>

<li>discount_percentage - Percentage of Discount for the Product</li>

<li>rating - Rating of the Product</li>

<li>rating_count - Number of people who voted for the Amazon rating</li>

<li>about_product - Description about the Product</li>

<li>user_id - ID of the user who wrote review for the Product</li>

<li>user_name - Name of the user who wrote review for the Product</li>

<li>review_id - ID of the user review</li>

<li>review_title - Short review</li>

<li>review_content - Long review</li>

<li>img_link - Image Link of the Product</li>

<li>product_link - Official Website Link of the Product</li>

</ul>

<p> To access the dataset, simply go to Kaggle website: https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset</p>


<ul>
-Data preparation
<p>Before we dive into the data analysis and visualization, we need to make sure our dataset is clean and properly formatted. This process is called data preparation, and it involves several steps:

-Data Inspection: We'll start by inspecting the dataset to see if there are any missing values, duplicates, or inconsistent data. We'll also check if the data types are correct and make sure the dataset is ready for analysis.
-Data Cleaning: Next, we'll clean the dataset by removing or correcting any errors, inconsistencies, or irrelevant information. This will make the dataset more reliable and accurate.

-Data Transformation: After cleaning the dataset, we may need to transform the data to make it more useful for analysis. This can include scaling, normalization, or feature engineering.

-Data Saving: Once we've prepared the data, we'll save it in a new file to avoid overwriting the original dataset. This way, we can always go back to the original dataset if we need to.</p>
<ul>

<p>By following these steps, it is ensured that our data is clean, accurate, and ready to analyze.</p>


<h2>Test Data & Data visualization</h2>

-Analyze the distribution of products by category using a bar plot.

-Analyze the distribution of customer ratings using a histogram.

-Analyze the reviews by creating word clouds or frequency tables of the most common words used in the reviews.

-Perform statistical analysis to identify any correlations between different features, such as the relationship between product price and customer rating.

Recommendation system
As a Machine Learning Engeenier, my goal is to help sellers find products that will perform and customer will love. To achieve this, I'm creating a recommendation system using a dataset from Amazon that contains information about products, reviews, and users.

<h2>Requierments</h2>

The analysis was develped in Linux Ubuntu 22.04.4 LTS

IDE: Anaconda 
Tools: Jupyter Notebook
 