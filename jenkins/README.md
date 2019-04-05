<img src="https://jenkins.io/sites/default/files/jenkins_logo.png"/>

# Jenkins in Docker

Install Master

```bash
docker pull jenkins/jenkins:lts
```
Run Master

```bash
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

or

docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
docker logs CONTAINER_ID
```

Run Slave

```bash

```

[Read the Documentation](https://github.com/jenkinsci/docker/blob/master/README.md)
