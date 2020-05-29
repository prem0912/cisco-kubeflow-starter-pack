FROM tensorflow/tensorflow:1.7.0-py3
RUN pip install azureml-core
ADD register_model.py  /opt/register_model.py
ENTRYPOINT ["/usr/bin/python"]
CMD ["/opt/register_model.py"]
