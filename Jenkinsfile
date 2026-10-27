
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Verify Environment') {
            steps {
                bat 'where.exe git'
                bat 'where.exe python'
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('Checkout Code') {
            steps {
                checkout scm
                bat 'git branch --show-current'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                if exist requirements.txt (
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                ) else if exist requirement.txt (
                    .venv\\Scripts\\python.exe -m pip install -r requirement.txt
                ) else (
                    echo ERROR: requirements.txt or requirement.txt not found.
                    exit /b 1
                )
                '''
            }
        }

        stage('Install Playwright Browser') {
            steps {
                bat '.venv\\Scripts\\python.exe -m playwright install chromium'
            }
        }

        stage('Run Automation Tests') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat '.venv\\Scripts\\python.exe -m pytest -v --junitxml=reports\\junit.xml'
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit.xml',
                  allowEmptyResults: true

            archiveArtifacts artifacts: 'reports/**',
                             allowEmptyArchive: true
        }
    }
}
