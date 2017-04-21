import rospy

def init(node, global_state):
    node["main_thread"] = True
    def tick(value):
        rospy.init_node(node["args"]["name"], anonymous=node["args"]["anonymous"])
        #rospy.spin()
        return {}

    node["tick"] = tick

def spec(node):
    node["name"] = "Ros Node Init"
    node["args"]["name"] = "GraphProgrammingNode"
    node["args"]["anonymous"] = False
    node["desc"] = "A ros node."
