import pandas as pd
import matplotlib.pyplot as plt


file_path = 'C:\Users\91992\OneDrive\Desktop\Hitraj study\CLG\PROJECT\data set.csv'  
data = pd.read_excel(file_path)


print(data.head())


plt.figure(figsize=(12, 8))


columns_to_plot = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']


for column in columns_to_plot:
    plt.plot(data[column], label=column)


plt.title('Air Quality Parameters')
plt.xlabel('Sample Index')  
plt.ylabel('Concentration (µg/m³ or ppm)')  
plt.legend()
plt.grid()
plt.show()