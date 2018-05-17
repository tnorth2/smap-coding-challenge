import numpy as np
import csv
import matplotlib.pyplot as plt

# =============================================================================
# # 'import.py'
# =============================================================================
user_iDs = "../data/user_data.csv"

with open(user_iDs,'r') as f:
    user_iter = csv.reader(f, delimiter = ',', quotechar = '"')
    user = [user for user in user_iter]
aUser = np.asarray(user[1:])

laDatetime = []
laConsump = []
aConsumpTotal = [] 
# any index 'i' will refer to the same user across all arrays

for i in range(len(aUser)):
    dest_file = "../data/consumption/" + aUser[i][0] +".csv"
    
    with open(dest_file,'r') as dest_f:
        data_iter = csv.reader(dest_f, delimiter = ',', quotechar = '"')
        data = [data for data in data_iter]
        
    aData = np.asarray(data[1:])
    laDatetime.append(aData[:,0].astype('datetime64'))
    laConsump.append(aData[:,1].astype(float))
    aConsumpTotal.append(np.sum(aData[:,1].astype(float)))

lData_all = [aUser, laDatetime, laConsump]

# =============================================================================
# # Graphing options for the summary section
# =============================================================================

lUsers = []
lConsumpMean=[]
for i in range(len(aUser)):
    lUsers.append(aUser[i][0])
    lConsumpMean.append(np.mean(aConsumpTotal))
    
plt.figure(figsize=(12,6))
plt.title("Total consumption per customer")
plt.bar(lUsers, aConsumpTotal, color='blue', label = "Total Consumption")
plt.plot(lUsers, lConsumpMean, color='red', linestyle='--', label="Mean Consumption")
plt.xticks(rotation=90)
plt.ylabel("Energy consumption (Wh)")
plt.legend()
plt.show()

plt.figure(figsize=(12,6))
plt.title("Consumption over 6 months for one customer (iD: 3011)")
plt.plot(laDatetime[0], laConsump[0], color='blue', label = "Consumption over time")
plt.ylabel("Energy consumption (Wh)")
plt.legend()
plt.show()

# =============================================================================
# For an individual's data
# =============================================================================

plt.figure(figsize=(12,6))
plt.title("Consumption by time of day for one customer (iD: 3011, 2016-07-15)")
plt.plot(laDatetime[0][:47], laConsump[0][:47], color='blue', label = "Consumption over time")
plt.ylabel("Energy consumption (Wh)")
plt.xlim(min(laDatetime[0][:47]), max(laDatetime[0][:47]))
plt.legend()
plt.show()