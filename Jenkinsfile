pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy'
            // Keep the workspace active for the post-processing
            reuseNode true 
        }
    }

    stages {
        stage('Run Tests') {
            steps {
                // We use 'python3 -m' to avoid the Exit Code 127 (Command Not Found)
                sh 'python3 -m pip install -r requirements.txt'
                
                // The '|| true' ensures that even if tests fail, 
                // Jenkins doesn't crash before reaching the 'post' block.
                sh 'python3 -m pytest --junitxml=results.xml || true'
            }
        }
    }

    post {
        always {
            // Because we are using 'agent' at the top level, 
            // this 'post' block now has the 'FilePath' context it needs.
            junit 'results.xml'
        }
    }
}