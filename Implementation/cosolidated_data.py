import pandas as pd
import numpy as np
from ClassRoom import *

pre_test = pd.read_excel("pre_test.xlsx")
pre_survey = pd.read_excel("pre_survey.xlsx")
post_test = pd.read_excel("post_test.xlsx")
post_survey = pd.read_excel("post_survey.xlsx")

def module_max():
    p_t_max = []
    pre_test_max = []
    post_test_max = []
    pre_survey_max = []
    post_survey_max = []
    # print(post_test)
    for i in range(1,7):
        post_test_max.append(max(post_test[f'LO_{i}']))
        post_survey_max.append(max(post_survey[f'LO_{i}']))
        pre_test_max.append(max(pre_test[f'LO_{i}']))
        pre_survey_max.append(max(pre_survey[f'LO_{i}']))
    
    p_t_max.append(pre_survey_max)
    p_t_max.append(pre_test_max)
    p_t_max.append(post_survey_max)
    p_t_max.append(post_test_max)
    return p_t_max


def module_min():
    p_t_m = []
    pre_test_min = []
    post_test_min = []
    pre_survey_min = []
    post_survey_min = []
    # print(post_test)
    for i in range(1,7):
        pre_survey_min.append(min(pre_survey[f'LO_{i}']))
        post_survey_min.append(min(post_survey[f'LO_{i}']))
        pre_test_min.append(min(pre_test[f'LO_{i}']))
        post_test_min.append(min(post_test[f'LO_{i}']))
    
    p_t_m.append(pre_survey_min)
    p_t_m.append(pre_test_min)
    p_t_m.append(post_survey_min)
    p_t_m.append(post_test_min)
    return p_t_m


def module_avg():
    presurveylist=[]
    possurveylist=[]
    pretestlist=[]
    postestlist=[]
    p = []
    for i in range(1,7):
        presurveylist.append(pre_survey[f"LO_{i}"].mean())
        possurveylist.append(post_survey[f"LO_{i}"].mean())
        pretestlist.append(pre_test[f"LO_{i}"].mean())
        postestlist.append(post_test[f"LO_{i}"].mean())

    p.append(presurveylist)
    p.append(pretestlist)
    p.append(possurveylist)
    p.append(postestlist)
    return p


# def data_for_graph():
#     post_test_LO = []
#     post_survey_LO = []
#     pre_test_LO = []
#     pre_survey_LO = []
#     consolidated_pre_survey = []    
#     consolidated_pre_test = []
#     consolidated_post_survey = []
#     consolidated_post_test = []
#     consolidated_data = []
#     data = []
#     max_module = module_max()
#     min_module = module_min()
#     module_average = module_avg()
#     data = {}
#     for i in range(0, len(pre_survey.columns)):  # iterates throw all the rows
#         for j in range(4, 10):  # iterated throw column
#             post_test_LO.append(post_test.iloc[i, j])
#             post_survey_LO.append(post_survey.iloc[i, j])
#             pre_test_LO.append(pre_test.iloc[i, j])
#             pre_survey_LO.append(pre_survey.iloc[i, j])
        
#         consolidated_pre_survey.append(pre_survey_LO)
#         consolidated_pre_survey.append(module_average[0])
#         consolidated_pre_survey.append(max_module[0])
#         consolidated_pre_survey.append(min_module[0])
        
#         consolidated_pre_test.append(pre_test_LO)
#         consolidated_pre_test.append(module_average[1])
#         consolidated_pre_test.append(max_module[1])
#         consolidated_pre_test.append(min_module[1])

#         consolidated_post_survey.append(post_survey_LO)
#         consolidated_post_survey.append(module_average[2])
#         consolidated_post_survey.append(max_module[2])
#         consolidated_post_survey.append(min_module[2])

#         consolidated_post_test.append(post_test_LO)
#         consolidated_post_test.append(module_average[3])
#         consolidated_post_test.append(max_module[3])
#         consolidated_post_test.append(min_module[3])

#         consolidated_data.append(consolidated_pre_survey)
#         consolidated_data.append(consolidated_pre_test)
#         consolidated_data.append(consolidated_post_survey)
#         consolidated_data.append(consolidated_post_test)
#         post_test_LO = []
#         post_survey_LO = []
#         pre_test_LO = []
#         pre_survey_LO = []
#         data[post_test.iloc[i, 1]] = consolidated_data
#         consolidated_data = []
#         consolidated_pre_survey = []
#         consolidated_pre_test = []
#         consolidated_post_survey = []
#         consolidated_post_test = []
#     return data

# def top_performer():
#     max_li_pre_test = []
#     max_li_post_test = []
#     max_li_pre_survey = []
#     max_li_post_survey = []
#     max_li = []
#     for i in range(1,7):
#         max_li_pre_test.append(max(pre_test[f'LO_{i}']))
#         max_li_post_survey.append(max(post_survey[f'LO_{i}']))
#         max_li_post_test.append(max(post_test[f'LO_{i}']))
#         max_li_pre_survey.append(max(pre_survey[f'LO_{i}']))
    
#     max_li.append(max_li_pre_survey)
#     max_li.append(max_li_pre_test)
#     max_li.append(max_li_post_survey)
#     max_li.append(max_li_post_test)
#     return max_li

# def bottom_performer():
#     min_li_pre_test = []
#     min_li_post_test = []
#     min_li_pre_survey = []
#     min_li_post_survey = []
#     min_li = []
#     for i in range(1,7):
#         min_li_pre_test.append(min(pre_test[f'LO_{i}']))
#         min_li_post_survey.append(min(post_survey[f'LO_{i}']))
#         min_li_post_test.append(min(post_test[f'LO_{i}']))
#         min_li_pre_survey.append(min(pre_survey[f'LO_{i}']))
    
#     min_li.append(min_li_pre_survey)
#     min_li.append(min_li_pre_test)
#     min_li.append(min_li_post_survey)
#     min_li.append(min_li_post_test)
#     return min_li
