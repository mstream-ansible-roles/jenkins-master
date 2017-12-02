job("seed_job_test") {
  scm {
    git {
      remote {
        url("https://github.com/mstream-ansible-roles/jenkins-master.git")
      }
    }
  }
  configure {
    it / buildWrappers << "com.cloudbees.jenkins.plugins.customtools.CustomToolInstallWrapper" {
      selectedTools {
        "com.cloudbees.jenkins.plugins.customtools.CustomToolInstallWrapper_-SelectedTool" {
          name "maven3"
        }
      }
    }
  }
  steps {
    maven {
      goals('clean package')
      rootPOM('tests/files/test-project/pom.xml')
    }
  }
}