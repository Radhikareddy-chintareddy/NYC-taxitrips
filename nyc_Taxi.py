# %% [markdown]
# 1.	What datetime range does your data cover?  How many rows are there total?

# %%
f=open('trip_data_2.csv','r')
n=0
for line in f:
    print(line)
    n+=1
    if n > 5: 
        break

# %%
import csv
f=open('trip_data_2.csv','r')
r=csv.reader(f)
n=0
for row in r:
    n+=1
    if n%100000==0:
        print(n)
print(n)

# %%
#Datetime Range Pickup
import csv
from datetime import datetime

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)


min_date = None
max_date = None
next(r,None)

for row in r:
    Pickup_date = row[5]
    
   
    date = datetime.strptime(Pickup_date, '%Y-%m-%d %H:%M:%S')
    
    if min_date is None or date < min_date:
        min_date = date
    
    if max_date is None or date > max_date:
        max_date = date
   
f.close()  
if min_date is not None and max_date is not None:
    print(f"Minimum Date: {min_date}")
    print(f"Maximum Date: {max_date}")


# %%
#Datetimerange Dropoff
import csv
from datetime import datetime

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)


min_date = None
max_date = None
next(r,None)

for row in r:
    dropoff_date = row[6]
   
    date = datetime.strptime(dropoff_date, '%Y-%m-%d %H:%M:%S')
    
    if min_date is None or date < min_date:
        min_date = date
    
    if max_date is None or date > max_date:
        max_date = date
   
f.close()  
if min_date is not None and max_date is not None:
    print(f"Minimum Date: {min_date}")
    print(f"Maximum Date: {max_date}")


# %%


# %% [markdown]
# 2.	What are the field names?  Give descriptions for each field.

# %%
import csv
from datetime import datetime

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)
Description = next(r)
print(Description)



# %%


# %% [markdown]
# 3.	Give some sample data for each field.

# %%
f=open('trip_data_2.csv','r')
n=0
for line in f:
    print(line)
    n+=1
    if n > 5: 
        break

# %%


# %%


# %% [markdown]
# 4.	What MySQL data types / len would you need to store each of the fields?
# a.	int(xx), varchar(xx),date,datetime,bool, decimal(m,d)
# 

# %% [markdown]
#  - 0    medallion           Varchar(50) 
#  - 1   hack_license        Varchar(50)
#  - 2   vendor_id           Varchar(50) 
#  - 3   rate_code           int64  
#  - 4   store_and_fwd_flag  Booliean 
#  - 5   pickup_datetime     datetime object 
#  - 6   dropoff_datetime    datetime object
#  - 7   passenger_count     int64  
#  - 8   trip_time_in_secs   int64  
#  - 9   trip_distance       Decimal(4,2)
#  - 10  pickup_longitude    Decimal(8,6)
#  - 11  pickup_latitude     Decimal(8,6)
#  - 12  dropoff_longitude   Decimal(8,6)
#  - 13  dropoff_latitude    Decimal(8,6)

# %% [markdown]
#  7.	What are the distinct values for each field? (If applicable)

# %%
# Medallion 
import csv
f=open('trip_data_2.csv','r')
r=csv.reader(f)
med={}
n=0
for row in r:
    if row[0] not in med:
        med[row[0]]=1
    else:
        med[row[0]]+=1
    
    n+=1
    if n%1000000==0:
        print(n)



med=dict(sorted(med.items(), key=lambda item: item[1],reverse=True))
for k,v in med.items():
    print(k,v)
unique_med = len(med)
print("Number of unique medallion values:", unique_med)

# %%
#Hack Licence
import csv
f=open('trip_data_2.csv','r')
r=csv.reader(f)
hl={}

for row in r:
    if row[1] not in hl:
        hl[row[1]]=1
    else:
        hl[row[1]]+=1
    

hl=dict(sorted(hl.items(), key=lambda item: item[1],reverse=True))
for k,v in hl.items():
    print(k,v)
