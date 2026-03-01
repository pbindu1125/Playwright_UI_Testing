pipeline {
    agent {
        docker {
            // Use the official Playwright image (includes Python and all Browsers)
            image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                // Install your python libraries
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run UI Tests') {
            steps {
                // Run tests and generate a JUnit XML report for Jenkins to read
                // We don't use --headed because Jenkins servers don't have a screen
                sh 'pytest --junitxml=results.xml'
            }
        }
    }

    post {
        always {
            // 1. Process the test results to show graphs in Jenkins
            junit 'results.xml'
            
            // 2. Archive screenshots or videos if the 'test-results' folder exists
            archiveArtifacts artifacts: 'test-results/**/*.png, test-results/**/*.mp4', allowEmptyArchive: true
        }
    }
}