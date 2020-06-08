#Python Script for setting parameters for BLERSSI integrated hybrid pipeline execution

from datetime import datetime

#Class for holding timestamps
#GCP accepts only underscores rather than hyphens
#AWS & Azure accept only hyphens rather than underscores
class Timestamp:

        #Set timestamp
        gcp_timestamp = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
        timestamp = datetime.now().strftime("%d-%m-%y-%H-%M-%S")

#Class defined for holding AWS parameters
class Aws_params:
    
        # execution_mode (string): where the notebook is being run
        # Sample: 'local', 'in-cluster'
        execution_mode = 'in-cluster'

        # host (string): KF Pipelines service endpoint
        # Sample:  "http://10.10.10.10:31380/pipeline"
        host = ''

        
        #bucket_name (string): S3 bucket to be used by the pipeline
        #Ensure bucket is created/exists
        #Sample: "mxnet-model-store"
        bucket_name = '<<bucket-name>>'
        
        
        #secret_name (string): AWS secret where IAM creds are stored
        #Sample: 'aws-secret'
        secret_name='aws-secret'

                     
        #AWS cloud: AWS instance type, Sample: 'ml.m4.xlarge'
        instance_type = 'ml.m4.xlarge'
        
        #Region where the pipeline is supposed to push/pull artifacts 
        #For aws cloud: sample: 'us-west-2'
        aws_cloud_region = 'us-west-2'
        #%env AWS_DEFAULT_REGION={aws_cloud_region}


        # role_arn (string): SageMaker Role ARN for execution of pipeline components
        # Sample: 'arn:aws:iam::${account_id}:role/service-role/AmazonSageMaker-ExecutionRole-${timestamp}'
        role_arn = '<<role-arn>>'


        # pre-built inference image for serving the mxnet BLERSSI model
        inference_image = '245980173641.dkr.ecr.us-west-2.amazonaws.com/mxnet-blerssi-inference:latest'

        # endpoint config name for the SageMaker Model Serving Endpoint Config
        endpoint_config_name = 'aws-blerssi-endpoint-config-'+Timestamp.timestamp

        # endpoint name for SageMaker Serving Endpoint
        endpoint_name = 'aws-blerssi-endpoint-'+Timestamp.timestamp

        #model name to create a re-usable SageMaker Model resource
        model_name = 'aws-blerssi-model-'+Timestamp.timestamp

        # model artifact URL
        # Path to the model tarball 
        model_path = 's3://'+bucket_name+'/blerssi/model.tar.gz'

#Class defined for holding GCP parameters
class Gcp_params:
    
        # execution_mode (string): where the notebook is being run
        # Sample: 'local', 'in-cluster'
        execution_mode = 'in-cluster'

        # host (string): KF Pipelines service endpoint
        # Sample:  "http://10.10.10.10:31380/pipeline"
        host = ''

        
        #bucket_name (string): GCP bucket to be used by the pipeline
        #Sample: "blerssi-model-store"
        bucket_name = '<<bucket-name>>'
        
        
        #secret_name (string): GCP secret where IAM creds are stored
        #Sample: 'user-gcp-sa'
        secret_name='user-gcp-sa'

                     
        #GCP cloud: GCP instance type, Sample: 'mls1-c1-m2'
        instance_type = 'mls1-c1-m2'
        
        #Specify path of .json file if file is not in the same folder as this notebook 
        google_application_credentials='auth.json'
        

        #Specific region to be used 
        #Sample: 'us-central1'
        gcp_cloud_region = 'us-central1'

        #model name to create a re-usable AL Platform Model resource
        model_name = 'blerssi_model_'+Timestamp.gcp_timestamp

        version_name = "blerssi_model_ver"+Timestamp.gcp_timestamp

        # model artifact URL
        # Path to the model
        model_path = 'gs://'+bucket_name+'/blerssi/'+Timestamp.gcp_timestamp


        #GCP Project Id
        project_id='<<project-id>>'

#Class defined for holding Azure parameters        
class  Azure_params:
    
       azure_model = "azuremodel"+Timestamp.timestamp
       azure_service = "azureservice"+Timestamp.timestamp    
