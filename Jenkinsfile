pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/mayankchadha16/IMT2020045_JenkinsAssignment.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x factorial.py"
                sh "./factorial.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x unit_test_1.py"
                sh "./unit_test_1.py"
            }
        }
    } 
}