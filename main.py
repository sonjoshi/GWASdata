# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas
import numpy

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.

def read_file(input_data):
    df = pandas.read_csv(input_data, sep='\t')
    print((df))
    df = df.set_index(['MARKER'])
    print(df.loc["rs11808675"])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Path = "/Users/sonali/UCLA/PathwayAnalysis/Mergeomics/InputData/"
    print_hi('PyCharm')
    input_data = "GWAS_IR_Input.txt"
    read_file(Path + input_data)


