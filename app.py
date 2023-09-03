import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout='wide')
st.title('MARKETING RESEARCH')





df = pd.read_csv('mercadeo1.csv')
 
col1, col2 = st.columns([2,3])


with col1:
   st.header('Final Dataframe')
   st.dataframe(df.head())

   st.header('Statistical exploration')
    

   fig,ax = plt.subplot_mosaic("""
                     AAAABB
                     AAAACC
                     AAAADD
   """)

   ax['A'].hist(df ['income'],color= 'purple')
   ax['A'].set_xlabel('Yearly Income')
   ax['A'].set_ylabel('Frequency')  
   ax['A'].set_title('INCOME HISTOGRAM')
      

   ax['B'].hist(df['age'],color= 'blue')
   ax['B'].set_xlabel('age')
   ax['B'].set_ylabel('Frequency')  
   ax['B'].set_title('AGE HISTOGRAM')
      

   ax['C'].hist(df['children'],color= 'magenta')
   ax['C'].set_xlabel('Children in house')
   ax['C'].set_ylabel('Frequency')  
   ax['C'].set_title('CHILDREN BAR PLOT')
      
   ax['D'].hist(df['education'],color= 'yellow')
   ax['D'].set_xlabel('Level education')
   ax['D'].set_ylabel('Frequency')  
   ax['D'].set_title('EDUCATION BAR PLOT')

   fig.tight_layout()

   st.pyplot(fig)

   
   columnas_seleccionadas = ['income',	'mntwines' ,'mntfruits' ,	'mntmeatproducts' ,	'mntfishproducts' ,	'mntsweetproducts' ,	'mntgoldprods']
   medias = []
   cuartiles = []
   moda = []
   for columna in columnas_seleccionadas:
    medias.append(df[columna].mean())
    cuartiles.append(df[columna].quantile([0.25, 0.5, 0.75]))
    moda.append(df[columna].mode().iloc[0])

   estadisticas = pd.DataFrame({'Column':columnas_seleccionadas,
                           'Mean': medias,
                           '25%': [q[0.25] for q in cuartiles],
                           'Median': [q[0.5] for q in cuartiles],
                           '75%': [q[0.75] for q in cuartiles],
                           'Mode': moda})
   st.header('Statistics')
   st.dataframe(estadisticas)
  
   st.header('Heat map')
   columnas_seleccionadas = ['income',	'mntwines' ,'mntfruits' ,	'mntmeatproducts' ,	'mntfishproducts' ,	'mntsweetproducts' ,	'mntgoldprods']
   df_seleccionado = df[columnas_seleccionadas]
   corr_matrix_spearman = df_seleccionado.corr(method='spearman')
   fig, ax = plt.subplots()
   sns.heatmap(corr_matrix_spearman, annot=True, cmap='plasma', linewidths=0.5, ax=ax)
   st.pyplot(fig)

   
   st.header('Conclusions')
   st.write('Of a population of 2,240 people, the majority are adults over 53 years of age, who in turn have the highest annual income, as well as an average of 1 child at home. Additionally, they have a behavior with a tendency to loyalty with the store, since the minimum time as a customer is 9 years and the maximum is 11 years.It should be noted that most of the customers do not accept advertising campaigns, so it is proposed to segment the population into 3 groups with similar characteristics to identify their behavior and preferences.')
   st.write('Created by: Catalina Fonseca Martinez - Jeffrey Chamorro Sanchez - Karen Pedraza Mesa')


