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
                bat """
                    %PYTHON% -m pip install --upgrade pip
                    %PYTHON% -m pip install -r requirements.txt
                """
            }
        }
        stage('Run Tests') {
            steps {
                // Si la app es necesaria:
                bat 'start /B npm run dev'
                bat 'timeout /T 10' // Espera 10 segundos
                bat '%PYTHON% -m pytest'
            }
        }
    }
    post {
        always {
            bat 'taskkill /F /IM node.exe || exit 0'
        }
    }
}
