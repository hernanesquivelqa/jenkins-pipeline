pipeline {
    agent any
    environment {
        PYTHON = "${env.MY_PYTHON}" // o "python"
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
        stage('Start App and Run Tests') {
            steps {
                // Iniciar app
                bat 'start /B npm run dev'

                // Esperar unos segundos
                bat 'ping 127.0.0.1 -n 10'

                // Ejecutar tests
                bat '%PYTHON% -m pytest tests/test_app.py --html=report.html --self-contained-html'

                // Matar node para liberar el puerto o memoria
                bat 'taskkill /F /IM node.exe || exit 0'
            }
        }
    }
    post {
        always {
            script {
                if (fileExists('report.html')) {
                    echo 'Report exists, publishing...'
                    publishHTML(target: [
                        reportDir: '.',
                        reportFiles: 'report.html',
                        reportName: 'Pytest Results',
                        keepAll: true
                    ])
                } else {
                    echo 'No report found.'
                }
            }
        }
    }
}