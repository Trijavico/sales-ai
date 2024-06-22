import pandas as pd


df = pd.read_csv("Hellium10.csv")


columns_to_keep = [
    'Unnamed: 0', 'ASIN', 'Title_x', 'Brand', 'Category', 'BSR', 'Subcategory', 
    'Price', 'Price Trend (90 days) (%)', 'Monthly Sales', 'Sales Trend (90 days) (%)', 
    'Monthly Revenue', 'Review Count', 'Reviews Rating', 'Best Sales Period'
]


df = df[columns_to_keep]


print("Valores faltantes antes de rellenar:")
print(df['Price Trend (90 days) (%)'].isna().sum())

df['Price Trend (90 days) (%)'] = pd.to_numeric(df['Price Trend (90 days) (%)'], errors='coerce')

mean_value = df['Price Trend (90 days) (%)'].mean()


rounded_mean_value = round(mean_value, 2)
print(f"Promedio redondeado de 'Price Trend (90 days) (%)': {rounded_mean_value}")


df['Price Trend (90 days) (%)'].fillna(rounded_mean_value, inplace=True)


print("Valores faltantes después de rellenar:")
print(df['Price Trend (90 days) (%)'].isna().sum())

