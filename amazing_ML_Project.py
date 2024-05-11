#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas


# In[3]:


import pandas as pd

df = pd.read_csv("amazon.csv")


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


#clean and error free data is required

def check_missing_values(dataframe):
    return dataframe.isnull().sum()

print(check_missing_values(df))
df[df.rating_count.isnull()]


# In[7]:


#The rows with missing informatio will be deleted. Missing values my affect the accuracy of our dataset.
#The missing values in rating_count will make all the rows with missing data to be deleted. 
df.dropna(subset=['rating_count'], inplace=True)
print(check_missing_values(df))


# In[8]:


#Additional data cleaning should take place. The step two is to make sure there are no duplicate
def check_duplicates(dataframe):
    return dataframe.duplicated().sum()

print(check_duplicates(df))


# In[9]:


#Once confirmed that the dataset is clean we proceed to check the data types
def check_data_types(dataframe):
    return dataframe.dtypes

print(check_data_types(df))


# In[10]:


#To analyze the dataset we need to transfor object data type to float data type
df['discounted_price'] = pd.to_numeric(df['discounted_price'].astype(str).str.replace('₹', '').str.replace(',', '')).astype(float)
df['actual_price'] = df['actual_price'].astype(str).str.replace('₹', '').str.replace(',', '').astype(float)
df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%','').astype(float)/100


# In[11]:


count = df['rating'].str.contains('\|').sum()
print(f"Total de linhas com '|' na coluna 'rating': {count}")
df = df[df['rating'].apply(lambda x: '|' not in str(x))]
count = df['rating'].str.contains('\|').sum()
print(f"Total de linhas com '|' na coluna 'rating': {count}")


# In[12]:


df['rating'] = df['rating'].astype(str).str.replace(',', '').astype(float)
df['rating_count'] = df['rating_count'].astype(str).str.replace(',','').astype(float)


# In[13]:


#This confirms that our data is ready to be analyzed. The data is now set as a float.
print(check_data_types(df))


# In[14]:


#creation of Rating_weighted column to normalize the data. A lot of the data may lead to inaccurate results due to the fact that some products may have less reviews with better notes

df['rating_weighted'] = df['rating'] * df['rating_count']


# In[15]:


df['sub_category'] = df['category'].astype(str).str.split('|').str[-1]
df['main_category'] = df['category'].astype(str).str.split('|').str[0]


# In[16]:


df.columns


# In[17]:


len(df)


# In[18]:


df.head()


# In[19]:


import matplotlib.pyplot as plt

main_category_counts = df['main_category'].value_counts()[:30]
plt.bar(range(len(main_category_counts)), main_category_counts.values)
plt.ylabel('Number of Products')
plt.title('Distribution of Products by Main Category (Top 30)')
plt.xticks(range(len(main_category_counts)), '')
plt.show()

top_main_categories = pd.DataFrame({'Main Category' : main_category_counts.index, 'Number of Products' : main_category_counts.values})
print('Top 30 main categories:')
print(top_main_categories.to_string(index=False))


# In[20]:


top = df.groupby(['main_category'])['rating'].mean().sort_values(ascending=False).head(10).reset_index()

plt.bar(top['main_category'], top['rating'])

plt.xlabel('main_category')
plt.ylabel('Rating')
plt.title('Top main_category by Rating')

plt.xticks(rotation=90)

plt.show()
ranking = df.groupby('main_category')['rating'].mean().sort_values(ascending=False).reset_index()
print(ranking)


# In[21]:


plt.hist(df['rating'])
plt.xlabel('Rating')
plt.ylabel('Number of Reviews')
plt.title('Distribution of Customer Ratings')
plt.show()

bins = [0, 1, 2, 3, 4, 5]
df['cluster'] = pd.cut(df['rating'], bins=bins, include_lowest=True, labels=['0-1', '1-2', '2-3', '3-4', '4-5'])
table = df['cluster'].value_counts().reset_index().sort_values('index').rename(columns={'index': 'Cluster', 'cluster': 'Number of Reviews'})
print(table)


