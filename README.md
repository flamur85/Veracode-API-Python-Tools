# Veracode-API-Python-Tools

Quick and easy set of tools to run for Veracode. Just import any dependencies, create credentials in Veracode (https://docs.veracode.com/r/c_api_credentials3), configure an api credentials file (https://docs.veracode.com/r/c_configure_api_cred_file) and your all set to run locally. 

Tools (one for now):
 <ul><b>GetBrokenDastScans.py</b> - Run this tool to get a list of broken Dast scans. Currently, you have to log into the portal daily to check the status. Automate this script in jenkins to run daily so that you get notified upon a failure. </ul>
