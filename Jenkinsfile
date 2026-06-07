pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install flake8 mypy pytest pytest-cov aiofiles types-aiofiles prometheus_client'
            }
        }

        stage('Lint') {
            steps {
                sh 'flake8 . --max-line-length=120 --exclude=.venv --ignore=E265,W391,E231,E225,F401,E303,E261,E262,E712,W293,E266,E305,W291,E302,E301,E117,E111,E122,E271,E302,E999,W292,E501,E203,E226,F541'
            }
        }

        stage('Type Check') {
            steps {
                sh 'mypy week2_PyDepth/storage_devoop.py'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest week3_ToolsandInfra/test_StorageDevice.py --cov=week2_PyDepth --cov-report=term-missing'
            }
        }
    }
}