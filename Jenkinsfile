pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aws-devops-app:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop aws-devops-container || true
                    docker rm aws-devops-container || true

                    docker run -d \
                        --name aws-devops-container \
                        -p 8000:8000 \
                        aws-devops-app:${BUILD_NUMBER}
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 3'
                sh 'curl -f http://localhost:8000/health'
            }
        }
    }
}
