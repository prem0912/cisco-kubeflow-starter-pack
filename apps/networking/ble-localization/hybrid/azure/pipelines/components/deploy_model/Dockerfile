FROM tensorflow/tensorflow:1.7.0-py3
RUN pip install azureml-core
ADD deploy_model.py  /opt/deploy_model.py
ADD blerssi_score.py /opt/blerssi_score.py
ADD blerssi_env.yml /opt/blerssi_env.yml
RUN chmod +x /opt/deploy_model.py  /opt/blerssi_score.py /opt/blerssi_env.yml
WORKDIR /opt/
ENTRYPOINT ["/usr/bin/python"]
CMD ["deploy_model.py"]
