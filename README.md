# scGPT_model_comparison_lung_disease_state
## Introduction

Cell clustering is commonly used for cell type identificaion. This algoritm reduces the dimensionality of the scRNA-seq data and can be visualized as culster maps dividing cells based on type. Traditional methods include algorithms such as seruat. This is widelt accepted however can be less effective in identifying complex relationships between genes and thus identifying aberant cell populations. This severly limits the application of cell culstering for studying disease state models. 

To combat this, a new machine learning model, scGPT, has been developed by the Bowang Lab. Harnesing transfer learning concepts, scGPT uses scRNA-seq data for cell type identification and allows for more accurate identification of complex gene expression relationships. By creating a more sensitive model, the Bowang Lab has increased the potential applications of clustering. Using this model to identify abberant cell types in disease states based on their gene expression can help researches determine pathogenesis of idopathic diseases. 

Here, we compare the scGPT whole human model (pre-trained on 33 million cells) and lung model (pre-trained on 2.1 million cells). We aim to determine whether a generalized model or task specific model best identifies aberrant cell populations in IPF, COPD and control lung cell samples.

We would further like to determine how specific cell identifiers impact the performance of the model. The data file provided includes train and test file of the same dataset using different levels of cell classification and subclassification to test the limits of each model. Further, we use these models to determine the disease state of each cell based on its gene expression.



*This script was derived from scGPT zero-shot reference mapping tutorial. Single Cell RNA sequencing data is analyzed from Kaminski et al. "Single-cell RNA-seq reveals ectopic and aberrant lung-resident cell populations in idiopathic pulmonary fibrosis".*


*The zero-shot reference mapping workflow is as follows:*

 1. *Load and pre-process the dataset*
    
 2. *Generate scGPT embeddings for each cell in reference and query datasets*

 3. *Transfer the annotations from reference to query dataset*
