pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy'
            // This ensures the container stays up long enough for the post steps
            reuseNode true 
        }
    }

    stages {
        stage('Install and Run') {
            steps {
                sh 'pip install -r requirements.txt'
                // Use || true to ensure the pipeline doesn't stop before the post block
                sh 'pytest --junitxml=results.xml || true' 
            }
        }
    }

    // Move the post block here, inside the pipeline
    post {
        always {
            // Jenkins will now look in the workspace for these files
            junit 'results.xml'
            archiveArtifacts artifacts: 'test-results/**', allowEmptyArchive: true
        }
    }
}
