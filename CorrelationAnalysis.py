#import necessary libraries for analysis
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load Excel file into a Pandas DataFrame
df = pd.read_excel('target_spreadsheet.xlsx', sheet_name='Sheet3')

# Select two columns of data to analyze (change column names as needed)
col1 = df['Length of telomere RNA sequence']
col2 = df['GC content ']

# Calculate correlation coefficient and significance of the correlatoon
corr_coef, p_value = stats.pearsonr(col1, col2)

# Print the correlation coefficient and p value
print("Correlation coefficient: ", corr_coef)
print("P-value: ", p_value)

#create the final scatterplot 
plt.scatter(col1, col2)
plt.xlabel('Length of Telomere RNA Sequence')
plt.ylabel('GC Content')
plt.title('Correlation Between Length of Telomere RNA Sequence and GC Content')
plt.show()

