from ..services import min_io as init_minio
import shutil

from ..services.min_io import client


def add_new_data_to_minio(bucket_name, new_filename, file):
    if not init_minio.client.bucket_exists(bucket_name):
        init_minio.client.make_bucket(bucket_name)

    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    init_minio.client.fput_object(bucket_name, new_filename, file.filename)

def print_objcts(bucket_name):
    objects = init_minio.client.list_objects(bucket_name)
    for object in objects:
        print(object.object_name)

print_objcts('20220628')

def delete_data_by_code_request(code):
    bucket_name = code[:8]
    objects = client.list_objects(bucket_name)

    for obj in objects:
        if code in obj.object_name:
            client.remove_object(bucket_name, obj.object_name)
