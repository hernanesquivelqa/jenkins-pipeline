pipeline {
    agent any
    
    environment {
        appName = "variable"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/hernan97carp/jenkins-pipeline.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                bat 'echo Hello World'
            }
        }
    }

    post {
        always {
            echo "delete 'fase always'"
            deleteDir()
        }
        success {
            echo "echo 'fase success'"
        }
        failure {
            echo "echo 'fase failure'"
        }
    }
}