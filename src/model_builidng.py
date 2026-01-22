
import matplotlib.pyplot as plt
import seaborn as sns

from EDA import df

sns.barplot(
    data=df,
    x='month',
    y='EnergyConsumption',
    hue='HVACUsage'
)

plt.title('Monthly Energy Consumption by HVAC Usage')
plt.xlabel('Month')
plt.ylabel('Energy Consumption')
plt.show()



sns.lineplot(
    data=df,
    x='month',
    y='EnergyConsumption',
    marker='o'
)

plt.title('Monthly Energy Consumption Trend')
plt.show()



sns.barplot(data=df, x='month', y='EnergyConsumption')
plt.title('Month-wise Energy Consumption')
plt.show()




sns.lineplot(data=df, x='hour', y='EnergyConsumption', marker='o')
plt.title('Hourly Energy Consumption')
plt.show()





sns.barplot(data=df, x='DayOfWeek', y='EnergyConsumption')
plt.title('Energy Consumption by Day of Week')
plt.show()




sns.scatterplot(
    data=df,
    x='Temperature',
    y='EnergyConsumption',
    size='Humidity',
    hue='Humidity'
)
plt.title('Energy Consumption vs Temperature & Humidity')
plt.show()






