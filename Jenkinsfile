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
                bat 'ping 127.0.0.1 -n 10'
            }
        }
        stage('Test') {
            steps {
                bat '%PYTHON% -m pytest tests/test_app.py --html=report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            script {
                bat 'taskkill /F /IM node.exe || exit 0'
                if (fileExists('report.html')) {
                    echo 'Report exists, publishing...'
                    publishHTML(target: [
                        reportDir: '.', 
                        reportFiles: 'report.html',
                        reportName: 'Pytest Report',
                        keepAll: true
                    ])
                } else {
                    echo 'No report found.'
                }
            }
        }
    }
}
