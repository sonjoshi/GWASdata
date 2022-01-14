import pandas
Path = "/Users/sonali/UCLA/PathwayAnalysis/Project2AA_HA/"

if __name__ == '__main__':
    gene_file = 'HA/HA_genes_20k.txt'
    #gene_file = 'AA/test_genes.txt'
    read_file = Path + gene_file
    df_gene_20K = pandas.read_csv(read_file, sep='\t',na_filter=False )

    multi_file = 'HA/0HA_gene_multi_resolved.txt'
    #multi_file = 'AA/test_modified.txt'
    df_multi_gene = pandas.read_csv(Path + multi_file, sep='\t')

    df_filtered = df_gene_20K[~df_gene_20K.rsID.isin(df_multi_gene.rsID)]
    df_output = pandas.concat([df_filtered, df_multi_gene])
    df_output = df_output.sort_values(by=['ID'])
    df_output.to_csv(Path + "HA/HA_all_resolved.tsv", header=True, sep='\t', index=False, float_format='%g')