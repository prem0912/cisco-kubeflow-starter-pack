import json
import numpy as np
import os
import tensorflow as tf
import base64

from azureml.core.model import Model
from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType


# The init() method is called once, when the web service starts up.
#
# Typically you would deserialize the model file, as shown here using joblib,
# and store it in a global variable so your run() method can access it later.
def init():
    global model_path

    # The AZUREML_MODEL_DIR environment variable indicates
    # a directory containing the model file you registered.
    model_filename = 'blerssi'
    model_path = os.path.join(os.environ['AZUREML_MODEL_DIR'], model_filename)

# The run() method is called each time a request is made to the scoring API.
#
# Shown here are the optional input_schema and output_schema decorators
# from the inference-schema pip package. Using these decorators on your
# run() method parses and validates the incoming payload against
# the example input you provide here. This will also generate a Swagger
# API document for your web service.

@input_schema('data', StandardPythonParameterType([-200,-200,-80,-200,-77,-56,-81,-200,-200,-200,-200,-200,-200]))
@output_schema(NumpyParameterType(np.array([0])))
def run(data):
        data1 = data[0]
        test_sampl3 = json.dumps({"data": data1})
        test_sampl3 = bytes(test_sampl3, encoding='utf8')
        data1 = np.array(json.loads(test_sampl3)['data'], dtype=np.float32)
        X=data1
        global model_input1, model_input, predictor
        feature_col=["b3001", "b3002","b3003","b3004","b3005","b3006","b3007","b3008","b3009","b3010","b3011","b3012","b3013"]
        model_input1=tf.train.Example()
        for i in range(len(X)):
            print(X[i])
            print(type(X[i]))
            model_input1.features.feature[feature_col[i]].float_list.value.append(X[i])
        # Open a Session to predict
        with tf.Session() as sess:
         tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING], model_path)
         model_input =model_input1

         predictor= tf.contrib.predictor.from_saved_model(model_path,signature_def_key='predict')
         input_tensor=tf.get_default_graph().get_tensor_by_name("input_example_tensor:0")

         model_input=model_input.SerializeToString()
         output_dict= predictor({"examples":[model_input]})
        sess.close()

        response = output_dict.items()
        print(response)
        response1 = output_dict['class_ids']
        print(response1)
        a = np.array(response1[0]).tolist()
        b = json.dumps({"prediction": a})
        return(b)
