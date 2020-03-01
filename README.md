# PolarityMining-StackOverflow
This is the code repository of my seminar paper "Polarity mining of Stack Overflow answers in the C and Python subcommunities".
It contains all my Python and SQL scripts for data processing, data analysis and the final presentation

DataProcessing files:

| Files         | Usage         |
| ------------- |:-------------:|
| analyzer.py   | Used to read the data from the csv data dumps, input it into VADER and then inserts everything into the PostgresSQL database |
| codecleaner.py      | Used to clean HTML tags from the answer bodies and remove code and links completely      |
| csvjointer.py | Used to join the csv files from the monthly data dumps      |
| statreader.py | Used to generate some statistics about the data dumps before they were processed      |
| tagprinter.py | Used to print example usages of HTML tags in the answer body       |
| tagreader.py  | Used to find all tags that occur withing the data dumps      |

Data Analysis files:

| Files         | Usage         |
| ------------- |:-------------:|
| answer_number_gen.py | Used to generate random numbers to get a set of numbers for the manual rating process      |
| correlationCalculator.py | Used to calculate the pearson correlation of 2 data dumps      |
| Edited_Answer_Code.py | Used to calculate statistics about answers which were edited and not edited from data dumps      |
| manual_answer_check_puller.py | Used to process data from the database for the manual rating process      |
| manual_rater.py | Used to manually rate answers from data dumps in the console      |
| presentation.py | Used to manually rate answers during the presentation through a graphical interface instead of the console      |
| results_of_manual_rating.py | Uses to display the results of the manual rating in a nice way for the paper     |
| Visualizer.py | Used to generate LateX graphs with Matplotlib from data dumps      |
| SQL files | All the database queries used to gain knowledge from the data. Most queries are commented and explained.  |

Data Acquision files:

| Files         | Usage         |
| ------------- |:-------------:|
| QueryFile.sql | Used to get the data from the live database of Stack Exchange Meta. Only the important skeleton queries, because one query for a 3 month interval is the same as for all other months with only changes to the time interval|
