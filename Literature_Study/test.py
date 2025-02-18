from datetime import datetime, timedelta

import pandas as pd



# Calculate the dates for the next weeks up until 6 months from now

start_date = datetime.today()

end_date = start_date + timedelta(days=30*6)  # Approximately 6 months



# Generate a list of dates from today to 6 months in the future, weekly

dates = pd.date_range(start_date, end_date, freq='W').date



# Create a DataFrame with a single 'Task' column, the dates will be the column headers

df = pd.DataFrame(columns=['Task'] + dates.strftime('%Y-%m-%d').tolist())



# Save the DataFrame to an Excel file

excel_filename = './Tasks_and_Dates.xlsx'

df.to_excel(excel_filename, index=False)
