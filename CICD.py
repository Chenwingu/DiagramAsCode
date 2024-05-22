from diagrams import Diagram, Cluster, Custom
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.onprem.container import Docker
from diagrams.programming.language import Java


with Diagram("CI/CD Pipeline", show=False, graph_attr={"ranksep": "0.7", "nodesep": "0.4"}):
    
    with Cluster("New Feature - Development", graph_attr={"fontsize": "10"}):
         ticket = Custom("Ticket raised/assigned", "/path/to/jira.png")
         developer = Java("Write/test code")
         github = Github("Developer pushes code")
 
         ticket >> developer >> github 

    with Cluster("Continuous Integration", graph_attr={"fontsize": "10"}):
        jenkins = Jenkins("Jenkins")
        maven_test = Custom("Compile code/Unit test", "/path/to/maven.png")
        sonarqube = Custom("Code Quality Check", "/path/to/sonarqube.png")
        dependency_check = Custom("Vulnerability Scan", "/path/to/dependencycheck.png")
        maven_build = Custom("Build/Package Application", "/path/to/maven.png")

        jenkins >> maven_test >> sonarqube >> dependency_check >> maven_build

    github >> jenkins

    with Cluster("Artifact - Docker Image", graph_attr={"fontsize": "10"}):
         nexus = Custom("Push Artifact", "/path/to/nexus.png")
         docker_build = Docker("Docker build and Tag")
         trivy = Custom("Docker Image Scan", "/path/to/trivy.png")

         nexus >> docker_build >> trivy

    maven_build >> nexus

    with Cluster("Continuous Deployment", graph_attr={"fontsize": "10"}):
         docker_push = Docker("Docker Push")
         kubernetes = Custom("Deploy to Kubernetes",  "/path/to/kubernetes.png")

         docker_push >> kubernetes

    trivy >> docker_push
