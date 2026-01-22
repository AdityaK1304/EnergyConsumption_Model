import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from research. import 

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


sns.barplot(
    data=df,
    x='Occupancy',
    y='EnergyConsumption',
    hue='HVACUsage'
)
plt.title('Energy Consumption by Occupancy and HVAC Usage')
plt.show()



sns.boxplot(data=df, x='month', y='EnergyConsumption')
plt.title('Monthly Energy Consumption Distribution')
plt.show()



sns.barplot(data=df, x='Occupancy', y='EnergyConsumption')
plt.title('Energy Consumption by Occupancy')
plt.show()



sns.barplot(data=df, x='HVACUsage', y='EnergyConsumption',color='green')
plt.title('Energy Consumption by HVAC Usage')
plt.show()



fig, ax = plt.subplots(1, 2, figsize=(14,5))

sns.lineplot(data=df, x='month', y='EnergyConsumption', ax=ax[0])
ax[0].set_title('Month-wise Energy Consumption')

sns.lineplot(data=df, x='hour', y='EnergyConsumption', ax=ax[1])
ax[1].set_title('Hour-wise Energy Consumption')

plt.show()




fig, ax = plt.subplots(1, 2, figsize=(14,5))

sns.barplot(data=df, x='Holiday', y='EnergyConsumption', ax=ax[0],color='green')
ax[0].set_title('Holiday vs Energy Consumption')

sns.barplot(data=df, x='DayOfWeek', y='EnergyConsumption', ax=ax[1],color='orange')
ax[1].set_title('Day of Week vs Energy Consumption')

plt.show()



fig, ax = plt.subplots(1, 2, figsize=(14,5))

sns.barplot(data=df, x='Occupancy', y='EnergyConsumption', ax=ax[0],color='purple')
ax[0].set_title('Energy Consumption by Occupancy')

sns.barplot(data=df, x='HVACUsage', y='EnergyConsumption', ax=ax[1],color='red')
ax[1].set_title('Energy Consumption by HVAC Usage')

plt.show()











