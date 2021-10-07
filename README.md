# ibm-cos-django-gallery

` cd IMBApp`

# Export your api key after creating service credentials for the bucket in IBM Cloud.
`export MY_COS_IBM_KEY_TEMP=<your API key from service credentials>`

# Export your secret keys to add in the environment variable

`export export MY_SVC_IBM_INST_ID_TEMP=<service instance id >`

# To change the bucket name go to file IBMA/views.py


# to change the image size go to file templates/index.html

#Run below commands and you can view your gallery in broswer http://127.0.0.1:8000

`python manage.py runserver`