with col2:
   st.header('Average consume')
   fig,ax=plt.subplots(1,1)
   (df.groupby(['cat_age'])[['mntwines','mntfruits', 'mntmeatproducts','mntfishproducts','mntsweetproducts','mntgoldprods']]
   .mean()
   .plot(kind='bar', stacked=True,figsize=(10,4), cmap='plasma', ax=ax))

   st.pyplot(fig)
   
   st.header('Average income by education')
   fig, ax = plt.subplots(1, 1, figsize=(10, 4))
   education_order = ['Basic', '2n Cycle', 'Graduation','Master','PhD']
   sns.violinplot(data=df, x='education', y='income',order=education_order, palette='plasma', ax=ax)
   st.pyplot(fig)


   fig, axes = plt.subplots(1, 3, figsize=(18, 5))

   st.header ('First category - elderly')
   sns.boxplot(data=df, x='cat_age', y='income', palette='plasma', ax=axes[0])
   axes[0].set_xlabel('cat_age')
   axes[0].set_ylabel('income')
   axes[0].set_title('BOX PLOT - Income')

   sns.boxplot(data=df, x='cat_age', y='mntwines', palette='plasma', ax=axes[1])
   axes[1].set_xlabel('cat_age')
   axes[1].set_ylabel('mntwines')
   axes[1].set_title('BOX PLOT - Mntwines')

   sns.boxplot(data=df, x='cat_age', y='numwebpurchases', palette='plasma', ax=axes[2])
   axes[2].set_xlabel('cat_age')
   axes[2].set_ylabel('numwebpurchases')
   axes[2].set_title('BOX PLOT - Numwebpurchases')

   st.write('This first category is composed of adults over 53 years old who have a higher annual income (USD), as well as a purchasing pattern focused on wine consumption and online shopping. Therefore, it is suggested to target online advertising for products related to alcoholic beverages.')

   plt.tight_layout()
   st.pyplot(fig)


   fig, axes = plt.subplots(1, 3, figsize=(18, 5))
   st.header ('Second category - young adults')
   sns.boxplot(data=df, x='cat_age', y='mntgoldprods', palette='plasma', ax=axes[0])
   axes[0].set_xlabel('cat_age')
   axes[0].set_ylabel('mntgoldprods')
   axes[0].set_title('BOX PLOT - mntgoldprods')

   sns.boxplot(data=df, x='cat_age', y='numstorepurchases', palette='plasma', ax=axes[1])
   axes[1].set_xlabel('cat_age')
   axes[1].set_ylabel('numstorepurchases')
   axes[1].set_title('BOX PLOT - numstorepurchases')

   sns.boxplot(data=df, x='cat_age', y='mntmeatproducts', palette='plasma', ax=axes[2])
   axes[2].set_xlabel('cat_age')
   axes[2].set_ylabel('mntmeatproducts')
   axes[2].set_title('BOX PLOT - mntmeatproducts')

   st.write('The second category is composed of people under 35 years of age, who have a higher consumption of luxury products and meat, and also represent the second group in purchases in physical stores. Therefore, it is recommended to direct advertising of luxury products and products related to meat in physical stores.  ')

   plt.tight_layout()
   st.pyplot(fig)



   fig, axes = plt.subplots(1, 3, figsize=(18, 5))
   st.header ('Third category - adults')
   sns.boxplot(data=df, x='children', y='mntfruits', hue='cat_age', palette='plasma', ax=axes[0])
   axes[0].set_xlabel('children')
   axes[0].set_ylabel('mntfruits')
   axes[0].set_title('BOX PLOT - mntfruits')

   sns.boxplot(data=df, x='cat_age', y='mntsweetproducts', palette='plasma', ax=axes[1])
   axes[1].set_xlabel('cat_age')
   axes[1].set_ylabel('mntsweetproducts')
   axes[1].set_title('BOX PLOT - mntsweetproducts')

   sns.boxplot(data=df, x='cat_age', y='mntmeatproducts', palette='plasma', ax=axes[2])
   axes[2].set_xlabel('cat_age')
   axes[2].set_ylabel('mntfishproducts')
   axes[2].set_title('BOX PLOT - mntfishproducts')

   st.write('The third category is made up of adults over 35 years old and under 53 years old, who have a high consumption of sweets and fish, as well as the highest average number of children in the household; however, their fruit consumption is the lowest of the population studied. Therefore, it is suggested to create online and in-store advertising that promotes healthy eating habits and a healthy lifestyle. ')
   plt.tight_layout()
   st.pyplot(fig)





