#This program finds the SNPs (chr:pos) that were not mapped to rsID
#Finds the rows that have '.' in the rsID column
import pandas
Path = "/Users/sonali/UCLA/Project3IL6_CRP/IL6/"

if __name__ == '__main__':
    rsid_file = 'IL6_RSidMapping.txt'
    df_rsid = pandas.read_csv(Path + rsid_file, sep='\t')
    #print(df_rsid)
    #Remove rows with missing rsids
    df_rsid = df_rsid[df_rsid.rsid != '.']

    #Get the rsid mapped to db153
    rsidmapped_file = 'IL6UnmappedSNPsMapped.txt'
    df_rsidmapped = pandas.read_csv(Path + rsidmapped_file, sep='\t')
    print(df_rsidmapped)
    df_output = pandas.concat([df_rsid,df_rsidmapped])
    df_output = df_output.sort_values(by=['Chr','Pos'])

    #Keep only rsid and -ve log10 p-values for Mergeomics Input
    df_output = df_output.drop(['Chr','Pos','P'], axis=1)
    print(df_output)

    df_output.to_csv(Path + "IL6_MergeIn.tsv", header=True, sep='\t', index=False, float_format='%g')