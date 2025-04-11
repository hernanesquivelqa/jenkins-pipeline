pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                bat 'npm install'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Start App') {
            steps {
                bat 'start /B npm run dev'
                bat 'timeout /T 10'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests/test_app.py --html=report.html'
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest Results'
            ])
            bat 'taskkill /F /IM node.exe || exit 0'
        }
    }
}