unique_hack_licence = len(hl)
print("Number of unique hack values:", unique_hack_licence)

# %%

# VendorID, Rate, Store and flag counts
import csv


vendor_id_counts = {}
rate_code_counts = {}
store_and_flag_counts = {}



f = open('trip_data_2.csv', 'r')
r = csv.reader(f)
next(r)

for row in r:
    if row[2] not in vendor_id_counts:
        vendor_id_counts[row[2]] = 1
    else:
        vendor_id_counts[row[2]] += 1

      
    if row[3] not in rate_code_counts:
        rate_code_counts[row[3]] = 1
    else:
        rate_code_counts[row[3]] += 1

        
    if row[4] not in store_and_flag_counts:
        store_and_flag_counts[row[4]] = 1
    else:
        store_and_flag_counts[row[4]] += 1


vendor_id_counts = dict(sorted(vendor_id_counts.items(), key=lambda item: item[1], reverse=True))
rate_code_counts = dict(sorted(rate_code_counts.items(), key=lambda item: item[1], reverse=True))
store_and_flag_counts = dict(sorted(store_and_flag_counts.items(), key=lambda item: item[1], reverse=True))


unique_vendor_id = len(vendor_id_counts)
unique_rate_code = len(rate_code_counts)
unique_store_and_flag = len(store_and_flag_counts)


print("Vendor ID counts:")
for k, v in vendor_id_counts.items():
    print(k, v)
print("Number of unique Vendor IDs:", unique_vendor_id)

print("\nRate Code counts:")
for k, v in rate_code_counts.items():
    print(k, v)
print("Number of unique Rate Codes:", unique_rate_code)

print("\nStore and Forward Flag counts:")
for k, v in store_and_flag_counts.items():
    print(k, v)
print("Number of unique Store and Forward Flags:", unique_store_and_flag)


# %%
#Description of numerical variables like passenger count, trip time and trip distance statistics.
import csv
import math


passenger_counts = []
trip_times = []
trip_distances = []


f = open('trip_data_2.csv', 'r')
r = csv.reader(f)
next(r)

for row in r:
    passenger_counts.append(int(row[7]))  
    trip_times.append(int(row[8]))       
    trip_distances.append(float(row[9]))  

def calculate_median(data):
    data.sort()
    n = len(data)
    middle = n // 2
    if n % 2 == 0:
        return (data[middle - 1] + data[middle]) / 2
    else:
        return data[middle]


passenger_count_mean = sum(passenger_counts) / len(passenger_counts)
passenger_count_std = math.sqrt(sum((x - passenger_count_mean) ** 2 for x in passenger_counts) / len(passenger_counts))


trip_time_mean = sum(trip_times) / len(trip_times)
trip_time_std = math.sqrt(sum((x - trip_time_mean) ** 2 for x in trip_times) / len(trip_times))

trip_distance_mean = sum(trip_distances) / len(trip_distances)
trip_distance_std = math.sqrt(sum((x - trip_distance_mean) ** 2 for x in trip_distances) / len(trip_distances))

print("Passenger Count Statistics:")
print(f"count: {len(passenger_counts)}")
print(f"mean: {passenger_count_mean}")
print(f"std: {passenger_count_std}")
print(f"min: {min(passenger_counts)}")
print(f"25%: {calculate_median(passenger_counts[:len(passenger_counts) // 2])}")
print(f"50%: {calculate_median(passenger_counts)}")
print(f"75%: {calculate_median(passenger_counts[len(passenger_counts) // 2:])}")
print(f"max: {max(passenger_counts)}")

print("\nTrip Time in Seconds Statistics:")
print(f"count: {len(trip_times)}")
print(f"mean: {trip_time_mean}")
print(f"std: {trip_time_std}")
print(f"min: {min(trip_times)}")
print(f"25%: {calculate_median(trip_times[:len(trip_times) // 2])}")
print(f"50%: {calculate_median(trip_times)}")
print(f"75%: {calculate_median(trip_times[len(trip_times) // 2:])}")
print(f"max: {max(trip_times)}")

