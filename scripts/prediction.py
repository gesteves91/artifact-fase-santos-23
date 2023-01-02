import pdb
from pycaret.classification import *
import pandas as pd

print("Welcome to the \"Yet Another Model! A Study on Model's Similarities for Defect and Code Smells\" prediction script!")
print("In this script you can make the following predictions:")
print("1. God Class")
print("2. Refused Bequest")
print("3. Spaghetti Code")
print("4. Lazy Class")
print("5. Class Data Should Be Private")
print("6. Data Class")
print("7. Speculative Generality")
print("8. Defects")

my_option = input(
    "Please input the number of the target that you want to predict: ")
my_dict = {}
my_dict["1"] = "gc"
my_dict["2"] = "rb"
my_dict["3"] = "sg"
my_dict["4"] = "lc"
my_dict["5"] = "cdspb"
my_dict["6"] = "dc"
my_dict["7"] = "sg"
my_dict["8"] = "defect"

while (my_option not in my_dict):
    my_option = input("Please, input a valid option: ")


df = pd.read_csv('data/unseen/pbeans.csv', index_col=0)
df = df.drop('LongName', 1)
df = df.drop('Name', 1)
df = df.drop('Parent', 1)
df = df.drop('Component', 1)
df = df.drop('Path', 1)
df = df.drop('Line', 1)
df = df.drop('EndLine', 1)
df = df.drop('Column', 1)
df = df.drop('EndColumn', 1)
df.head()

model = f'models/{my_dict[my_option]}'

predict_model(model, data=df, probability_threshold=0.3, raw_score=True)
