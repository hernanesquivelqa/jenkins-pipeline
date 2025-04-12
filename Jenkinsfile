pipeline {
    agent any
    environment {
        PYTHON = "${env.MY_PYTHON}" // o directamente "python" si ya está en PATH
    }
    stages {
        stage('Setup') {
            steps {
                bat 'npm install'

                // ✅ Mostrar contenido del requirements.txt
                bat 'type requirements.txt'

                // ✅ Instalación de dependencias
                bat """
                    %PYTHON% -m pip install --upgrade pip
                    %PYTHON% -m pip install -r requirements.txt
                """
            }
        }
        stage('Start App and Run Tests') {
            steps {
                // ✅ Inicia la app en segundo plano
                bat 'start /B npm run dev'
                bat 'timeout /T 10'

                // ✅ Ejecuta tests
                bat '%PYTHON% -m pytest tests/test_app.py --html=report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            // ✅ Publicar reporte
            publishHTML(target: [
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest Results',
                keepAll: true
            ])
            
            // ✅ Mata procesos de node.js
            bat 'taskkill /F /IM node.exe || exit 0'
        }
    }
}