print("\nTrip Distance Statistics:")
print(f"count: {len(trip_distances)}")
print(f"mean: {trip_distance_mean}")
print(f"std: {trip_distance_std}")
print(f"min: {min(trip_distances)}")
print(f"25%: {calculate_median(trip_distances[:len(trip_distances) // 2])}")
print(f"50%: {calculate_median(trip_distances)}")
print(f"75%: {calculate_median(trip_distances[len(trip_distances) // 2:])}")
print(f"max: {max(trip_distances)}")


# %%
#Null value count
import csv

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)
h = next(r)


null_counts = {column: 0 for column in h}

for row in r:
    for i in range(len(h)):
        if not row[i]:  
            null_counts[h[i]] += 1


for column, count in null_counts.items():
    print(f"{column}: {count} null values")

# %%


# %% [markdown]
# 8.	For other numeric types besides lat and lon, what are the min and max values?

# %%
import csv

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)
n = 0
min_passenger_counts = None
max_passenger_counts = None

for row in r:
    passenger_count = float(row[7]) 
    
    if n == 0:
        min_passenger_counts = passenger_count
        max_passenger_counts = passenger_count
    else:
        if passenger_count > max_passenger_counts:
            max_passenger_counts = passenger_count
        elif passenger_count < min_passenger_counts:
            min_passenger_counts = passenger_count
    
    n += 1

print("Min passenger count:", min_passenger_counts)
print("Max passenger count:", max_passenger_counts)

# %%
import csv

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)
n = 0
min_triptime = None
max_triptime = None

for row in r:
    triptime_sec = float(row[8]) 
    
    if n == 0:
        min_triptime = triptime_sec
        max_triptime = triptime_sec
    else:
        if triptime_sec > max_triptime:
            max_triptime = triptime_sec
        elif triptime_sec < min_triptime:
            min_triptime = triptime_sec
    
    n += 1

print("Min trip time:", min_triptime)
print("Max trip time:", max_triptime)

# %%
import csv

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)
n = 0
min_trip_distance = None
max_trip_distance = None

for row in r:
    trip_distance = float(row[9]) 
    
    if n == 0:
        min_trip_distance = trip_distance
        max_trip_distance = trip_distance
    else:
        if trip_distance > max_trip_distance:
            max_trip_distance = trip_distance
        elif trip_distance < min_trip_distance:
            min_trip_distance = trip_distance
    
    n += 1

print("Min trip distance:", min_trip_distance)
print("Max trip distance:", max_trip_distance)

# %% [markdown]
# For other numeric types like
# 
# Passenger Count Statistics:
# 
# - min: 0
# - max: 208
# 
# Trip Time in Seconds Statistics:
# - min: 0
# - max: 10800
# 
# Trip Distance Statistics:
# 
# - min: 0.0
# - max: 100.0

# %%


# %% [markdown]
# 5.	What is the geographic range of your data (min/max - X/Y)?
# a.	Plot this (approximately on a map)
# 

# %%
#Pickup _Latitude
import csv

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)
n = 0
min_lat = None
max_lat = None

for row in r:
    pickup_lat = float(row[11]) 
    
    if n == 0:
        min_lat = pickup_lat
        max_lat = pickup_lat
    else:
        if pickup_lat > max_lat:
            max_lat = pickup_lat
        elif pickup_lat < min_lat:
            min_lat = pickup_lat
    
    n += 1

print("Min Latitude:", min_lat)
print("Max Latitude:", max_lat)
            
    


# %%
#Pickup_longitude
import csv

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)
n = 0
min_lat = None
max_lat = None

for row in r:
    pickup_lon = float(row[10]) 
    
    if n == 0:
        min_lon = pickup_lon
        max_lon = pickup_lon
    else:
        if pickup_lon > max_lon:
            max_lon = pickup_lon
        elif pickup_lon < min_lon:
            min_lon = pickup_lon
    
    n += 1

print("Min Longitude:", min_lon)
print("Max Longitude:", max_lon)
            
    


