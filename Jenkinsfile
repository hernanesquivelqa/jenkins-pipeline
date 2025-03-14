pipeline {
    agent any
    
    // Parámetros para personalización
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Rama a construir')
        choice(name: 'ENVIRONMENT', choices: ['dev', 'prod'], description: 'Entorno de despliegue')
    }

    // Variables de entorno dinámicas
    environment {
        appName = "mi-app-${env.BUILD_NUMBER}"
        //MY_CREDENTIALS = credentials('my-secret-id') // Asume que tienes una credencial configurada en Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/hernan97carp/jenkins-pipeline.git', branch: "${params.BRANCH}"
            }
        }

        // Control de errores con try-catch
        stage('Build') {
            steps {
                script {
                    try {
                        echo 'Building...'
                        bat 'echo Hello World'
                    } catch (Exception e) {
                        echo "Error during build: ${e.getMessage()}"
                        error "Build failed due to an error"
                    }
                }
            }
        }

        // Stage para pruebas
        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'echo Tests passed!'
            }
        }

        // Stage para construir un artefacto
        stage('Package') {
            steps {
                echo 'Packaging the app...'
                bat 'echo Packaged!'
            // archiveArtifacts artifacts: '**/*.jar', allowEmptyArchive: true
            }
        }

        // Stage de despliegue
        stage('Deploy') {
            when {
                expression { params.ENVIRONMENT == 'prod' }
            }
            steps {
                echo "Deploying to ${params.ENVIRONMENT}..."
                bat 'echo Deployed!'
            }
        }
    }

    //Notificaciones
    post {
        always {
            echo "Cleaning up..."
            deleteDir()
        }
        success {
            echo 'Pipeline succeeded!'
            //mail to: 'email@dominio.com',
                // subject: "Build ${env.JOB_NAME} #${env.BUILD_NUMBER} Succeeded",
                // body: "El build fue exitoso. Revisa ${env.BUILD_URL}"
        }
        failure {
            echo 'Pipeline failed!'
           // mail to: 'email@dominio.com',
                // subject: "Build ${env.JOB_NAME} #${env.BUILD_NUMBER} Failed",
                // body: "El build falló. Revisa ${env.BUILD_URL}"
        }
    }
}