pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'git@github.com:hernan97carp/jenkins-pipeline.git', credentialsId: 'github-ssh-key'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                bat 'echo Hello World'
            }
        }
    }
}