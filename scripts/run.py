import pdb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from pycaret.classification import *


root_dir = os.getcwd()
df = pd.read_csv(f'{root_dir}/data/final/defects_smells.csv', index_col=0)
df_type = df['Type']
df.shape

duplicate_rows = df[df.duplicated()]

df = df.drop('LongName', 1)
df = df.drop('Name', 1)
df = df.drop('Parent', 1)
df = df.drop('Component', 1)
df = df.drop('Path', 1)
df = df.drop('Line', 1)
df = df.drop('EndLine', 1)
df = df.drop('Column', 1)
df = df.drop('EndColumn', 1)
df = df.drop('Type', 1)

df = df.drop('fe', 1)
df = df.drop('dico', 1)
df = df.drop('ic', 1)
df = df.drop('lpl', 1)
df = df.drop('mc', 1)
df = df.drop('ss', 1)
df = df.drop('lm', 1)

print("Welcome to the \"Yet Another Model! A Study on Model's Similarities for Defect and Code Smells\" prediction script!")
print("In this script you can make the following predictions:")
print("1. God Class")
print("2. Refused Bequest")
print("3. Spaghetti Code")
print("4. Lazy Class")
print("5. Class Data Should Be Private")
print("6. Data Class")
print("7. Speculative Generality")
print("8. Defects\n")

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

target = my_dict[my_option]

list_of_smells = ["rb", "cdsbp", "dacl", "lc", "sc", "sg", "gc", "bug"]
list_of_smells.remove(target)

for items in list_of_smells:
    df = df.drop(items, 1)
    print(items)

corr = df.corr()
threshold = 0.99

columns = np.full((corr.shape[0],), True, dtype=bool)
for i in range(corr.shape[0]):
    for j in range(i+1, corr.shape[0]):
        if corr.iloc[i, j] >= threshold:
            print(df.columns[i], df.columns[j])
            if columns[j]:
                columns[j] = False
selected_columns = df.columns[columns]
high_corr = set(df.columns) - set(selected_columns)
df = df[selected_columns]

df['Type'] = df_type

results = df[target].values
df = df.drop(target, axis=1)
df[target] = results

s = setup(
    data=df, target=target,
    feature_selection=True,
    remove_multicollinearity=True,
    multicollinearity_threshold=0.85,
    feature_selection_method='boruta',
    fix_imbalance=True, fold=10, silent=True,
    html=False
)

df = get_config('X')

print('\nSaving the features file to csv')
selected_features = list(get_config('X').columns)
with open(f'tests/features_{target}.csv', 'w') as f:
    f.write("\n".join(selected_features))

top5_models = compare_models(n_select=5, sort='f1')

tuned_top5 = [
    tune_model(
        i,
        n_iter=30,
        optimize="f1",
        search_library='optuna',
        choose_better=True,
        early_stopping=True)
    for i in top5_models
]

blended_models = blend_models(
    tuned_top5,
    choose_better=True,
    optimize="f1")

pred = predict_model(blended_models)

result = pull()
result.to_csv(f'tests/models_{target}.csv')

final_best = finalize_model(blended_models)

my_save_location = f'tests/{target}'
save_model(final_best, my_save_location)

interpret_model(tuned_top5[0], save=True)