# %%
#Dropoff lat and Longitude
import csv

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)
n = 0
min_dropoff_lat = None
max_dropoff_lat = None
min_dropoff_lon = None
max_dropoff_lon = None

for row in r:
    if not row[12] or not row[13]:
        continue  

    try:
        dropoff_lat = float(row[12])
        dropoff_lon = float(row[13])
    except ValueError:
        continue  

    if n == 0:
        min_dropoff_lat = dropoff_lat
        max_dropoff_lat = dropoff_lat
        min_dropoff_lon = dropoff_lon
        max_dropoff_lon = dropoff_lon
    else:
        if dropoff_lat > max_dropoff_lat:
            max_dropoff_lat = dropoff_lat
        elif dropoff_lat < min_dropoff_lat:
            min_dropoff_lat = dropoff_lat

        if dropoff_lon > max_dropoff_lon:
            max_dropoff_lon = dropoff_lon
        elif dropoff_lon < min_dropoff_lon:
            min_dropoff_lon = dropoff_lon
    
    n += 1

print("Min Drop-off Latitude:", min_dropoff_lat)
print("Max Drop-off Latitude:", max_dropoff_lat)
print("Min Drop-off Longitude:", min_dropoff_lon)
print("Max Drop-off Longitude:", max_dropoff_lon)


# %%
#Check the other values since min and max values are seen as outliers

import csv
import math

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        middle = n // 2
        median = (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else:
        median = sorted_data[n // 2]
    return median

pickup_latitudes = []

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)

for row in r:
    pickup_lat_str = row[11]  
    if pickup_lat_str:
        pickup_lat = float(pickup_lat_str)
        pickup_latitudes.append(pickup_lat)

pickup_lat_mean = sum(pickup_latitudes) / len(pickup_latitudes)
pickup_lat_std = math.sqrt(sum((x - pickup_lat_mean) ** 2 for x in pickup_latitudes) / len(pickup_latitudes))

print("Pickup Latitude Statistics:")
print(f"count: {len(pickup_latitudes)}")
print(f"mean: {pickup_lat_mean}")
print(f"std: {pickup_lat_std}")
print(f"min: {min(pickup_latitudes)}")
print(f"25%: {calculate_median(pickup_latitudes[:len(pickup_latitudes) // 2])}")
print(f"50%: {calculate_median(pickup_latitudes)}")
print(f"75%: {calculate_median(pickup_latitudes[len(pickup_latitudes) // 2:])}")
print(f"max: {max(pickup_latitudes)}")


# %%
#Looking at other percentile values to check for outliers
import csv
import math

def calculate_percentile(data, percentile):
    sorted_data = sorted(data)
    n = len(sorted_data)
    index = int((percentile / 100) * (n - 1))
    if index < 0:
        index = 0
    elif index >= n:
        index = n - 1
    return sorted_data[index]

pickup_latitudes = []

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)

for row in r:
    pickup_lat_str = row[11]
    if pickup_lat_str:
        pickup_lat = float(pickup_lat_str)
        pickup_latitudes.append(pickup_lat)

pickup_lat_percentiles = {
    "1%": calculate_percentile(pickup_latitudes, 1),
    "5%": calculate_percentile(pickup_latitudes, 5),
    "95%": calculate_percentile(pickup_latitudes, 95),
    "99%": calculate_percentile(pickup_latitudes, 99)
}

print("Pickup Latitude Percentiles:")
for percentile, value in pickup_lat_percentiles.items():
    print(f"{percentile}: {value}")


# %%
import csv
import math

def calculate_percentile(data, percentile):
    sorted_data = sorted(data)
    n = len(sorted_data)
    index = int((percentile / 100) * (n - 1))
    if index < 0:
        index = 0
    elif index >= n:
        index = n - 1
    return sorted_data[index]

pickup_longitudes = []
dropoff_latitudes = []
dropoff_longitudes = []

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)

