
import json
import boto3
#import mimetypes
#import magic
import uuid
import config as cf
from services.s3Service import S3Service
from services.apiService import ApiService



def upload_file_S3(event, context):
	""" This method revolves around uploading a file to S3.

    Parameters
    event: Event generated from lambda
    """

	s3 = boto3.client("s3")
	file_name = event['headers']['file-name']
	user_id = event['headers']['user-id']
	file_content = event['body']
	bucket_name = cf.constants['bucket_name']
	file_id = str(uuid.uuid4())
	s3ServiceObj=S3Service()
	# Method call
	extension = s3ServiceObj.vald_file_checker(file_name)
	#print("The recieved value is",extension)
	if(extension == "invalid"):
		return {
		"statusCode": 400,
		"body": json.dumps(cf.response_message['fileFormat'])
		}

	try:
		response_upload_object = s3ServiceObj.upload_file_tos3(bucket_name,file_id,file_content)
		print(response_upload_object)
		if(response_upload_object['ResponseMetadata']['HTTPStatusCode']==200):
			response_upload_api_call_exec=upload_api_call_exec(file_id,file_name,user_id,extension)
			print("The response_upload-api_call_exec ",response_upload_api_call_exec)
			if(response_upload_api_call_exec!="failure"):
				return {
					"statusCode": 200, 
					"body": response_upload_api_call_exec.content 
				}
			else:
				return{
					"statusCode":200,
					"body":cf.response_message['file_upload_api_success']
				}
		else:
			return{
				"statusCode": 400,
				"body":cf.response_message['uploadException']
			}

	except:
		print("Issues while uploading file to s3")
		return {    
			"statusCode": 400,
			"body": json.dumps(cf.response_message["uploadException"])
			}
def upload_api_call_exec(file_id,file_name,user_id,extension):
	""" This function calls the Rest API to upload the file_id and other attributes to DynamoDB

	Parameters
	file_id : string
		The file_id which need to be created in DynamoDB.
	file_name : string
		The file_name corresponding to the file_id
	user_id : string
		The user_id corresponding to the file_id
	extension : string
		The extension of the file

	 """

	try:
		apiService_obj = ApiService()
		content_api_call = apiService_obj.content_to_api_call(file_id, file_name, user_id, extension)
		print("The content api-call is",content_api_call)
		response_post_api_call = apiService_obj.post_api_call(content_api_call,cf.constants['post_back_url'])
		print("Reached here 4")
		print("The response_post_api call is",response_post_api_call)
		return response_post_api_call
	except:
		print("Failure in calling API")
		return "failure"



#Question 1:
  # Whether status code need to be placed in config,json and use it from there? 
