# Veracode-API-Python-Tools

Quick and easy set of tools to run for Veracode. 

<b>Directions:</b><ol>
<li>Create API credentials in Veracode (https://docs.veracode.com/r/c_api_credentials3).</li>
<li>Configure an API credentials file locally (https://docs.veracode.com/r/c_configure_api_cred_file).</li>
<li>Import all python dependencies.</li></ol>
You should now be all set to run the scripts locally!

<br><b>Tools:</b><ol>
 <li><b>GetBrokenDastScans.py</b> - Run this tool to get a list of broken Dast scans. Currently, you have to log into the portal daily to check the status. </li>
 <li>More to come!</li></ol>

<i>*Automate these script in Jenkins <b>(via Jenkinsfile)</b> to run daily so that you get notified upon a failure.</i> 
<br><br>More information about this integration: https://docs.veracode.com/r/c_enabling_hmac
