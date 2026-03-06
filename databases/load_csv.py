import pandas as pd
import mysql.connector
df=pd.read_csv("data\\cleaned_data.csv")

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
    database="economic_data"
)
cursor=conn.cursor()

for i,row in df.iterrows():
    sql="""
    insert into economy (country,year,GDP,Population,Life_Expectancy,Unemployment_Rate,CO2_Emissions_metric_tons_per_capita,Access_to_Electricity)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    values=(
        row['Country'],
        row['Year'],
        row['GDP_USD'],
        row['Population'],
        row['Life_Expectancy'],
        row['Unemployment_Rate_%'],
        row['CO2_Emissions_metric_tons_per_capita'],
        row['Access_to_Electricity_%']
    )
    cursor.execute(sql,values)
conn.commit()
print("data inserted successfully")

