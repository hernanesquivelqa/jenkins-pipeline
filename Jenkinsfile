pipeline {
    agent any
    environment {
        PYTHON = "${env.MY_PYTHON}" // o directamente "python" si está en el PATH
    }
    stages {
        stage('Setup') {
            steps {
                bat 'npm install'
                bat """
                    %PYTHON% -m pip install --upgrade pip
                    %PYTHON% -m pip install -r requirements.txt
                """
            }
        }
        stage('Start App and Run Tests') {
            steps {
                bat 'start /B npm run dev'
                bat 'timeout /T 10'
                bat '%PYTHON% -m pytest tests/test_app.py --html=report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest Results',
                keepAll: true
            ])
            bat 'taskkill /F /IM node.exe || exit 0'
        }
    }
}
