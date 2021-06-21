
import boto3
import json
import config as cf
class S3Service:
    """
    This class is intended to have helper methods for operations in s3.

    ...

    Methods
    --------
    validFileChecker(file_name)
        Checks the extension of the file and returns if the file is valid or not.

    """
    def vald_file_checker(self, file_name):
        """Returns "valid" if the file extension is of csv, hl7, json else returns invalid.

        Parameters
        ----------
        file_name : str
            File_name in string format

        Returns
        --------
        string
            Returns "valid" or "invalid" based on the extensionw

        """
        if("." in file_name):
             file_name_split = file_name.split(".")
             extension = file_name_split[1]
             check = ["csv","hl7","json"]
             if(extension  not in check):
                 print(cf.respomseMessage['fileFormat'])
                 return "invalid"
        else:
            #if the file-name doesn't have any extension return invalid
            return "invalid"
        return extension


    def upload_file_tos3(self,bucket_name,file_name,file_content):
        """Methof to upload file to s3.

        Parameters
        ----------
        bucket_name : string
            Name of the bucket, where the file need to be uploaded.
        file_name : string
            file which need to be uploaded to bucket
        file_content: json
            The content which is being uploaded to s3 with it's name as file_name
        """
        s3 = boto3.client("s3")
        s3_file_path = cf.constants['s3_folder_path']
        #s3.put_object is the method provided by boto3 to upload file.
        response_upload_object  = s3.put_object(Bucket=bucket_name, Key=s3_file_path+file_name,Body=file_content)
        print("The response upload object is",response_upload_object)
   
        # #print("The extension of the file is ",magic.from_file(fileContent, mime = True))
        return response_upload_object
       
        


