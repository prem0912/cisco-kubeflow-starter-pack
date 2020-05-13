# BLERSSI Hybrid Pipeline using Cisco UCS 🤝 Amazon SageMaker

<!-- vscode-markdown-toc -->
1. [Pre-requisites](#Pre-requisites)
2. [AWS Setup](#AWSSetup)
  * 2.1. [Create S3 Bucket](#CreateS3Bucket)
	* 2.2. [Setup SageMaker permissions](#SetupSageMakerpermissions)
3. [UCS Setup](#UCSSetup)
	* 3.1. [Retrieve Ingress IP](#RetrieveIngressIP)
	* 3.2. [Create Jupyter Notebook Server](#CreateJupyterNotebookServer)
	* 3.3. [Upload Hybrid Pipeline notebook](#UploadHybridPipelinenotebook)
	* 3.4. [Run Pipeline](#RunPipeline)
	* 3.5. [Note - Building inference image](#Note-Buildinginferenceimage)
	* 3.6. [Run Prediction API](#RunPredictionAPI)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='Pre-requisites'></a>Pre-requisites

- [ ] UCS machine with Kubeflow 1.0 installed
- [ ] AWS account with appropriate permissions

##  2. <a name='AWSSetup'></a>AWS Setup
###  2.1. <a name='CreateS3Bucket'></a>Create S3 Bucket

Ensure you have the AWS CLI installed. 
Otherwise, you can use the docker image with the alias set.

    alias aws='docker run --rm -it -v ~/.aws:/root/.aws -v $(pwd):/aws amazon/aws-cli'
    aws s3 mb s3://mxnet-model-store --region us-west-2

###  2.2. <a name='SetupSageMakerpermissions'></a>Setup SageMaker permissions

In order to run this pipeline, we need to prepare an IAM Role to run Sagemaker jobs. You need this `role_arn` to run a pipeline. Check [here](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) for details.

This pipeline also use aws-secret to get access to Sagemaker services, please also make sure you have a `aws-secret` in the kubeflow namespace.

    echo -n $AWS_ACCESS_KEY_ID | base64
    echo -n $AWS_SECRET_ACCESS_KEY | base64

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: aws-secret
  namespace: kubeflow
type: Opaque
data:
  AWS_ACCESS_KEY_ID: YOUR_BASE64_ACCESS_KEY
  AWS_SECRET_ACCESS_KEY: YOUR_BASE64_SECRET_ACCESS
```

##  3. <a name='UCSSetup'></a>UCS Setup

To install Kubeflow, follow the instructions [here](../../../../../install)

###  3.1. <a name='RetrieveIngressIP'></a>Retrieve Ingress IP

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

###  3.2. <a name='CreateJupyterNotebookServer'></a>Create Jupyter Notebook Server

Follow the [steps](./../notebook#create--connect-to-jupyter-notebook-server) to create & connect to Jupyter Notebook Server in Kubeflow    
    
###  3.3. <a name='UploadHybridPipelinenotebook'></a>Upload Hybrid Pipeline notebook

Upload [blerssi-aws.ipynb](blerssi-aws.ipynb) file to the created Notebook server.
    
###  3.4. <a name='RunPipeline'></a>Run Pipeline

Open the [blerssi-aws.ipynb](blerssi-aws.ipynb) file and run pipeline

Set the input parameters for the pipeline in the first cell of the notebook.

![BLERSSI Pipeline](./pictures/notebook-sabe-1.PNG)

Import libraries and set model/deploy component yaml path variables.

![BLERSSI Pipeline](./pictures/notebook-sabe-2.PNG)

Define BLERSSI mxnet pipeline function

![BLERSSI Pipeline](./pictures/notebook-sabe-3.PNG)

Create experiment with name "BLERSSI-Sagemaker"

![BLERSSI Pipeline](./pictures/notebook-sabe-4.PNG)

###  3.5. <a name='Note-Buildinginferenceimage'></a>Note - Building inference image
   Run build & push script [here](./components/v1/mxnet-byom-inference/container/build_and_push.sh) using your *account credentials*.

Set AWS region, and inference image to the built ECR image

![BLERSSI Pipeline](./pictures/notebook-sabe-5.PNG)

Create BLERSSI run and open run link

![BLERSSI Pipeline](./pictures/notebook-sabe-6.PNG)


The BLERSSI Sagemaker pipeline starts executing. 
Once all the components executed successfully, check the logs of sagemaker-deploy component to verify endpoint is created.

![BLERSSI Pipeline](./pictures/notebook-sabe-7.PNG)

To verify endpoint in AWS, open AWS sagemaker and check endpoints created successfully as snapshot given below

![BLERSSI Pipeline](./pictures/aws-sagemaker-endpoint.PNG)

###  3.6. <a name='RunPredictionAPI'></a>Run Prediction API

To predict the output go back to jupyter notebook and start executing other cells

Provide AWS credentials

![BLERSSI Pipeline](./pictures/notebook-sabe-8.PNG)

Predicted result will be displayed

![BLERSSI Pipeline](./pictures/notebook-sabe-9.PNG)
