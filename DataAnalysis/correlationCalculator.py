from scipy.stats.stats import pearsonr
import csv


def calculate_pearson_polarity_account_number():
    monthly_Account_creations_file = open("./QueryDumps/Number_Of_Registered_Users_Monthly.csv", mode="r", encoding="utf8")
    monthly_compound_val_c = open("./QueryDumps/Average_Compound_All_Monthly_Python.csv", mode="r", encoding="utf8")

    account_values = []
    compound_values = []

    reader_accounts = csv.reader(monthly_Account_creations_file, delimiter = ",")
    reader_compound = csv.reader(monthly_compound_val_c, delimiter = ",")
    for row in reader_accounts:
        account_values.append(int(row[0]))
    for row in reader_compound:
        compound_values.append(float(row[0]))
    pearson_correlation = pearsonr(account_values, compound_values)
    print("The pearson correlation of C and Number of Accounts", pearson_correlation)


calculate_pearson_polarity_account_number()