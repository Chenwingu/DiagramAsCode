# Import necessary modules from the diagrams library
from diagrams import Cluster, Diagram, Edge, Node
from diagrams.k8s.infra import ETCD
from diagrams.k8s.controlplane import APIServer, ControllerManager, CCM, KubeProxy, Kubelet, Scheduler

# Create a new Diagram object
with Diagram("Kubernetes Cluster", show=False, direction="BT", graph_attr={"ranksep": "1.3", "nodesep": "0.8", "splines": "ortho", "ratio": "0.5", "fontsize": "40"}):
        # Create a cluster for the Control Plane
        with Cluster("Control Plane",  graph_attr={"fontsize": "20"}):
           # Define nodes for the Control Plane
           etcd_server = ETCD("")
           scheduler = Scheduler("")
           api_server = APIServer("", color="blue", shape="doublecircle")
           controller_manager = ControllerManager("")
           cloud_controller_manager = CCM("")

           # Connect the API Server to ETCD, Scheduler, and Controller Manager
           etcd_server << api_server
           scheduler << api_server
           controller_manager << api_server
           cloud_controller_manager << Edge(color="purple", style="dashed") << api_server

        # Create clusters for each Node
        with Cluster("Node 1",  graph_attr={"fontsize": "20"}):
           # Define nodes for Node 1
           kubelet1 = Kubelet("")
           kube_proxy1 = KubeProxy("")
           # Create an invisible node for merging connections
           merge_node1 = Node("", shape="point", width="0")
           kubelet1 - merge_node1 >> api_server
           kube_proxy1 - merge_node1

        with Cluster("Node 2",  graph_attr={"fontsize": "20"}):
           # Define nodes for Node 2
           kubelet2 = Kubelet("")
           kube_proxy2 = KubeProxy("")
           # Create an invisible node for merging connections
           merge_node2 = Node("", shape="point", width="0")
           kubelet2 - merge_node2 >> api_server
           kube_proxy2 - merge_node2

        with Cluster("Node 3",  graph_attr={"fontsize": "20"}):
           # Define nodes for Node 3
           kubelet3 = Kubelet("")
           kube_proxy3 = KubeProxy("")
           # Create an invisible node for merging connections
           merge_node3 = Node("", shape="point", width="0")
           kubelet3 - merge_node3 >> api_server
           kube_proxy3 - merge_node3

