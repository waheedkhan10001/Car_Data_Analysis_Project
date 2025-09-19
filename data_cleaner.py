import pandas as pd

# आपकी फ़ाइल का नाम 'CAR_DETAILS.csv' है
file_name = 'CAR_DETAILS.csv'
df = pd.read_csv(file_name)

# डेटा के पहले 5 पंक्तियों को देखें
print("Original data head:")
print(df.head())
print("\n" + "="*30 + "\n")

# हर कॉलम में कितनी खाली वैल्यू हैं, वह जांचें
print("Missing values in each column:")
print(df.isnull().sum())

# यहाँ से नया कोड शुरू होता है
print("\n" + "="*30 + "\n")

# कारों की औसत (average) कीमत पता करें
average_price = df['selling_price'].mean()
print("Average Selling Price:", average_price)

# सबसे आम फ्यूल टाइप (petrol/diesel) पता करें
fuel_counts = df['fuel'].value_counts()
print("\nFuel Types Breakdown:")
print(fuel_counts)