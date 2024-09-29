pipeline {
    
  environment {
    imagename = "muzafferjoya/spring-boot-poc"  // Update this to your desired Docker image name
    registryCredential = 'muzaffar-hub-id'      // Docker Hub credentials
    dockerImage = ''
    poetryBin = "/var/lib/jenkins/.local/bin"
  }
  
  agent any
  
  stages {
      
    stage('Clean Workspace') {
       steps {
           cleanWs()
       }
    }
        
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/kunal-copods/monorepo.git', branch: 'with-docker'])
      }
    }
    
    stage('Setting up Python Environment') {
      steps {
          dir('backend'){
        sh 'curl -sSL https://install.python-poetry.org | python3 -' // Install Poetry
        sh 'export PATH="$poetryBin:$PATH" && poetry install --no-dev'
      }
     }
    }
    
    stage('Building Python Package') {
      steps {
          dir('backend'){
          sh 'export PATH="$poetryBin:$PATH" && poetry build'
      }
      }
    }
    
    stage('Archive Artifact') {
      steps {
          dir('backend'){
        archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: false
      }
    }
  }
    
    // stage('Building Docker Image') {
    //   steps {
    //     script {
    //       dockerImage = docker.build imagename // Build the Docker image
    //     }
    //   }
    // }
   
  }
  
  post {
    always {
      cleanWs() // Clean workspace after build
    }
  }
}
