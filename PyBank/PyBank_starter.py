# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
import pandas as pd

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
total_profit_losses = 0
profit_losses_changes = []
previous_profit = None
greatest_increase = ["", 0]  # [date, amount]
greatest_decrease = ["", 0]  # [date, amount]
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
df = pd.read_csv('budge_data.csv')

    # Skip the header row
header = next(reader)

    # Extract first row to avoid appending to net_change_list
net_change_list = []
    previous_profit = df['Profit/Losses'].iloc[0]
    for index in range (1,len(df)):
        current_profit = df['Profit/Losses'].iloc[index]
        change = current_profit - previous_profit
        net_change_list.append(change)
        previous_profit = current_profit

    # Track the total and net change


    # Process each row of data
    for row in reader:
        date = row[0]
        profit_losses = int(row[1])

        # Track the total
        total_months +=1

        # Track the net change
        total_profit_losses += profit_losses
        if previous_profit is not None:
            change = profit_losses - previous_profit
            profit_losses_changes.append(change)

        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase[1]:
            greatest_increase = [date,change]


        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease[1]:
            greatest_decrease = [date,change]

            previous_profit = profit_losses

# Calculate the average net change across the months
average_change = sum(profit_losses_changes) / len(profit_losses_changes) if profit_losses_changes else 0

# Generate the output summary
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(results)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
