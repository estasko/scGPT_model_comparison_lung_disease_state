# Application of scGPT to identify cell types in lung disease states
## Introduction

Cell clustering is commonly used for cell type identification. This algorithm reduces the dimensionality of the scRNA-seq data and can be visualized as UMAP maps dividing cells based on type. Traditional methods include algorithms such as Seurat. This is widely accepted however can be less effective in identifying complex relationships between genes and thus identifying aberrant cell populations. This severely limits the application of cell clustering for studying disease state models. 

To combat this, a new machine learning model, scGPT, has been developed by the Bowang Lab. Harnessing transfer learning concepts, scGPT uses scRNA-seq data for cell type identification and allows for more accurate identification of complex gene expression relationships. By creating a more sensitive model, the Bowang Lab has increased the potential applications of clustering. Using this model to identify aberrant cell types in disease states based on their gene expression can help researches determine pathogenesis of idiopathic diseases. 

Here, we compare the scGPT whole human model (pre-trained on 33 million cells) and lung model (pre-trained on 2.1 million cells). We aim to determine whether a generalized model or task specific model best identifies aberrant cell populations in IPF, COPD and control lung cell samples.

We would further like to determine how specific cell identifiers impact the performance of the model. The data used can be downloaded from the ipfcellatlas.com (Kaminski/Rosas) and was configured into train and test files  using different cell classification and subclassification provided in the meta data to test the limits of each model. Further, we use these models to determine the disease state of each cell based on its gene expression. These files used in analysis were created using mxt_h5ad_file_conversion.py. 

## Methods
*This script was derived from scGPT zero-shot reference mapping tutorial. Single Cell RNA sequencing data is analyzed from Kaminski et al. "Single-cell RNA-seq reveals ectopic and aberrant lung-resident cell populations in idiopathic pulmonary fibrosis".*


*The zero-shot reference mapping workflow is as follows:*

 1. *Load and pre-process the dataset*
    
 2. *Generate scGPT embeddings for each cell in reference and query datasets*

 3. *Transfer the annotations from reference to query dataset*


## Results

Both the whole human and lung scGPT models were successful in identifying cell types. The most successful data set for both models was annotated with cell type. These annotations were less specific then the cell type subclass identity used and thus less relevant to the intended purpose of identifying abberant cell types. 

Shown below are the UMAP clusters of the whole human and lung model for the cell type annotation and evaluation shows a similar distribution of cell types / clustering. 
The confusion matrix again shows similar success for all cell types excluding multiplet where the whole human model slightly outperformed the lung model.


