import plotly.graph_objects as go
import plotly.io as pio
import psycopg2 as postgres
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import csv
from matplotlib.font_manager import FontProperties

# User Matplotlib for export to Latex
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# gebraucht um nur die Jahre anzugeben
def format_funcC(value, tick_number):
    return str(tick_number+2007)


def format_func(value, tick_number):
    return str(tick_number+2007)

def format_func9(value, tick_number):
    return str(tick_number+2008)
def databaseAccess():
    databaseConnection = postgres.connect(host="localhost", dbname="DataAnalytics", user="postgres", password="1")
# create a cursor to execute commands
    databaseCursor = databaseConnection.cursor()



    databaseCursor.execute("select to_char(creationdate, 'YYYY-MM') as year_month, count(to_char(creationdate, 'YYYY-MM')) as number_of_answers from posts where community = 1 group by to_char(creationdate, 'YYYY-MM');")
    #databaseCursor.execute("select to_char(creationdate, 'YYYY-MM') as year_month, count(to_char(creationdate, 'YYYY-MM')) as number_of_answers from posts where community = 1 group by to_char(creationdate, 'YYYY-MM');")
    result = databaseCursor.fetchall()

    years = []
    answers = []

    for row in result:
        years.append(row[0])
        answers.append(row[1])

    # An welchen Stellen sollen Tick angezeigt werden
    tick_spacing = 12
    return [years, answers, tick_spacing]



#values = databaseAccess()

def calculateUsersPerMonth():
    numberOfAccountCreations = open("./QueryDumps/Number_AccountCreation_pear_year_monthly.csv", mode="r", encoding="utf8")
    registered = open("./QueryDumps/Number_Of_Registered_Users_Monthly.csv", mode="w", newline='', encoding="utf8")
    reader = csv.reader(numberOfAccountCreations, delimiter=",")
    csvWriter = csv.writer(registered, delimiter=',')
    users = []
    prevUsers = 0
    for row in reader:
        users.append(prevUsers+int(row[0]))
        prevUsers += int(row[0])
        csvWriter.writerow([prevUsers])
    return users

def fromFileReaderOverAllUsers():
    file = open("./QueryDumps/Number_AccountCreation_pear_year_monthly.csv", mode="r", encoding="utf8")
    reader = csv.reader(file, delimiter=",")
    years = []
    tick_spacing = 12
    for row in reader:
        if row[1] == '2020':
            break
        #year_values.append(float(row[0]))
        years.append(row[1])
    year_values = calculateUsersPerMonth()
    return [years, year_values, tick_spacing]


def fromFileReader():
    file = open("./QueryDumps/Number_AccountCreation_pear_year_monthly.csv", mode="r", encoding="utf8")
    reader = csv.reader(file, delimiter=",")
    year_values = []
    years = []
    tick_spacing = 12
    for row in reader:
        if row[1] == '2020':
            break
        year_values.append(int(row[0]))
        #year_values.append(float(row[0]))
        years.append(row[1])
    return [years, year_values, tick_spacing]

def statistic_score_over_time():
    file = open("./QueryDumps/average_score_comments_per_top_answers_c_yearly.csv", mode="r", encoding="utf8")
    reader = csv.reader(file, delimiter=",")
    usersYears = []
    year_values = []
    years = []
    tick_spacing = 1
    currentuservalues = []
    currentUser = 15168
    #currentUser = 100297
    for row in reader:
        if int(row[2]) == currentUser:
            currentuservalues.append(float(row[0]))
            usersYears.append(row[3])
        else:
            year_values.append(currentuservalues)
            currentuservalues = [float(row[0])]

            currentUser = int(row[2])
            if len(usersYears) > len(years):
                years = usersYears

            usersYears = []

        #year_values.append(float(row[0]))
        # otherwise we add years multiple times
    year_values.append(currentuservalues)
    if len(usersYears) > len(years):
        years = usersYears
    return [years, year_values, tick_spacing]
def statistic_score_over_time2():
    file = open("./QueryDumps/yearly_number_answers_top_c.csv", mode="r", encoding="utf8")
    reader = csv.reader(file, delimiter=",")
    year_values = []
    c = []
    p = []
    years = []
    tick_spacing = 1
    for row in reader:
        years.append(row[1])
        c.append(int(row[0]))
        p.append(int(row[2]))
    year_values.append(c)
    year_values.append(p)
    return [years, year_values, tick_spacing]


def statistic_score_over_time_compound():
    file = open("./QueryDumps/Top_10_compound_python_average_yearly.csv", mode="r", encoding="utf8")
    reader = csv.reader(file, delimiter=",")
    usersYears = []
    year_values = []
    years = []
    tick_spacing = 1
    currentuservalues = []
    currentUser = 100297
    for row in reader:
        if int(row[0]) == currentUser:
            currentuservalues.append(float(row[1]))
            usersYears.append(row[2])
        else:
            year_values.append(currentuservalues)
            currentuservalues = [float(row[1])]

            currentUser = int(row[0])
            if len(usersYears) > len(years):
                years = usersYears

            usersYears = []

        #year_values.append(float(row[0]))
        # otherwise we add years multiple times
    year_values.append(currentuservalues)
    if len(usersYears) > len(years):
        years = usersYears
    return [years, year_values, tick_spacing]

#values = fromFileReader()
#values = fromFileReaderOverAllUsers()
#values = databaseAccess()
#ploz genertion

values = statistic_score_over_time()
#values = statistic_score_over_time_compound()

fig, ax = plt.subplots(1, 1)
a = np.array(values[0])
b = np.array(values[1])


lines = []
for row in b:
    lines += ax.plot(a, row)
#ax.plot
ax.xaxis.set_major_locator(ticker.MultipleLocator(values[2]))
ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
plt.xlabel("Time in yearly intervals")
plt.ylabel("Average voting score")
#plt.show()

fP = FontProperties()
fP.set_size('small')
plt.legend(['userid = 15168', 'userid = 28169', 'userid = 440558', 'userid = 2173917', 'userid = 2410359'], loc='upper right')


#plt.legend(['userid = 100297', 'userid = 104349', 'userid = 190597', 'userid = 771848', 'userid = 2901002'], loc='upper right')
#plt.legend(['community = c', 'community = python'], loc='upper left')
plt.savefig('./Plots/Average_voting_score_c_top_5_yearly.pgf')


# fig = {
#     "data": [{"type": "scatter",
#               "x": years,
#               "y": answers}],
#     "layout": {"title": {"text": "Number of answers on questions tagged with Python each month"}}
# }
# #TODO test whether that code works
# pio.write_image(fig, './filename.png', width=1920, height=1080)
# pio.show(fig)