# In[22]:


top = df.groupby(['sub_category'])['rating'].mean().sort_values(ascending=False).head(10).reset_index()

plt.bar(top['sub_category'], top['rating'])

plt.xlabel('sub_category')
plt.ylabel('Rating')
plt.title('Top sub_category by Rating')

plt.xticks(rotation=90)

plt.show()
ranking = df.groupby('sub_category')['rating'].mean().sort_values(ascending=False).reset_index()
print(ranking)


# In[23]:


mean_discount_by_category = df.groupby('main_category')['discount_percentage'].mean()
mean_discount_by_category = mean_discount_by_category.sort_values(ascending=True)

plt.barh(mean_discount_by_category.index, mean_discount_by_category.values)
plt.title('Discount Percentage by Main Category')
plt.xlabel('Discount Percentage')
plt.ylabel('Main Category')
plt.show()

table = pd.DataFrame({'Main Category': mean_discount_by_category.index, 'Mean Discount Percentage': mean_discount_by_category.values})

print(table)


# In[24]:


mean_discount_by_sub_category = df.groupby('sub_category')['discount_percentage'].mean().head(15)
mean_discount_by_sub_category = mean_discount_by_sub_category.sort_values(ascending=True)


plt.barh(mean_discount_by_sub_category.index, mean_discount_by_sub_category.values)
plt.xlabel('Discount Percentage')
plt.ylabel('Sub Category')
plt.show()

table = pd.DataFrame({'Sub Category': mean_discount_by_sub_category.index, 'Mean Discount Percentage': mean_discount_by_sub_category.values})

print(table)


# In[25]:


from wordcloud import WordCloud

reviews_text = ''.join(df['review_content'].dropna().values)
wordcloud = WordCloud (width=650, height=650, background_color='orange', min_font_size=10).generate(reviews_text)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()


# In[27]:


low_rating_df = df[df['rating'] > 4.0]

reviews_text = ''.join(low_rating_df['review_content'].dropna().values)

wordcloud = WordCloud(width=650, height=650, background_color='orange', min_font_size=10).generate(reviews_text)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()


# In[28]:


numeric_cols = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_cols.corr()

print(correlation_matrix)


# In[29]:


import seaborn as sns
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


# In[32]:


from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['user_id_encoded'] = le.fit_transform(df['user_id'])

freq_table = pd.DataFrame({'User ID': df['user_id_encoded'].value_counts().index, 'Frequency': df['user_id_encoded'].value_counts().values})

print(freq_table)
id_example = freq_table.iloc[0,0]
print(id_example)


# In[41]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_products(df, user_id_encoded):
    tfidf = TfidfVectorizer(stop_words='english')
    df['about_product'] = df['about_product'].fillna('')
    tfidf_matrix = tfidf.fit_transform(df['about_product'])
    
    user_history = df[df['user_id_encoded'] == user_id_encoded]
    
    indices = user_history.index.tolist()
    
    if indices:
        
        cosine_sim_user = cosine_similarity(tfidf_matrix[indices], tfidf_matrix)
        
        products = df.iloc[indices]['product_name']
        indices = pd.Series(products.index, index=products)
        
        similarity_scores = list(enumerate(cosine_sim_user[-1]))
        similarity_scores = [(i, score) for (i, score) in similarity_scores if i not in indices]
        
        similarity_scores = sorted(similarity_scores, key=lambda x:x[1], reverse=True)
        
        top_products = [i[0] for i in similarity_scores[1:6]]
        
        recommended_products = df.iloc[top_products]['product_name'].tolist()
        
        score = [similarity_scores[i][1] for i in range(5)]
        
        results_df = pd.DataFrame({'Id Encoded': [user_id_encoded] * 5, 'recommended product': recommended_products, 'score recommendation': score})
        
        return results_df
    
    else:
        print("No purchase history found")
        return None


# In[42]:


recommend_products(df, 893)

