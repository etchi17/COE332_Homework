FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install pytest==7.0.0

COPY ml_data_analysis.py /code/ml_data_analysis.py
COPY test_ml_data_analysis.py /code/test_ml_data_analysis.py

RUN chmod +rx /code/ml_data_analysis.py
RUN chmod +rx /code/test_ml_data_analysis.py

ENV PATH "/code:$PATH"
