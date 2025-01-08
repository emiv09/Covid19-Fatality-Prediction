import pandas as pd

# Încărcarea datelor
file_path = 'C:\\Users\\emili\\Desktop\\fac\\master\\Machine Learning\\Project\\dataset\\raw\\WHO-COVID-19-cases.csv'
data = pd.read_csv(file_path)

 # Filtrarea datelor pentru România
romania_data = data[data['Country'] == 'Romania']

    # Verificarea rezultatului filtrării
print("\nPrimele 5 rânduri pentru România:")
print(romania_data.head())
print(romania_data.tail())


# Salvarea datelor filtrate (opțional)
romania_data.to_csv('C:\\Users\\emili\\Desktop\\fac\\master\\Machine Learning\\Project\\dataset\\interim\\romania_covid_data.csv', index=False)
print("\nDatele pentru România au fost salvate.")


