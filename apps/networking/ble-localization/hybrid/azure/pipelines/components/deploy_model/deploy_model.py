from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import argparse
import json
import sys
import tensorflow as tf
import pandas as pd
import numpy as np
import shutil
import os
from sklearn.preprocessing import OneHotEncoder
from zipfile import ZipFile

from azureml.core.webservice import AciWebservice
from azureml.core.webservice import Webservice
from azureml.core.image import ContainerImage
from azureml.core.model import Model
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace


def parse_arguments():
  parser = argparse.ArgumentParser()

  
  parser.add_argument('--workspacename',
                      type=str,
                      help='Workspace name.')
  parser.add_argument('--subscriptionid',
                      type=str,
                      help='subscription id.')
  parser.add_argument('--resourcegroup',
                      type=str,
                      help='resource group name')

  parser.add_argument('--modelname',
                      type=str,
                      help='registered model name')
  parser.add_argument('--servicename',
                      type=str,
                      help='Inference service name')
  parser.add_argument('--tenantid',
                      type=str,
                      help='Azure tenant ID')
  parser.add_argument('--serviceprincipalid',
                      type=str,
                      help='Azure Service Principal ID')
  parser.add_argument('--serviceprincipalpassword',
                      type=str,
                      help='Azure Service Principal Password')


  args = parser.parse_args()
  return args



def main(unused_args):

    args = parse_arguments()

    svc_pr = ServicePrincipalAuthentication(
        tenant_id=args.tenantid,
        service_principal_id=args.serviceprincipalid,
        service_principal_password=args.serviceprincipalpassword)


    ws = Workspace(
        subscription_id=args.subscriptionid,
        resource_group=args.resourcegroup,
        workspace_name=args.workspacename,
        auth=svc_pr
        )

    print("Found workspace {} at location {}".format(ws.name, ws.location))


    args = parse_arguments()

    ws = Workspace.get(name=args.workspacename, subscription_id=args.subscriptionid, resource_group=args.resourcegroup, auth=svc_pr)


    model = Model(ws, args.modelname)


    imgconfig = ContainerImage.image_configuration(execution_script="blerssi_score.py",
                                               runtime="python",
                                               conda_file="blerssi_env.yml")

    aciconfig = AciWebservice.deploy_configuration(cpu_cores=0.5, memory_gb=0.5)

    service = Webservice.deploy_from_model(workspace=ws,
                                       name=args.servicename,
                                       deployment_config=aciconfig,
                                       models=[model],
                                       image_config=imgconfig)

    service.wait_for_deployment(show_output=True)

    service.get_logs()

    print(service.state)

    print("scoring URI: " + service.scoring_uri)


if __name__ == "__main__":
    tf.app.run()
