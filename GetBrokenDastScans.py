import requests
import logging
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]  # Outputs logs to the console
)

# Define constants
broken_dast_list = []
api_base = "https://api.veracode.com/was/configservice/v1/"
headers = {
    "Content-Type": "application/json"
}


def get_dast_analyses():
    analysis_array = []

    path = api_base + "analyses"
    try:
        response = requests.get(path, auth=RequestsAuthPluginVeracodeHMAC(), headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parsing JSON response for the 'embedded' array then parse for the 'analysis' array.
        if response.status_code == 200:
            json_array_response = response.json()
            embedded_array = json_array_response.get('_embedded', {})
            analysis_array = embedded_array.get('analyses', [])

        # Parsing the analysis array for the 'latest_occurrence_status' -> 'status_type' object.
        # Then checking the status type for a bad status and adding to a list.
        for json_object in analysis_array:
            try:
                status_type = json_object['latest_occurrence_status']['status_type']
                if status_type not in ['FINISHED_RESULTS_AVAILABLE_WITH_WARNING', 'FINISHED_RESULTS_AVAILABLE', 'IN_PROGRESS']:
                    broken_dast_list.append(json_object['name'])
            except KeyError as e:
                logging.error(f"Missing expected field: {e} in the analysis object. Check the structure of the response.")
            except Exception as e:
                logging.error(f"Error processing analysis object: {json_object}. Exception: {e}")

    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to retrieve DAST analyses: {e}")
        return


if __name__ == '__main__':
    logging.info('************************* - SCRIPT START - *************************')
    logging.info('Retrieving a list of broken DAST scans... Please wait.\n')

    get_dast_analyses()

    if len(broken_dast_list) > 0:
        logging.warning('Please check the following DAST scans immediately:')
        for item in broken_dast_list:
            logging.warning(item)
        logging.warning('-------------------------------------')
        logging.warning(f'Total number of broken DAST Scans: {len(broken_dast_list)}')
        logging.info('\n************************* - SCRIPT END - ***************************\n')
        exit(1)
    else:
        logging.info('All DAST scans seem to be in working order.')

    logging.info('\n************************* - SCRIPT END - ***************************\n')
