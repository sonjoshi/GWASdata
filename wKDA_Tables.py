# coding=utf-8
#This file formats results to make wKDA tables for publication
import pandas
import numpy

Path = "/Users/sonali/UCLA/Project3IL6_CRP/Mergeomics/DiseaseAssociation/3T2D/50KB/LocusPerm/"

# Read the Excel file
def read_excel_file(file_name, sheet, ref_mark):
    read_file = Path + file_name
    df = pandas.read_excel(read_file, sheet_name=sheet)
    print(read_file, sheet)
    df = df.loc[df['IsSignificant'] == 'Significant']
    n_rows = len(df)

    #Create a comma separated list of genes for each module
    df = df.sort_values("MODULE")
    group_by_module = df.groupby("MODULE")
    #print(group_by_module.groups)
    df_output=[]
    for module,group in group_by_module:
        #Keep only the top 5 KDs for each module sorted by FDR
        group = group.sort_values(by=['FDR'])
        if len(group) > 5:
            group = group[0:5]

        # Identify member status
        group_by_membership = group.groupby("MEMBER")

        #Initialize node list variables
        true_nodes = ''
        false_nodes = ''

        for a,b in group_by_membership: #Add * for if member

            if a is True:
                true_nodes = '*,'.join(b['NODE'].values.tolist())

            else: #a is False:
                false_nodes =  ','.join(b['NODE'].values.tolist())

        if true_nodes:
            true_nodes = true_nodes + '*'
        if false_nodes:
            if true_nodes:
                true_nodes = true_nodes + ','


        Nodes = true_nodes+false_nodes
        Module_size = group.iloc[0]['N.mod'].astype(str)+ ref_mark
        print(Module_size)
        df_output.append(
            {
                'MODULE':module,
                'DESCR':group.iloc[0]['DESCR'], #Get the module size and description
                'N.mod':Module_size,
                #'N.mod':group.iloc[0]['N.mod'],
                #'Nodes':'\u2217 ,'.join(group['NODE'].values.tolist())
                #'Nodes': ','.join(group['NODE'].values.tolist())
                #'Member Nodes': true_nodes,
                #'Non-Member Nodes':false_nodes
                'Nodes':Nodes
            }
        )

    df_output = pandas.DataFrame(df_output)
    #print(df_output)
    #df_output.to_csv(Path+'adipose'+".tsv", header=True, sep='\t', index=False )
    return df_output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_file = 'T2D_50KBLocus_RearrangedResults.xlsx'
    print('File-', my_file)

    sheet_name = 'Adipose_wKDA'
    ref_mark = '*'
    print('Tissue-', sheet_name)
    df_output = read_excel_file(my_file, sheet_name, ref_mark)
    df_output.to_csv(Path + sheet_name + "_top5.tsv", header=True, sep='\t', index=False)
    sheet_name = 'Blood_wKDA'
    ref_mark = '**'
    print('Tissue-', sheet_name)
    df_output = read_excel_file(my_file, sheet_name, ref_mark)
    df_output.to_csv(Path + sheet_name + "_top5.tsv", header=True, sep='\t', index=False)
    sheet_name = 'Liver_wKDA'
    ref_mark = '^'
    print('Tissue-', sheet_name)
    df_output = read_excel_file(my_file, sheet_name, ref_mark)
    df_output.to_csv(Path + sheet_name + "_top5.tsv", header=True, sep='\t', index=False)
    sheet_name = 'Muscle_wKDA'
    ref_mark = '~'
    print('Tissue-', sheet_name)
    df_output = read_excel_file(my_file, sheet_name, ref_mark)
    df_output.to_csv(Path + sheet_name + "_top5.tsv", header=True, sep='\t', index=False)
    sheet_name = 'PPI_wKDA'
    ref_mark = '"'
    print('Tissue-', sheet_name)
    df_output = read_excel_file(my_file, sheet_name, ref_mark)
    df_output.to_csv(Path + sheet_name + "_top5.tsv", header=True, sep='\t', index=False)

    # For all results that are 'significant' (column M)
        # Group by the module name
        # For each module,
            # Make a comma separated list of all the nodes in each module
            # Save in a dataframe Module name, Module description, N.mod and the list of nodes
    # Create output file using the sheet name
    # Copy the dataframe (Module, Descr, N.mod, Node list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
