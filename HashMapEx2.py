'''
What was the temperature on Jan 9?
What was the temperature on Jan 4?
'''
weather_data = {}
with open('Files/nyc_weather.csv','r') as f:
    for line in f:
        data = line.split(',')
        try:
            temp = int(data[1])
            date = data[0]
            weather_data[date] = temp
        except:
            print('Invalid Temperature. Ignore the row.')
print(weather_data)
# Temperature on Jan 9
print(weather_data['Jan 9'])
# Temperature on Jan 4
print(weather_data['Jan 4'])
# Data Structure best for this problem was dictionary(internally hash table) as we need to access temperature using date (look up temp by day -> O(1))