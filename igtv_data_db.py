import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

#connecting to mysql database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rodney",
    database="igtv_data_db"
)

#Perform a SQL query to retrieve data
query = """
SELECT title, views, likes, comments, upload_date
FROM igtv_videos;
"""

# Read the data into a Pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Display the DataFrame
print(df)

# Group data by upload date and calculate total views, likes, and comments
daily_metrics = df.groupby('upload_date').agg({
    'views': 'sum',
    'likes': 'sum',
    'comments': 'sum'
}).reset_index()

# Create line plots for views, likes, and comments over time
plt.figure(figsize=(10, 5))
plt.plot(daily_metrics['upload_date'], daily_metrics['views'], label='Views')
plt.plot(daily_metrics['upload_date'], daily_metrics['likes'], label='Likes')
plt.plot(daily_metrics['upload_date'], daily_metrics['comments'], label='Comments')
plt.xlabel('Upload Date')
plt.ylabel('Count')
plt.title('IGTV Performance Metrics Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Show the chart
plt.show()
