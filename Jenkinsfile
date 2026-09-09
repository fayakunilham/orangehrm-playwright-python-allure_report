pipeline {

    agent any

    environment {
    PYTHON = 'C:\\Users\\Hype\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'

        // Credentials Jenkins
        ORANGEHRM_URL = credentials('orangehrm-url')
        ORANGEHRM_USERNAME = credentials('orangehrm-username')
        ORANGEHRM_PASSWORD = credentials('orangehrm-password')
    }

    stages {

        stage('Checkout') {
            steps {
                echo '========================================'
                echo 'CHECKOUT SOURCE CODE'
                echo '========================================'

                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo '========================================'
                echo 'PYTHON ENVIRONMENT'
                echo '========================================'

//                 bat 'python --version'
//                 bat 'python -m pip --version'

                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m pip --version'

            }
        }

        stage('Install Dependencies') {
            steps {
                echo '========================================'
                echo 'INSTALL DEPENDENCIES'
                echo '========================================'

//                 bat 'python -m pip install --upgrade pip'
//                 bat 'python -m pip install -r requirements.txt'

                bat '"%PYTHON%" -m pip install --upgrade pip'
                bat '"%PYTHON%" -m pip install -r requirements.txt'

            }
        }

        stage('Install Playwright') {
            steps {
                echo '========================================'
                echo 'INSTALL PLAYWRIGHT BROWSER'
                echo '========================================'

//                 bat 'python -m playwright install chromium'

                bat '"%PYTHON%" -m playwright install chromium'

            }
        }

        stage('Prepare Test Results') {
            steps {
                echo '========================================'
                echo 'PREPARE TEST RESULT DIRECTORY'
                echo '========================================'

                bat '''
                    if exist allure-results rmdir /s /q allure-results
                    if exist test-results rmdir /s /q test-results
                    if exist logs rmdir /s /q logs

                    mkdir allure-results
                    mkdir test-results
                    mkdir logs
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '========================================'
                echo 'RUN PLAYWRIGHT TEST'
                echo '========================================'

//                 bat '''
//                     pytest -v ^
//                     --alluredir=allure-results ^
//                     --log-file=logs/pytest.log ^
//                     --log-file-level=INFO
//                 '''

                    bat '''
                        "%PYTHON%" -m pytest -v ^
                        --alluredir=allure-results ^
                        --log-file=logs/pytest.log ^
                        --log-file-level=INFO
                    '''

            }
        }
    }

    post {

        always {

            echo '========================================'
            echo 'COLLECTING TEST RESULTS'
            echo '========================================'

            /*
             * Archive semua hasil automation.
             *
             * allowEmptyArchive = true
             * supaya Jenkins tidak gagal hanya karena
             * salah satu folder tidak menghasilkan file.
             */

            archiveArtifacts(
                artifacts: '''
                    logs/**/*,
                    screenshots/**/*,
                    videos/**/*,
                    test-results/**/*,
                    allure-results/**/*,
                    **/*.png,
                    **/*.webm,
                    **/*.zip
                ''',
                allowEmptyArchive: true,
                fingerprint: true
            )

            echo '========================================'
            echo 'GENERATING ALLURE REPORT'
            echo '========================================'

            allure([
                includeProperties: false,
                results: [
                    [path: 'allure-results']
                ]
            ])

            echo '========================================'
            echo 'TEST EXECUTION COMPLETED'
            echo '========================================'
        }

        success {

            echo '========================================'
            echo 'PLAYWRIGHT TESTS PASSED'
            echo '========================================'
        }

        failure {

            echo '========================================'
            echo 'PLAYWRIGHT TESTS FAILED'
            echo '========================================'

            echo 'Please check:'
            echo '1. Console Output'
            echo '2. Allure Report'
            echo '3. Screenshot'
            echo '4. Video'
            echo '5. Test Log'
        }

        unstable {

            echo '========================================'
            echo 'PLAYWRIGHT TESTS UNSTABLE'
            echo '========================================'
        }
    }
}