for row in r:
    pickup_lon_str = row[10]
    dropoff_lon_str = row[12]
    dropoff_lat_str = row[13]
    
    if pickup_lon_str and pickup_lat_str:
        pickup_lon = float(pickup_lon_str)
        pickup_longitudes.append(pickup_lon)
    if dropoff_lon_str and dropoff_lat_str:
        dropoff_lon = float(dropoff_lon_str)
        dropoff_longitudes.append(dropoff_lon)
        dropoff_lat = float(dropoff_lat_str)
        dropoff_latitudes.append(dropoff_lat)

pickup_lon_percentiles = {
    "1%": calculate_percentile(pickup_longitudes, 1),
    "5%": calculate_percentile(pickup_longitudes, 5),
    "95%": calculate_percentile(pickup_longitudes, 95),
    "99%": calculate_percentile(pickup_longitudes, 99)
}

dropoff_lat_percentiles = {
    "1%": calculate_percentile(dropoff_latitudes, 1),
    "5%": calculate_percentile(dropoff_latitudes, 5),
    "95%": calculate_percentile(dropoff_latitudes, 95),
    "99%": calculate_percentile(dropoff_latitudes, 99)
}

dropoff_lon_percentiles = {
    "1%": calculate_percentile(dropoff_longitudes, 1),
    "5%": calculate_percentile(dropoff_longitudes, 5),
    "95%": calculate_percentile(dropoff_longitudes, 95),
    "99%": calculate_percentile(dropoff_longitudes, 99)
}

print("Pickup Longitude Percentiles:")
for percentile, value in pickup_lon_percentiles.items():
    print(f"{percentile}: {value}")

print("Drop-off Latitude Percentiles:")
for percentile, value in dropoff_lat_percentiles.items():
    print(f"{percentile}: {value}")

print("Drop-off Longitude Percentiles:")
for percentile, value in dropoff_lon_percentiles.items():
    print(f"{percentile}: {value}")


# %%


# %% [markdown]
# 6.	What is the average computed trip distance? (You should use Haversine Distance)
# a.	Draw a histogram of the trip distances binned any way you see fit.
# 

# %%
import csv
import math


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance

trip_dist = []

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)

for row in r:
    pickup_lat_str = row[11]
    pickup_lon_str = row[10]
    dropoff_lat_str = row[13]
    dropoff_lon_str = row[12]

 
    if pickup_lat_str and pickup_lon_str and dropoff_lat_str and dropoff_lon_str:
        pickup_lat = float(pickup_lat_str)
        pickup_lon = float(pickup_lon_str)
        dropoff_lat = float(dropoff_lat_str)
        dropoff_lon = float(dropoff_lon_str)

        distance = haversine(pickup_lat, pickup_lon, dropoff_lat, dropoff_lon)
        trip_dist.append(distance)
    else:
        trip_dist.append(0.0)  


n=0
for distance in trip_dist:
    print(distance)
    n+=1
    if n > 100: 
        break



# %%
print(len(trip_dist))
trip_dist_mean = sum(trip_dist) / len(trip_dist)
trip_dist_std = math.sqrt(sum((x - trip_dist_mean) ** 2 for x in trip_dist) / len(trip_dist))
print("\nTrip Distance Statistics:")
print(f"count: {len(trip_dist)}")
print(f"mean: {trip_dist_mean}")
print(f"std: {trip_dist_std}")
print(f"min: {min(trip_dist)}")
print(f"25%: {calculate_median(trip_dist[:len(trip_dist) // 2])}")
print(f"50%: {calculate_median(trip_dist)}")
print(f"75%: {calculate_median(trip_dist[len(trip_dist) // 2:])}")
print(f"max: {max(trip_dist)}")

# %%
import matplotlib.pyplot as plt
import numpy as np


bin_edges = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]


plt.hist(trip_dist, bins=bin_edges, edgecolor='k', alpha=0.7)
plt.xlabel('Trip Distance')
plt.ylabel('Count')
plt.title('Trip Distance Count Histogram')


