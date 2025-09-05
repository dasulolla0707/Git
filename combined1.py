import pandas as pd

files = [
   r"D:\Dasu\Web_scraping\input\turkey\Turkey_part1.csv",
    r"D:\Dasu\Web_scraping\input\turkey\Turkey_part2.csv", 
    r"D:\Dasu\Web_scraping\input\turkey\Turkey_part3.csv"
]

# Read with latin-1 encoding and save as UTF-8
df = pd.concat([pd.read_csv(f, encoding='latin-1') for f in files])
df.to_csv("Turkey_combined.csv", index=False, encoding='utf-8')

print("✅ Files combined successfully with latin-1 encoding!")