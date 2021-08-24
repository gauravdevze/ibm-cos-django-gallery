from django.shortcuts import render
import os
import ibm_boto3
from ibm_botocore.client import Config


cos = ibm_boto3.client(
    service_name='s3',
    #ibm_api_key_id='P3NumbDp2YClbtOhbolYnDmMUmHP-fpTcz10iBoYoK9K',
    #ibm_service_instance_id="crn:v1:bluemix:public:cloud-object-storage:global:a/ffbc32d94c3a4f16bcd2db52110a859a:21e49f99-4053-4adb-af7c-0073f8222c9a::",
    ibm_api_key_id=os.getenv("MY_COS_IBM_KEY_TEMP"),
    ibm_service_instance_id=os.getenv("MY_SVC_IBM_INST_ID_TEMP"),
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.us.cloud-object-storage.appdomain.cloud'
)


def index(request):
    data = cos.list_objects(Bucket='pixmedia')
    di = data['Contents']
    endpoint="https://s3.us.cloud-object-storage.appdomain.cloud/pixmedia/"
    #print(di)
    image_list=[]
    for key in di:
        print("Key is--->",key['Key'])
        res=key['Key']
        res=endpoint + res
        print("Res is ---->",res)
        image_list.append(res)
        #print("Image List is",image_list)

         
    
    #image_list=['https://s3.us.cloud-object-storage.appdomain.cloud/pixmedia/ob-1.png','https://s3.us.cloud-object-storage.appdomain.cloud/pixmedia/ob-2.png','https://s3.us.cloud-object-storage.appdomain.cloud/pixmedia/ob-3.png']
    print("Image List is",image_list)
    context = {
            'image_list': image_list
    }

    return render(request, "index.html", context)

