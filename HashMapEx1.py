'''
stock_prices = []
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])

'''
temp_list = []
with open('Files/nyc_weather.csv','r') as f:
    for line in f:
        data = line.split(',')
        try:
            temp = int(data[1])
            temp_list.append(temp)
        except:
            print("Invalid temperature. Ignore the row.")
# Average temperature in first week
first_week_avg = sum(temp_list[:7])/7
print(first_week_avg)
# Maximum temperature in first 10 days
max_temp = max(temp_list[:10])
print(max_temp)
# Data Structure best for this problem was list as we only need to access temperature