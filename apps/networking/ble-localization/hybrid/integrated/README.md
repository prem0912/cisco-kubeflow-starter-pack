# BLE-RSSI Integrated Hybrid Pipeline 

<!-- vscode-markdown-toc -->
* [Problem Definition](#ProblemDefinition)
* [Prerequisites](#Prerequisites)
* [Solution Schematic](#SolutionSchematic)
* [Cloud Setup](#CloudSetup)
* [UCS Setup](#UCSSetup)
	* [Pipeline Workflow](#PipelineWorkflow)
	* [Create Jupyter Notebook Server](#CreateJupyterNotebookServer)
	* [Upload Integrated Hybrid Pipeline notebook](#UploadIntegratedHybridPipelinenotebook)
	* [Run Pipeline](#RunPipeline)
	
<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='ProblemDefinition'></a>Problem Definition
The description of the BLE-RSSI based location prediction problem
can be found [here](../../README.md).

## <a name='Prerequisites'></a>Prerequisites

- [ ] UCS machine with Kubeflow 1.0 installed
- [ ] Based on the choice of your cloud:
  * AWS account with appropriate permissions
  * GCP account with appropriate permissions
  * Azure account with appropriate permissions 

## <a name='SolutionSchematic'></a>Solution Schematic

The overall solution uses [Kubeflow](https://www.kubeflow.org/) to run
the training on [Cisco UCS](https://www.cisco.com/c/en_in/products/servers-unified-computing/index.html) servers and the model is then served via [Amazon SageMaker](https://aws.amazon.com/sagemaker/) in case of AWS cloud, via [GCP AI Platform](https://cloud.google.com/ai-platform/prediction/docs) in case of GCP cloud & via [Azure ML](https://docs.microsoft.com/en-us/azure/machine-learning/) in case of Azure cloud.

## <a name='CloudSetup'></a>Cloud Setup

To complete the initial setup for selected cloud for deployment, Please refer [AWS Setup](../aws/pipelines#aws-setup), [GCP Setup](../gcp/pipelines#gcp-setup) or [Azure Setup](../azure/pipelines#azure-setup) based on your requirement.


## <a name='UCSSetup'></a>UCS Setup

To complete UCS setup, Please refer [UCS Setup](../gcp/pipelines#ucs-setup).

## <a name='PipelineWorkflow'></a>Pipeline Workflow
Once the setup is complete, the following are the steps in the pipeline
workflow.

### <a name='CreateJupyterNotebookServer'></a>Create Jupyter Notebook Server

Add configuration as shown below to attach aws-secrets and/or azure-secrets while creating new notebook server.

![BLERSSI Pipeline](./pictures/0_notebook_config.PNG)

Follow the [steps](./../notebook#create--connect-to-jupyter-notebook-server) to create & connect to Jupyter Notebook Server in Kubeflow    
### <a name='UploadIntegratedHybridPipelinenotebook'></a>Upload Integrated Hybrid Pipeline notebook

Upload [blerssi-integrated-hybrid.ipynb](blerssi-integrated-hybrid.ipynb) file to the created Notebook server.
    
### <a name='RunPipeline'></a>Run Pipeline

Open the [blerssi-integrated-hybrid.ipynb](blerssi-integrated-hybrid.ipynb) file and run pipeline.

Clone the Cisco Kubeflow Starter Pack repository

![BLERSSI Pipeline](./pictures/1_clone_repo.png)

Install common packages 

![BLERSSI Pipeline](./pictures/2_install_common_packages.png)

Install specific packages related to your choice of cloud

![BLERSSI Pipeline](./pictures/3_install_specific_packages.png)

Set Name of the cloud you wish to use for model deployment

![BLERSSI Pipeline](./pictures/4_set_cloud_name.png)

Import libraries 

![BLERSSI Pipeline](./pictures/5_import_libraries.png)

:information_source: 
### <a name='Buildinginferenceimage'></a>Building inference image if using aws cloud
  
   Run build & push script [here](../aws/pipelines/components/v1/mxnet-byom-inference/container/build_and_push.sh) using your *account credentials*.

Set timestamp

![BLERSSI Pipeline](./pictures/6_set_timestamp.png)

Set common parameters (common for GCP & AWS clouds)

![BLERSSI Pipeline](./pictures/7_set_common_parameters.png)

Set specific parameters for required cloud

![BLERSSI Pipeline](./pictures/8_set_specific_parameters.png)

Validate whether the required parameters are set

![BLERSSI Pipeline](./pictures/9_validate_parameter.png)

Load components 

![BLERSSI Pipeline](./pictures/10_load_components.png)

Define pipeline functions

![BLERSSI Pipeline](./pictures/11_define_pipeline_functions.png)

Run pipeline functions

![BLERSSI Pipeline](./pictures/12_1_run_pipeline.png)

Click on the Run link as shown below to view your pipeline that is executing

![BLERSSI Pipeline](./pictures/12_2_run_pipeline.png)

Wait until the pipeline execution is complete. (sample pipeline for aws cloud is shown)

![BLERSSI Pipeline](../aws/pipelines/pictures/notebook-sabe-7.PNG) 

Check service endpoint status deployed on the chosen cloud

![BLERSSI Pipeline](./pictures/13_check_endpoint_status.png)

Predict using service endpoint

![BLERSSI Pipeline](./pictures/14_predict_using_endpoint.png)

Clean up resources after prediction

![BLERSSI Pipeline](./pictures/15_clean_up_endpoint.png)




