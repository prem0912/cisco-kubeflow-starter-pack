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
from azureml.core.model import Model
import os, uuid
import re
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace

def parse_arguments():
  parser = argparse.ArgumentParser()

  parser.add_argument('--workspacename',
                      type=str,
                      help='Name of the Azure Workspace')
  parser.add_argument('--subscriptionid',
                      type=str,
                      help='Name of the Azure Subscription ID.')
  parser.add_argument('--resourcegroup',
                      type=str,
                      help='Name of the Azure Resource Group.')
    
  parser.add_argument('--modelname',
                      type=str,
                      help='registered model name')
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

    ws = Workspace.get(name=args.workspacename, subscription_id=args.subscriptionid, resource_group=args.resourcegroup, auth=svc_pr)
    print(ws)
    model_path = "/mnt/Model_Blerssi/"
    sample = []
    for file in  os.listdir(model_path):
        sample.append(file)
    sample

    def extract_number(f):
        s = re.findall("\d+$",f)
        return (int(s[0]) if s else -1,f)

    numberfolder = max(sample,key=extract_number)
    target_path = os.path.join(model_path, numberfolder)
    absolute_path = target_path + "/blerssi"
    if not os.path.exists(absolute_path):
        os.mkdir(absolute_path)
        src1 = target_path + '/saved_model.pb'
        src2 = target_path + '/variables'
        var_path = absolute_path + '/variables'
        if not os.path.exists(var_path):
            os.mkdir(var_path)
            shutil.copy(src1, absolute_path)
            for file in os.listdir(src2):
                subsrc = os.path.join(src2,file)
                shutil.copy(subsrc, var_path)
   
    model = Model.register(model_path = absolute_path,
                       model_name = args.modelname,
                       description = "BLE-Localisation analysis",
                       workspace = ws)


if __name__ == "__main__":
    tf.app.run()