bin_labels = [f'{bin_edges[i]} - {bin_edges[i+1]}' for i in range(len(bin_edges)-1)]
plt.xticks(bin_edges[:-1], bin_labels, rotation=45)  

plt.show()

# %%


# %% [markdown]
# 9.	Create a chart that shows the average number of passengers each hour of the day. (X axis should have 24 hours)

# %%
import csv


hourly_count = {}

csv_file = 'trip_data_2.csv'

f = open('trip_data_2.csv', 'r')
r = csv.reader(f)

next(r)

for row in r:
    pickup_datetime = row[5]  
    passenger_count = int(row[7])  


    hour = pickup_datetime.split()[1].split(':')[0]

        
    if hour in hourly_count:
        hourly_count[hour]['passenger_sum'] += passenger_count
        hourly_count[hour]['trip_count'] += 1
    else:
        hourly_count[hour] = {'passenger_sum': passenger_count, 'trip_count': 1}

sorted_hours = sorted(hourly_count.keys(), key=int, reverse=True)

for hour in sorted_hours:
    count = hourly_count[hour]
    average_passengers = count['passenger_sum'] / count['trip_count']
    print(f'Hour: {hour}, Average Passengers: {average_passengers:.2f}')


# %%
import matplotlib.pyplot as plt
import numpy as np

sorted_hours = sorted(hourly_count.keys(), key=int)
average_passengers = [hourly_count[hour]['passenger_sum'] / hourly_count[hour]['trip_count'] for hour in sorted_hours]

plt.figure(figsize=(10, 6))
plt.bar(sorted_hours, average_passengers, width=0.5, align='center', color='skyblue')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Passengers')
plt.title('Hourly Average Passengers')
plt.xticks(np.arange(0, 24))  
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

# %%


# %% [markdown]
# 10.	Create a new CSV file which has only one out of every thousand rows.

# %%
import csv
f=open('trip_data_2.csv','r')
r=csv.reader(f)



f2=open("NYC_Taxi_Subset.csv",'w')
f2.write('')
f2.close()
f2=open('NYC_Taxi_Subset.csv','a')
w=csv.writer(f2,delimiter=',',lineterminator='\n')
n=0
for row in r:
    if n%1000==0:
        w.writerow(row)
        print(n)   
    n+=1


f.close()
f2.close()

# %%
import csv
f2=open("NYC_Taxi_Subset.csv", 'r')
r2 = csv.reader(f2)
row_count = 0  

for row in r2:
    row_count += 1

print("Number of rows in the subset:", row_count)

# %% [markdown]
# 11.	Repeat step 9 with the reduced dataset and compare the two charts.

# %%
import csv


hourly_count = {}



f2 = open('NYC_Taxi_Subset.csv', 'r')
r2 = csv.reader(f2)

next(r2)

for row in r2:
    pickup_datetime = row[5]  
    passenger_count = int(row[7])  


    hour = pickup_datetime.split()[1].split(':')[0]

        
    if hour in hourly_count:
        hourly_count[hour]['passenger_sum'] += passenger_count
        hourly_count[hour]['trip_count'] += 1
    else:
        hourly_count[hour] = {'passenger_sum': passenger_count, 'trip_count': 1}

sorted_hours = sorted(hourly_count.keys(), key=int, reverse=True)

for hour in sorted_hours:
    count = hourly_count[hour]
    average_passengers = count['passenger_sum'] / count['trip_count']
    print(f'Hour: {hour}, Average Passengers: {average_passengers:.2f}')


# %%
import matplotlib.pyplot as plt
import numpy as np

sorted_hours = sorted(hourly_count.keys(), key=int)
average_passengers = [hourly_count[hour]['passenger_sum'] / hourly_count[hour]['trip_count'] for hour in sorted_hours]

plt.figure(figsize=(10, 6))
plt.bar(sorted_hours, average_passengers, width=0.5, align='center', color='skyblue')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Passengers')
plt.title('Hourly Average Passengers')
plt.xticks(np.arange(0, 24))  
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()


