import pandas as pd
import numpy as np
import itertools

def utilities_list(csv, exclude_csv, include_csv, utility_csv):
    
    df_utility = pd.read_csv(utility_csv)

    utility_ls = []

    for index, row in df_utility.iterrows():
        utility_ls.append(row['Name'])


    df = pd.read_csv(csv)
    # df = df[['Client Name', 'Client Status', 'Contract Name', 'Account Manager', 'Status', 'Type', 'Excludes Utilities', 'Includes Utilities']]
    # Exludes_Utilities Output
    df['Excludes Utilities'] = df['Excludes Utilities'].astype(str)
    ex_client_ls = []
    ex_client_status_ls = []
    ex_contract_ls = []
    ex_am_ls = []
    ex_status_ls = []
    ex_type_ls = []
    ex_utility_ls = []

    for index, row in df.iterrows():
        ex_client_ls.append(row['Client Name'])
        ex_client_status_ls.append(row['Client Status'])
        ex_contract_ls.append(row['Contract Name'])
        ex_am_ls.append(row['Account Manager'])
        ex_status_ls.append(row['Status'])
        ex_type_ls.append(row['Type'])
        ex_utility_ls.append(row['Excludes Utilities'].split('|'))
        
    ex_utility_ls = list(zip(ex_client_ls, ex_client_status_ls, ex_contract_ls, ex_am_ls, ex_status_ls, ex_type_ls, ex_utility_ls))

    ex_client_ls2 = []
    ex_client_status_ls2 = []
    ex_contract_ls2 = []
    ex_am_ls2 = []
    ex_status_ls2 = []
    ex_type_ls2 = []
    ex_utility_ls2 = []

    for ls in ex_utility_ls:
        for utility in ls[6]:
            ex_client_ls2.append(ls[0])
            ex_client_status_ls2.append(ls[1])
            ex_contract_ls2.append(ls[2])
            ex_am_ls2.append(ls[3])
            ex_status_ls2.append([ls[4]])
            ex_type_ls2.append(ls[5])
            ex_utility_ls2.append(utility)
            
    df_ls = [ex_client_ls2, ex_client_status_ls2, ex_contract_ls2, ex_am_ls2, ex_status_ls2, ex_type_ls2, ex_utility_ls2]
    labels = ['Client', 'Client Status', 'Contract Name', 'Account Manager', 'Contract Status', 'Type', 'Utility']
    df_output = pd.DataFrame(df_ls, labels).T
    df_output = df_output[df_output['Utility'] != 'nan']


    df_output['Utility_Check'] = df_output['Utility'].isin(utility_ls)


    df_output.to_csv(exclude_csv, index=False)

    #Includes_Utilities Output
    df['Includes Utilities'] = df['Includes Utilities'].astype(str)
    in_client_ls = []
    in_client_status_ls = []
    in_contract_ls = []
    in_am_ls = []
    in_status_ls = []
    in_type_ls = []
    in_utility_ls = []

    for index, row in df.iterrows():
        in_client_ls.append(row['Client Name'])
        in_client_status_ls.append(row['Client Status'])
        in_contract_ls.append(row['Contract Name'])
        in_am_ls.append(row['Account Manager'])
        in_status_ls.append(row['Status'])
        in_type_ls.append(row['Type'])
        in_utility_ls.append(row['Includes Utilities'].split('|'))
        
    in_utility_ls = list(zip(in_client_ls, in_client_status_ls, in_contract_ls, in_am_ls, in_status_ls, in_type_ls, in_utility_ls))

    in_client_ls2 = []
    in_client_status_ls2 = []
    in_contract_ls2 = []
    in_am_ls2 = []
    in_status_ls2 = []
    in_type_ls2 = []
    in_utility_ls2 = []

    for ls in in_utility_ls:
        for utility in ls[6]:
            in_client_ls2.append(ls[0])
            in_client_status_ls2.append(ls[1])
            in_contract_ls2.append(ls[2])
            in_am_ls2.append(ls[3])
            in_status_ls2.append([ls[4]])
            in_type_ls2.append(ls[5])
            in_utility_ls2.append(utility)
            
    df_ls = [in_client_ls2, in_client_status_ls2, in_contract_ls2, in_am_ls2, in_status_ls2, in_type_ls2, in_utility_ls2]
    labels = ['Client', 'Client Status', 'Contract Name', 'Account Manager', 'Contract Status', 'Type', 'Utility']
    df_output = pd.DataFrame(df_ls, labels).T
    df_output = df_output[df_output['Utility'] != 'nan']
    


    df_output['Utility_Check'] = df_output['Utility'].isin(utility_ls)


    df_output.to_csv(include_csv, index=False)


utilities_list(csv="/Users/christopherdiaz/Jupyter Notebooks/SRXX Utility Settings 171218.csv", exclude_csv = "/Users/christopherdiaz/Jupyter Notebooks/excludes_test_171218.csv", include_csv = "/Users/christopherdiaz/Jupyter Notebooks/includes_test_171218.csv.csv", utility_csv ="/Users/christopherdiaz/Jupyter Notebooks/Electric Utilities (1).csv")

