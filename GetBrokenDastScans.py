import requests
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


broken_dast_list = []
api_base = "https://api.veracode.com/was/configservice/v1/"
headers = {
    "Content-Type": "application/json"
}


def get_dast_analyses():
    analysis_array = ''

    path = api_base + "analyses"
    response = requests.get(path, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)

    # Parsing JSON response for the 'embedded' array then parse for the 'analysis' array.
    if response.status_code == 200:
        json_array_response = response.json()
        for embedded_key, embedded_value in json_array_response.items():
            if str(embedded_key) == '_embedded':
                embedded_array = embedded_value
                for analysis_key, analysis_value in embedded_array.items():
                    analysis_array = analysis_value
                break

        # Parsing the analysis array for the 'latest_occurrence_status' -> 'status_type' object.
        # Then checking the status type for a bad status and adding to a list.
        for json_object in analysis_array:
            try:
                if json_object['latest_occurrence_status']['status_type'] not in \
                        ['FINISHED_RESULTS_AVAILABLE_WITH_WARNING', 'FINISHED_RESULTS_AVAILABLE', 'IN_PROGRESS']:
                    broken_dast_list.append(json_object['name'])
            except:
                print(json_object)
                print('Error! Please check the - latest_occurrence_status - field to see if its missing...')


if __name__ == '__main__':
    print('\n************************* - SCRIPT START - *************************')
    print('Retrieving a list of broken DAST scans... Please wait. \n')
    get_dast_analyses()

    if len(broken_dast_list) > 0:
        print('Please check the following DAST scans immediately:')
        for item in broken_dast_list:
            print(item)
        print('-------------------------------------')
        print('Total number of broken DAST Scans: ' + str(len(broken_dast_list)))
        print('\n************************* - SCRIPT END - ***************************\n')
        exit(1)
    else:
        print('All DAST scans seem to be in working order.')

    print('\n************************* - SCRIPT END - ***************************\n')
