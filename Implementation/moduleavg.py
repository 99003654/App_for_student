import pandas as pd

# Import all the excel files
pre_test = pd.read_excel("pre_test.xlsx")
pre_survey = pd.read_excel("pre_survey.xlsx")
post_test = pd.read_excel("post_test.xlsx")
post_survey = pd.read_excel("post_survey.xlsx")



def mod_avg():
    prelist=[]
    for i in range(1,7):
        prelist.append(pre_survey[f"LO_{i}"].mean())
    return prelist
mod_avg()
