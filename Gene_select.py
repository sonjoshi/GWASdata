# coding=utf-8
#This program looks at all the SNPs mapped to multiple genes and tries to keep only genes that
#are "protein coding". The Homo_sapiens.gene_info.csv file gives the 'type' of each gene.
#If no protein-coding genes are found then all the genes are kept.

import pandas
import numpy
Path = "/Users/sonali/UCLA/PathwayAnalysis/Project2AA_HA/"

if __name__ == '__main__':
    #This file is downloaded from the NCBI ftp site. Gives type of each gene.
    gene_file = 'Homo_sapiens.gene_info.csv'
    read_file = Path+gene_file
    df_gene_info = pandas.read_csv(read_file)

    multi_file = 'HA/0HA_gene_multi.txt'
    df_multi_gene = pandas.read_csv(Path+multi_file, sep='\t')
    z=0

    group_by_genelist = df_multi_gene.groupby("gene")
    for group in group_by_genelist:
        x = 0
        y = 0
        gene_protein_coding = ""
        gene_others = ""
        genes_keep = ""
        genes_remove = ""
        for gene in group[0].split(","):
            df_temp = df_gene_info.loc[df_gene_info["Symbol"] == gene]
            #In some cases the gene is not found in the NCBI file.
            try:
                gene_type = df_temp.iloc[0]["type_of_gene"]
            except:
                print("Error in gene", gene)
                gene_type = 'Others'

            if str(gene_type) == "protein-coding":
                #protein_coding_gene = "str(gene_type)"
                if x == 0:
                    gene_protein_coding = gene
                if x >= 1:
                    gene_protein_coding = gene_protein_coding + ", " + gene
                x=x+1
            else:
                if y==0:
                    gene_others = gene
                if y>= 1:
                    gene_others = gene_others + ", " + gene
                y=y+1
        if x==0:
            message = "No protein coding genes."
            genes_keep = gene_others
            genes_remove = "N/A"
        elif x == 1:
            message = "Kept one gene"
            genes_keep = gene_protein_coding
            genes_remove = gene_others
        elif x>1 and y==0:
            message = "All genes are protein coding"
            genes_keep = gene_protein_coding
            genes_remove = "N/A"
        else:
            message = "Kept protein coding genes"
            genes_keep = gene_protein_coding
            genes_remove = gene_others

        #print(x, genes_keep, y, genes_remove, message)
        #Create the output dataframe, change the gene column and
        # add columns for genes_removed and comments

        df_temp1 = pandas.DataFrame(group[1])
        df_temp1.loc[:,'Genes to keep'] = str(genes_keep)
        df_temp1.loc[:,'Genes to remove'] = str(genes_remove)
        df_temp1.loc[:,'Comments'] = str(message)

        if z == 0:
            df_output = df_temp1
            z=1
        else:
            df_temp2 = df_output
            df_output = pandas.concat([df_temp2,df_temp1])

    #print(df_output)
    df_output = df_output.sort_values(by=['CHROM','POS'])
    #df_output.to_csv(Path + "HA/gene_file.tsv", header=True, sep='\t', index=False)
