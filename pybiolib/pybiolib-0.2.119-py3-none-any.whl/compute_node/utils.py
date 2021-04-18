from enum import Enum
import logging
import random
import string

biolib_logger = logging.getLogger('biolib')


def get_package_type(package):
    package_type = int.from_bytes(package[1:2], 'big')
    if package_type == 1:
        return 'ModuleInput'
    elif package_type == 2:
        return 'ModuleOutput'
    elif package_type == 3:  # Not used in the compute node
        return 'ModuleSource'
    elif package_type == 4:
        return 'AttestationDocument'
    elif package_type == 5:
        return 'SavedJob'
    elif package_type == 6:
        return 'RsaEncryptedAesPackage'
    elif package_type == 7:
        return 'AesEncryptedPackage'
    elif package_type == 8:
        return 'SystemStatusUpdate'
    elif package_type == 9:
        return 'SystemException'

    else:
        raise Exception(f"Unexpected package type {package_type}")


class SystemExceptionCodes(Enum):
    FAILED_TO_INIT_COMPUTE_PROCESS_VARIABLES = 1
    FAILED_TO_CONNECT_TO_WORKER_THREAD_SOCKET = 2
    FAILED_TO_START_SENDER_THREAD_OR_RECEIVER_THREAD = 3
    FAILED_TO_GET_ATTESTATION_DOCUMENT = 4
    FAILED_TO_CREATE_DOCKER_NETWORKS = 5
    FAILED_TO_START_REMOTE_HOST_PROXIES = 6
    FAILED_TO_REDIRECT_ENCLAVE_TRAFFIC_TO_PROXIES = 7
    FAILED_TO_CREATE_PROXY_CONTAINER = 8
    FAILED_TO_CONFIGURE_ALLOWED_REMOTE_HOST = 9
    FAILED_TO_SEND_STATUS_UPDATE = 10
    FAILED_TO_GET_REQUIRED_DATA_FOR_COMPUTE = 11
    FAILED_TO_START_RUNTIME_ZIP_DOWNLOAD_THREAD = 12
    FAILED_TO_DOWNLOAD_RUNTIME_ZIP = 13
    FAILED_TO_CONTACT_BACKEND_TO_CREATE_JOB = 14
    FAILED_TO_CREATE_NEW_JOB = 15
    FAILED_TO_START_IMAGE_PULLING_THREAD = 16
    FAILED_TO_PULL_DOCKER_IMAGE = 17
    FAILED_TO_START_COMPUTE_CONTAINER = 18
    FAILED_TO_COPY_INPUT_FILES_TO_COMPUTE_CONTAINER = 19
    FAILED_TO_COPY_RUNTIME_FILES_TO_COMPUTE_CONTAINER = 20
    FAILED_TO_RUN_COMPUTE_CONTAINER = 21
    FAILED_TO_RETRIEVE_AND_MAP_OUTPUT_FILES = 22
    FAILED_TO_SERIALIZE_AND_SEND_MODULE_OUTPUT = 23
    FAILED_TO_DESERIALIZE_SAVED_JOB = 24
    UNKOWN_COMPUTE_PROCESS_ERROR = 25
    FAILED_TO_INITIALIZE_WORKER_THREAD = 26
    FAILED_TO_HANDLE_PACKAGE_IN_WORKER_THREAD = 27


class WorkerThreadException(Exception):
    def __init__(self, original_error, error_code, worker_thread):
        super().__init__()
        worker_thread.compute_state['status']['error_code'] = error_code
        biolib_logger.error(original_error)
        worker_thread.terminate()


enclave_remote_hosts = ['biolib-cloud-api.s3.amazonaws.com',
                        'prod-eu-west-1-starport-layer-bucket.s3.eu-west-1.amazonaws.com',
                        'biolib.com',
                        'containers.biolib.com',
                        'staging-elb.biolib.com',
                        'containers.staging.biolib.com']


def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))
