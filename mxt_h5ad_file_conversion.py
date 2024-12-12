#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:56:42 2024

This script creates train and test h5ad files from data published in  
"Single-cell RNA-seq reveals ectopic and aberrant lung-resident cell populations in idiopathic pulmonary fibrosis"

These data can be downloaded from the IPF Cell Atlas  

@author: Ella Stasko
"""
 #%% Import packages 
 
import anndata
import scipy.io as sio 
from psutil import virtual_memory
import pandas as pd
import scanpy as sc

#%% Read matrix file - using absolute path for file  adjust as necessary 

mtx_file = "/Users/ellastasko/OneDrive - University of Vermont/Senior_Year_Classes/Fall_2024/deep_learning/final_project/GSE136831_RawCounts_Sparse.mtx.gz"

matrix = sio.mmread(mtx_file).tocsr()

#%% Read metadata - Using absolute path for file - adjust as necessary 

genes = pd.read_csv("/Users/ellastasko/Library/CloudStorage/OneDrive-UniversityofVermont/Senior_Year_Classes/Fall_2024/deep_learning/final_project/GSE136831_AllCells.GeneIDs.txt", sep='\t', dtype=str)
genes = genes.reindex(columns = ['HGNC_EnsemblAlt_GeneID'])
genes = genes['HGNC_EnsemblAlt_GeneID']


barcodes = pd.read_csv("/Users/ellastasko/Library/CloudStorage/OneDrive-UniversityofVermont/Senior_Year_Classes/Fall_2024/deep_learning/final_project/GSE136831_AllCells.cellBarcodes.txt.gz",sep='\t', header=None, dtype=str)
barcodes = barcodes[0]

meta_data = pd.read_csv("/Users/ellastasko/Library/CloudStorage/OneDrive-UniversityofVermont/Senior_Year_Classes/Fall_2024/deep_learning/final_project/GSE136831_AllCells.Samples.CellType.MetadataTable.txt", sep='\t', dtype=str)
cell_type_category = meta_data["CellType_Category"]

Subclass_Cell_Identity = meta_data["Subclass_Cell_Identity"]
Disease_Identity = meta_data["Disease_Identity"]


#%% Convert meta data into data frame objects 

# vars
genes_df = pd.DataFrame(index=genes)  
genes_df.index.name = 'gene_id'  

# obs
barcodes_df = pd.DataFrame(index=barcodes) 
barcodes_df.index.name = 'cell_barcode' 

cell_type_category_df = pd.DataFrame(index=meta_data)  
cell_type_category_df.index.name = 'cell_name'  

subclass_cell_id_df = pd.DataFrame(index=Subclass_Cell_Identity)
subclass_cell_id_df.index.name = 'Subclass_Cell_Identity'  

Disease_Identity_df = pd.DataFrame(index=Disease_Identity)
Disease_Identity_df.index.name = 'Disease_Identity'  
#%% Create the AnnData object, ensuring the matrix has (n_cells, n_genes)

# Replace obs = "x" with desired metadata 
adata = anndata.AnnData(X=matrix.T, obs=Disease_Identity_df, var=genes_df)

#%% Create file with all data - adjust naming convention as necessary

adata.write_h5ad("RawCounts_Sparse_Disease_Identity.h5ad")

#%%Split into test and train

from sklearn.model_selection import train_test_split
test_size = 0.2
train_adata, test_adata = train_test_split(adata, test_size=test_size, random_state=42)

#%% Create the training data file - adjust naming convention as necessary

train_adata.write_h5ad("RawCounts_Sparse_Disease_Identity_train.h5ad")

#%% Create the testing data file - adjust naming convention as necessary

test_adata.write_h5ad("RawCounts_Sparse_Disease_Identity_test.h5ad")



