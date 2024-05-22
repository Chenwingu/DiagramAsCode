from diagrams import Cluster, Diagram, Edge
from diagrams.aws.network import Route53, ELB
from diagrams.aws.compute import EC2, AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.database import ElastiCache
from diagrams.onprem.client import Users

with Diagram("3 Tier Web Application", show=False, graph_attr={"ranksep": "1.2", "nodesep": "0.4", "splines": "ortho", "ratio": "0.8", "fontsize": "20"}):
    users = Users("Users")
    route53 = Route53("Route53")
    elb = ELB("ELB")

    with Cluster("Web Tier", graph_attr={"fontsize": "20"}):
        asg = AutoScaling("ASG")
        with Cluster("Availability Zone 1"):
            ec2_instance1 = EC2("EC2")
        with Cluster("Availability Zone 2"):
            ec2_instance2 = EC2("EC2")
        with Cluster("Availability Zone 3"):
            ec2_instance3 = EC2("EC2")
        asg - [ec2_instance1, ec2_instance2, ec2_instance3]

    with Cluster("Database Tier", graph_attr={"fontsize": "20"}):
        elasticache = ElastiCache("ElastiCache")
        rds = RDS("RDS")

    users >> Edge(color="blue")\
    << route53
    users >> Edge(color="green", label="HTTP/HTTPS to 0.0.0.0/0")\
    >> elb >> Edge(color="black") << asg
    ec2_instance1 >> Edge(color="purple", label="Read/Write") << elasticache
    ec2_instance2 >> Edge(color="red", label="Read/Write") << rds

