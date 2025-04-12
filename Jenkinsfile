pipeline {
    agent any
    environment {
        PYTHON = "${env.MY_PYTHON}" // o directamente "python" si ya está en PATH
    }
    stages {
        stage('Setup') {
            steps {
                // Instalar dependencias de npm
                bat 'npm install'

                // Mostrar el contenido del requirements.txt para verificar
                bat 'type requirements.txt'

                // Instalación de dependencias de Python
                bat """
                    %PYTHON% -m pip install --upgrade pip
                    %PYTHON% -m pip install -r requirements.txt
                """
            }
        }
        stage('Start App and Run Tests') {
            steps {
                // Iniciar la app en segundo plano
                bat 'start /B npm run dev'

                // Esperar para asegurarse de que el servidor esté listo
                bat 'ping 127.0.0.1 -n 10'  // Espera 10 "paquetes" antes de continuar

                // Ejecutar los tests con pytest y generar el reporte en HTML
                bat '%PYTHON% -m pytest tests/test_app.py --html=report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            // Verificar si el archivo report.html existe y publicarlo si es así
            bat '''
            if exist report.html (
                echo "Report exists, proceeding to publish"
                // Publicar el reporte de pytest
                publishHTML(target: [
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Pytest Results',
                    keepAll: true
                ])
            ) else (
                echo "Report not found, skipping publish"
            )
            '''

            // Verificar si hay procesos de node.js y matarlos si es necesario
            bat 'tasklist /FI "IMAGENAME eq node.exe" || exit 0'
            bat 'taskkill /F /IM node.exe || exit 0'
        }
    }
}
