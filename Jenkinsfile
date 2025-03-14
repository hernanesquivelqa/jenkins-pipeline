pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/hernan97carp/jenkins-pipeline.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                bat 'echo Hello World' // Usa 'bat' para Windows
            }
        }
    }
}