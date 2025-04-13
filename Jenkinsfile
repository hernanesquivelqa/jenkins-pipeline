pipeline {
    agent any
    environment {
        PYTHON = "${env.MY_PYTHON}"
    }
    stages {
        stage('Setup') {
            steps {
                bat 'npm install'
                bat 'type requirements.txt'
                bat '%PYTHON% -m pip install --upgrade pip'
                bat '%PYTHON% -m pip install -r requirements.txt'
            }
        }
        stage('Run App') {
            steps {
                // Si la app es necesaria para los tests:
                bat 'start /B npm run dev'
                bat 'ping 127.0.0.1 -n 10' // Espera 10 segundos para que arranque
            }
        }
        stage('Test') {
            steps {
                bat '%PYTHON% -m pytest'
            }
        }
    }

}
