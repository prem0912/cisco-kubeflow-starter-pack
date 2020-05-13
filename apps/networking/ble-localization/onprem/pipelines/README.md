# BLE-RSSI Location Prediction using Kubeflow Pipelines

<!-- vscode-markdown-toc -->
* [What we're going to build](#Whatweregoingtobuild)
* [Infrastructure Used](#InfrastructureUsed)
* [Setup](#Setup)
	* [Install NFS server (if not installed)](#InstallNFSserverifnotinstalled)
		* [Retrieve Ingress IP](#RetrieveIngressIP)
		* [Installing NFS server, PVs and PVCs.](#InstallingNFSserverPVsandPVCs.)
	* [Create Jupyter Notebook Server](#CreateJupyterNotebookServer)
	* [Upload Notebook file](#UploadNotebookfile)
	* [Run BLERSSI Pipeline](#RunBLERSSIPipeline)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Whatweregoingtobuild'></a>What we're going to build

To train, serve and prodict  model  using kubeflow pipeline through jupyter-notebook.

![TF-BLERSSI Pipeline](pictures/0-blerssi-graph.png)

## <a name='InfrastructureUsed'></a>Infrastructure Used

* Cisco UCS - C240

## <a name='Setup'></a>Setup

### <a name='InstallNFSserverifnotinstalled'></a>Install NFS server (if not installed)

To install NFS server follow steps below.

#### <a name='RetrieveIngressIP'></a>Retrieve Ingress IP

For installation, we need to know the external IP of the 'istio-ingressgateway' service. This can be retrieved by the following steps.  

```
kubectl get service -n istio-system istio-ingressgateway
```

If your service is of LoadBalancer Type, use the 'EXTERNAL-IP' of this service.  

Or else, if your service is of NodePort Type - run the following command:  

```
kubectl get nodes -o wide
```

Use either of 'EXTERNAL-IP' or 'INTERNAL-IP' of any of the nodes based on which IP is accessible in your network.  

This IP will be referred to as INGRESS_IP from here on.

#### <a name='InstallingNFSserverPVsandPVCs.'></a>Installing NFS server, PVs and PVCs.

Follow the [steps](./../install/) to install NFS server, PVs and PVCs.

### <a name='CreateJupyterNotebookServer'></a>Create Jupyter Notebook Server

Follow the [steps](./../notebook#create--connect-to-jupyter-notebook-server) to create & connect to Jupyter Notebook Server in Kubeflow

### <a name='UploadNotebookfile'></a>Upload Notebook file

Upload [BLERSSI-Pipeline-Deployment.ipynb](BLERSSI-Pipeline-Deployment.ipynb)

### <a name='RunBLERSSIPipeline'></a>Run BLERSSI Pipeline

Open the BLERSSI-Pipeline-Deployment.ipynb file and run pipeline

Clone git repo

![TF-BLERSSI Pipeline](pictures/1-git-clone.PNG)

Loading Components

![TF-BLERSSI Pipeline](pictures/2-load-compoents.PNG)


Run Pipeline

![TF-BLERSSI Pipeline](pictures/2-run-pipeline.PNG)


Once BLERSSI Pipeline is executed, Experiment and Run link will be generated and displayed as output

![TF-BLERSSI Pipeline](pictures/3-exp-link.PNG)


Click on latest experiment which is created 

![TF-BLERSSI Pipeline](pictures/4-pipeline-created.PNG)


Pipeline components execution can be viewed as below

![TF-BLERSSI Pipeline](pictures/6-pipeline-completed.PNG)


Logs of BLERSSI Training Component

![TF-BLERSSI Pipeline](pictures/2-training.PNG)


Logs of Serving Component

![TF-BLERSSI Pipeline](pictures/3-serving.PNG)


Logs of WebUI Component

![TF-BLERSSI Pipeline](pictures/4-webui.PNG)


Logs of Tensorboard Component

![TF-BLERSSI Pipeline](pictures/5-tensorboard-log.PNG)

For obtaining the URLs for Tensorboard Graph and WebUI for BLERSSI as shown below, change the INGRESS_IP in the last two cells with your ingress IP.

Tensorboard Graph for BLERSSI

![TF-BLERSSI Pipeline](pictures/5-tensorboard-graph.PNG)


Tensorboard Scalar for BLERSSI

![TF-BLERSSI Pipeline](pictures/5-tensorboard-scalar.PNG)


Predict BLERSSI Location using Web UI - upload data file located at [location](./../data/iBeacon_RSSI_Unlabeled_truncated.csv)

![TF-BLERSSI Pipeline](pictures/7-upload-file-1.png)


BLERSSI Prediction Location with Probability

![TF-BLERSSI Pipeline](pictures/8-show-table.PNG)
