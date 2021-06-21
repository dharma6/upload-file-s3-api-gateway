response_message ={
    "fileFormat":"only csv, json,hl7 are allowed",
    "uploadException":"Exception seen while uploading the file. Failure, file not uploaded",
    "restException":"Exception seen when posting the content to the rest API",
    "file_upload_api_success":"File is successfully upload to s3, Issues in calling API"
}
constants ={
    "s3_folder_path":"incoming-files/",
    "bucket_name":"upload-file-s3",
    "post_back_url":"https://xpk8jjxnei.execute-api.us-east-1.amazonaws.com/api/v1/filesmetadata"
}