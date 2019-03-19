import os


class Config(object):
    # Elasticsearch information. This is the cluster used to store address data.
    # Replace the URL, user and password information with these of your cluster.
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL','https://624eff0b7be7446a9c60f993d57b19ca.us-central1.gcp.cloud.es.io:9243')
    ELASTICSEARCH_USER = os.getenv('ELASTICSEARCH_USER','elastic')
    ELASTICSEARCH_PASSWORD = os.getenv('ELASTICSEARCH_PASSWORD', '5UbC2kOJiC8jy8ATejDMzpHK')

    ELASTICSEARCH_VALIDATE_CERTS = os.getenv('ELASTICSEARCH_VALIDATE_CERTS', 'true')
    ADDRESSES_PER_PAGE=int(os.getenv('ADDRESSES_PER_PAGE','25'))
    ADDRESS_INDEX = os.getenv('ADDRESS_INDEX','address')
    ELASTIC_APM = {
        # Elastic APM server information. This is where your agents will send APM data.
        # Replace the URL and token with these of your APM server.
        'SERVICE_NAME': os.getenv('ELASTIC_APM_SERVICE_NAME','address-finder'),
        'SERVER_URL': os.getenv('ELASTIC_APM_SERVER_URL','https://5fea15b641064bfa800ef7591069c865.apm.us-central1.gcp.cloud.es.io:443'),
        'SECRET_TOKEN': '92g2WYrFpnY0TappU7',
        'SERVICE_VERSION': os.getenv('ELASTIC_APM_SERVER_URL','1.0'),
        'COLLECT_LOCAL_VARIABLES': os.getenv('ELASTIC_APM_COLLECT_LOCAL_VARIABLES','all'),
        'SOURCE_LINES_ERROR_APP_FRAMES': os.getenv('ELASTIC_APM_SOURCE_LINES_ERROR_APP_FRAMES','10'),
        'SOURCE_LINES_ERROR_LIBRARY_FRAMES': os.getenv('ELASTIC_APM_SOURCE_LINES_ERROR_LIBRARY_FRAMES','10'),
        'SOURCE_LINES_SPAN_APP_FRAMES': os.getenv('ELASTIC_APM_SOURCE_LINES_SPAN_APP_FRAMES','5'),
        'SOURCE_LINES_SPAN_LIBRARY_FRAMES': os.getenv('ELASTIC_APM_SOURCE_LINES_SPAN_LIBRARY_FRAMES','5'),
        'CAPTURE_BODY': os.getenv('ELASTIC_APM_CAPTURE_BODY','all'),
        'SPAN_FRAMES_MIN_DURATION': os.getenv('ELASTIC_APM_SPAN_FRAMES_MIN_DURATION','-1'),
        'TRANSACTION_SAMPLE_RATE': os.getenv('ELASTIC_APM_TRANSACTION_SAMPLE_RATE','1.0'),
        'DEBUG': os.getenv('ELASTIC_APM_DEBUG', False)
    }
