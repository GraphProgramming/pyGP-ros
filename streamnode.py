import rospy

def init(node, global_state):
    node["main_thread"] = True
    def tick(value):
        rospy.init_node(node["args"]["name"], anonymous=node["args"]["anonymous"])
        #rospy.spin()
        return {"trigger": value["trigger"]}

    node["tick"] = tick

def spec(node):
    node["name"] = "(Serial) Ros Node Init"
    node["inputs"]["trigger"] = "Object"
    node["outputs"]["trigger"] = "Object"
    node["args"]["name"] = "GraphProgrammingNode"
    node["args"]["anonymous"] = False
    node["desc"] = "A ros node."
