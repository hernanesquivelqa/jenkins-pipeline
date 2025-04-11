pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Instalar dependencias de Node.js
                bat 'npm install'
                // Crear entorno virtual si no existe y activarlo
                bat """
                    if not exist venv (
                        python -m venv venv
                    )
                    venv\\Scripts\\pip install --upgrade pip
                    venv\\Scripts\\pip install -r requirements.txt
                """
                // Ejecutar tests y generar reporte en Setup
                bat 'venv\\Scripts\\python -m pytest tests/test_app.py --html=report.html --self-contained-html'
            }
        }

        stage('Start App') {
            steps {
                // Iniciar la aplicación en segundo plano
                bat 'start /B npm run dev'
                // Esperar a que la aplicación esté lista
                bat 'timeout /T 10'
            }
        }

        stage('Run Tests') {
            steps {
                // Activar entorno virtual y ejecutar tests
                bat 'venv\\Scripts\\activate && pytest tests/test_app.py --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            // Publicar el reporte HTML
            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest Results',
                keepAll: true
            ])
            // Terminar procesos de Node.js
            bat 'taskkill /F /IM node.exe || exit 0'
        }
    }
}