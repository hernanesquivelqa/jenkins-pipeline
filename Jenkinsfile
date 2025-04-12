pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                // Instalar dependencias de Node.js
                bat 'npm install'
                // Usar withPythonEnv para crear/configurar el entorno virtual e instalar dependencias
                withPythonEnv('python') {
                    bat '''
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Start App and Run Tests') {
            steps {
                // Iniciar la aplicación en segundo plano
                bat 'start /B npm run dev'
                // Esperar a que la aplicación esté lista
                bat 'timeout /T 10'
                // Usar withPythonEnv para ejecutar las pruebas
                withPythonEnv('python') {
                    bat 'pytest tests/test_app.py --html=report.html --self-contained-html'
                }
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