pipeline {
    agent any

    stages {
        stage ("Deploy") {
            steps {
                sh 'docker build -t test:lastest .'
                sh 'docker run --rm -d test:lastest'
            }
        }
    }
}