| scGPT whole human model | scGPT lung model |
|-------------------------|-------------------------|
| UMap| |
|![human_umap_cell_name](https://github.com/user-attachments/assets/e99714d0-3317-4b80-8657-0768af2870e0) |![lung_umap_cell_name](https://github.com/user-attachments/assets/123163bc-d3df-4328-8a7e-5e0e5f1f6635)|
| Confusion Matrix | |
|![confustion_matrix_lung_human_cell_name](https://github.com/user-attachments/assets/01844d15-9afa-4c1b-bec1-d2cd7779e7cc)|![confusion_lung_cell_name](https://github.com/user-attachments/assets/3328dcb2-75f6-4d3d-b0a1-32db75d0335f)|

When the annotations were further specified to focus on cell type subclass, the possible classifications increased from 6 to 49. This makes interpretation of the cluster map difficult. As seen below the coloring is grey scale and time constraints did not allow for trouble shooting. However important information can be ascertained from the confusion matrices. Namely, again the whole human model did a better job overall identifying cell types this is concisely seen by the accuracy, precision, recall and macro f1 score of each model. The matrix shows further details explaining which cell types were identified with greater accuracy. This may be for a variety of reasons including the proportion of cells of each type the model was trained on.


| Metric | scGPT whole human model | scGPT lung model|
|-------------------------|-------------------------|-------------------------|
|accuracy| 0.7433132010353753 | ?|
|precision| 0.7306583316543472 | ?|
|recall | 0.7250614699713483| ?|
|macro f1| 0.7263983803368087 |?| 


|scGPT whole human model | scGPT lung model|
|-------------------------|-------------------------|
|UMap|
|![human_umap_subclass](https://github.com/user-attachments/assets/fb0d7132-9de6-4349-86ca-e93714e2c10f) |![lung_umap_subclass](https://github.com/user-attachments/assets/cc955483-bb9d-4b5d-bf12-7a0ea2a25a0f)|
| Confusion Matrix|
| ![confusion_matrix_human_cell_subclass](https://github.com/user-attachments/assets/29914af9-16ad-413d-aa80-c4d0be7dce3e)|![confusion_matrix_lung_cell_subclass](https://github.com/user-attachments/assets/e85cc104-417f-41a1-bbfe-bd8a45fe30b4)|



When the training data sent to the models was instead annotated with the cells' disease state (IPF, COPD or control), the human model again outperformed the lung model. The UMAP plots created do not give much information, the model still seems to cluster the cells by cell type, not disease state. However bands of similar disease state can be seen in the plots suggesting an up regulation of certain cell types in each disease state. Importantly, this again depends on the data presented to the model. It is unclear whether the data collected for the original study equally harvested cells between disease states from similar areas of the lungs. If this is not the case, the information from the UMAP plots might be misleading. 

The confusion matrices for this test explicitly show the whole human model outperforming the lung model. This is also seen by the explicit accuracy, precision, recall and macro f1 scores of the models.


| Metric | scGPT whole human model | scGPT lung model|
|-------------------------|-------------------------|-------------------------|
|accuracy| 0.0.7433132010353753 | 0.7127792157990605|
|precision| 0.0.7306583316543472 | 0.6988279191653136|
|recall | 0.0.7250614699713483| 0.692754924917788|
|macro f1| 0.0.7263983803368087 |0.6941320833645248| 


|scGPT whole human model | scGPT lung model|
|-------------------------|-------------------------|
|UMap|
|![cluster_human_disease_id](https://github.com/user-attachments/assets/9f853b65-5f52-4e63-b124-dbfca5461d36)| ![cluster_lung_disease_id](https://github.com/user-attachments/assets/2d5a246c-248f-45c8-90ba-cede1412b844)|
|![confusion_matrix_human_disease_id](https://github.com/user-attachments/assets/17f34970-e649-4aa1-a4fd-f1795305d2ea)| ![confusion_matrix_lung_disease_id](https://github.com/user-attachments/assets/497db3e1-9c04-43ba-9502-6edc67caa7d9)|



These data can further be analyzed to compare the model outputs for each annotation choice to see how this impacted the clustering and accuracy metrics of the model.![image]

| scGPT whole human model | | |
|-------------------------|-------------------------|-------------------------|
| Cell Name | Cell Subclassification | Disease Identity |
|![human_umap_cell_name](https://github.com/user-attachments/assets/60650adc-4e34-46a4-a7b2-002eb2d76a22)|![human_umap_subclass](https://github.com/user-attachments/assets/67ff9255-dc70-4042-a22b-7528ea00f63b)|![cluster_human_disease_id](https://github.com/user-attachments/assets/f534f82d-4ebf-4495-ad6f-f41a2c7e6394)|

Interestingly, while the cell UMAP and confusion matrices differ the metrics for each data annotation are identical.


| scGPT whole human model | | ||
|-------------------------|-------------------------|-------------------------|-------------------------|
| Metric | Cell Name | Cell Subclassification | Disease Identity |
|accuracy| ?| 0.7433132010353753 |0.7433132010353753|
|precision| ?| 0.7306583316543472 |0.0.0.7306583316543472|
|recall | ?| 0.7250614699713483| 0.0.7250614699713483|
|macro f1|?|  0.7263983803368087| 0.0.7263983803368087|




Acknowledgments:

The Bowang lab: scGPT https://pubmed.ncbi.nlm.nih.gov/38409223/
Single-cell RNA-seq reveals ectopic and aberrant lung-resident cell populations in idiopathic pulmonary fibrosis: https://www.lungmap.net/omics/?experiment_id=LMEX0000004393
