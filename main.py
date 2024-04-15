from __future__ import print_function
import cloudmersive_validate_api_client
from cloudmersive_validate_api_client.rest import ApiException
from pprint import pprint


# Configure API key authorization: Apikey
configuration = cloudmersive_validate_api_client.Configuration()
configuration.api_key['Apikey'] = 'Your-api-key'

# create an instance of the API class
api_instance = cloudmersive_validate_api_client.EmailApi(cloudmersive_validate_api_client.ApiClient(configuration))
email = input("Enter Email to verify: ")

try:
    # Fully validate an email address
    api_response = api_instance.email_full_validation(email)
    is_disposable = api_response.is_disposable

    if not is_disposable:
        # Getting root domain
        domain_name = api_response.domain
        sub_domain = domain_name.split('.')
        root_domain = sub_domain[0]

        with open("IANA_Domains.txt", 'r') as file:
            valid_domains = [line.strip() for line in file.readlines()]
            if root_domain not in valid_domains:
                api_response.is_disposable = True

    pprint(api_response)
    quit()
except ApiException as e:
    print("Exception when calling EmailApi->email_full_validation: %s\n" % e)

