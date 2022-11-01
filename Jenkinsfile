pipeline {
    agent any
     environment {
        CREDS = credentials('') //Insert the environment variable name stored in Jenkins.
    }
    stages {
        stage('Run Python Script') {
            agent {
                docker {
                    image 'python:3.10.7-alpine'
                }
            }
            steps {
                sh 'python --version'
                sh 'python -m venv env'
                sh	"""
                	source ./env/bin/activate
					python --version
					python -m pip install veracode-api-signing
					python -m pip install requests
                    export VERACODE_API_KEY_ID=$CREDS_USR
                    export VERACODE_API_KEY_SECRET=$CREDS_PSW
					python GetBrokenDastScans.py
				   	"""
            }
        }
    }
    post {
        success {
             echo 'This ran successfully!'
         }
         failure {
            emailext body: 'Please take a look ASAP! \n\n${BUILD_LOG, maxLines=100, escapeHtml=false}',
                    to: "insertyouremailhere@test.com",
                    subject: 'Jenkins: A Veracode DAST scan is currently broken.'
         }
    }
}
