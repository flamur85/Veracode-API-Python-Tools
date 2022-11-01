# Veracode-API-Python-Tools

Quick and easy set of tools to run for Veracode. 

<b>Directions:</b><ul>
<li>Import any python dependencies.</li>
<li>Create API credentials in Veracode (https://docs.veracode.com/r/c_api_credentials3).</li>
<li>Configure an API credentials file locally (https://docs.veracode.com/r/c_configure_api_cred_file) and your all set to run locally. </li>
</ul>

Tools (one for now):<ol>
 <li><b>GetBrokenDastScans.py</b> - Run this tool to get a list of broken Dast scans. Currently, you have to log into the portal daily to check the status. </li>
</ol>

<b><i>*Automate these script in Jenkins (via Jenkinsfile) to run daily so that you get notified upon a failure.</b></i> 
