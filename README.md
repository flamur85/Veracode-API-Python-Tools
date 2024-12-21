# Veracode-API-Python-Tools

Quick and easy set of tools to run for Veracode. 

## Directions:
1. **Create API credentials in Veracode**  
   Follow the instructions to create your API credentials:  
   [Veracode API Credentials](https://docs.veracode.com/r/c_api_credentials3).

2. **Configure an API credentials file locally**  
   Follow the instructions to configure your API credentials file:  
   [Configure API Credentials](https://docs.veracode.com/r/c_configure_api_cred_file).

3. **Import all Python dependencies**  
   Use `pip install -r requirements.txt` or follow the next steps to set up a virtual environment.

Now, you should be all set to run the scripts locally!

## Tools:
- **GetBrokenDastScans.py**  
  Run this tool to get a list of broken DAST scans. Currently, you have to log into the portal daily to check the status.

- More tools coming soon!

> **Note:** Automate these scripts in Jenkins via a Jenkinsfile to run daily so that you get notified upon a failure.

More information about this integration:  
[Enabling HMAC in Veracode](https://docs.veracode.com/r/c_enabling_hmac)

---

# Setup and Run

## Creating a Virtual Environment

1. **Create a New Virtual Environment:**
   - On Windows:
     ```bash
     python -m venv venv
     ```
   - On macOS and Linux:
     ```bash
     python3 -m venv venv
     ```

2. **Activate Your Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

## Installing Packages

1. **Generate `venv_packages.txt` Using `pip freeze`:**
   - Run:
     ```bash
     pip freeze > venv_packages.txt
     ```
   - This command generates a list of installed packages and versions and saves it in the `venv_packages.txt` file.

2. **Install Packages from the `venv_packages.txt` File:**
   - Run:
     ```bash
     pip install -r venv_packages.txt
     ```

3. **Verify Installed Packages:**
   - Run:
     ```bash
     pip list
     ```

## Updating the .env File

1. **Edit the .env File:**
   - Open your `backup.env` file in a text editor.
   - Add or update key-value pairs as needed.
   - Rename `backup.env` to `.env`.

## Running the Script

1. **Activate Your Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

2. **Navigate to the Directory Containing `main.py`:**

3. **Run the Script:**
   - Execute:
     ```bash
     python main.py
     ```

4. **Deactivate the Virtual Environment (Optional):**
   - Run:
     ```bash
     deactivate
     ```

