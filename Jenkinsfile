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
                bat 'ping 127.0.0.1 -n 10'

                // ✅ Ejecuta tests
                bat '%PYTHON% -m pytest tests/test_app.py --html=report.html --self-contained-html'
            }
        }
    }
  post {
    always {
        // Verificar si el archivo existe
        bat 'if exist report.html echo "Report exists" else echo "Report not found"'

        // Publicar el reporte solo si existe
        publishHTML(target: [
            reportDir: '.',
            reportFiles: 'report.html',
            reportName: 'Pytest Results',
            keepAll: true
        ])

        // Matar procesos de node.js para evitar que se queden corriendo
        bat 'taskkill /F /IM node.exe || exit 0'
    }
}
}
