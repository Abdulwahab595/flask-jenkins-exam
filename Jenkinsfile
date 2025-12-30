pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Stage 1: Pulling latest code from GitHub...'
                // Jenkins handles the clone automatically when linked to GitHub
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Stage 2: Installing Python libraries...'
                // This tells Windows to install what is in your requirements.txt
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Stage 3: Running Pytest...'
                // This runs the test_app.py file you just created
                bat 'pytest test_app.py'
            }
        }

        stage('Build Application') {
            steps {
                echo 'Stage 4: Building/Packaging App...'
                // This simulates a build process by creating a 'dist' folder
                bat 'mkdir dist && copy app.py dist\\'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Stage 5: Deploying App...'
                // This simulates deployment by echoing a success message
                echo 'Application has been deployed to the target directory successfully!'
            }
        }
    }

    post {
        always {
            echo 'Final Exam Status: Task Completed by Abdul Wahab (22i-1714)'
        }
    }
}
