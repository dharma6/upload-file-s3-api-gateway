
import requests
import json
import traceback
class ApiService:
    """ 
    This class intended to provide helper methods W.r.t to API's

    Methods
    -------
    callRestAPI(file_name,extension,user_id)
        calls RestAPI to write information to DynamoDB.

    """
    def post_api_call(self,content_api_call, api_url):
        """ Rest API Call

        Attributes
        ----------
        file_name:string
            The name of the file which need to be posted.
        extension:string
            The extension of the file which need to be posted
        user_id:string
            Which need to be posted as well along with the above.   

        """
        response= requests.post(api_url, json = content_api_call)
        return response
    


    def content_to_api_call(self,file_id,file_name,user_id,extension):

        """Prepares an json to pass as an body to the rest api call

        Parameters:
        file_id: string
            Id which need to be uploaded to dynamo db
        file_name : string
            file_name associated with the file_id
        user_id: string
            To send the back the response of users with the user_id
        extension: string
            The extension of the file.

        Returns:
            A dictionary where file_id, file_name, user_id, and file_type are the keys.
        
        """
        api_call_content = [{'file_id': file_id, 'file_name': file_name, 'user_id' : user_id, 'file_type':extension}]
        print("The api-call-content is",api_call_content)
        #print("The api-call content type is",type(api_api_call_content))
        return api_call_content


         #Corrections:
         # I have to use same uuid when posting the
         #URL as parameter
         #Seperate function for post event
         #PostDataToURL take only 2 parameters.