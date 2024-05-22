from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Github
from diagrams.onprem.container import Docker
from diagrams.programming.language import Java
from diagrams.generic.storage import Storage
from diagrams.onprem.compute import Server

with Diagram("CI/CD Pipeline", show=False, graph_attr={"ranksep": "0.7", "nodesep": "0.4", "splines": "polyline", "ratio": "0.15"}):
    
    with Cluster("New Feature - Development", graph_attr={"fontsize": "20"}):
         ticket = Custom("Ticket raised/assigned", r"C:\Users\ngucd\Desktop\Projects\diagrams\New folder\jira.png")
         developer = Java("Write/test code")
         github = Github("Developer pushes code")
 
         ticket >> developer >> github 

    with Cluster("Continuous Integration", graph_attr={"fontsize": "20"}):
        jenkins = Jenkins("Jenkins")
        maven_test = Custom("Compile code/Unit test", r"C:\Users\ngucd\Desktop\Projects\diagrams\New folder\maven.png")
        sonarqube = Custom("Code Quality Check", r"C:\Users\ngucd\Desktop\Projects\diagrams\New folder\sonarqube.png")
        dependency_check = Custom("Vulnerability Scan", r"C:\Users\ngucd\Desktop\Projects\diagrams\New folder\dependencycheck.png")
        maven_build = Custom("Build/Package Application", r"C:\Users\ngucd\Desktop\Projects\diagrams\New folder\maven.png")

        jenkins >> maven_test >> sonarqube >> dependency_check >> maven_build

    github >> jenkins

    with Cluster("Artifact - Docker Image", graph_attr={"fontsize": "20"}):
         nexus = Custom("Push Artifact", r"C:\Users\ngucd\Desktop\Projects\diagrams\New folder\nexus.png")
         docker_build = Docker("Docker build and Tag")
         trivy = Custom("Docker Image Scan", r"C:\Users\ngucd\Desktop\Projects\diagrams\New folder\trivy.png")

         nexus >> docker_build >> trivy

    maven_build >> nexus

    with Cluster("Continuous Delivery", graph_attr={"fontsize": "20"}):
         docker_push = Docker("Docker Push")
         kubernetes = Custom("Deploy to Kubernetes",  r"C:\Users\ngucd\Desktop\Projects\diagrams\New folder\kubernetes.png")

         docker_push >> kubernetes

    trivy >> docker_push
