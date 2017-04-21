import rospy
import rostopic
import roslib
import time
import sys

def init(node, global_state):
    def callback(data):
        global_state.publish(node, "result", data.data)
        
    def tick(value):
        global_state.shutdown_blockers += 1
        time.sleep(1.0)
        data_type = None
        while data_type is None:
            data_type = rostopic.get_topic_type(node["args"]["topic"], blocking=False)[0]
        data_class = roslib.message.get_message_class(data_type)
        rospy.Subscriber(node["args"]["topic"], data_class, callback)
        return {}

    node["tick"] = tick

def spec(node):
    node["name"] = "Subscriber"
    node["outputs"]["result"] = "Object"
    node["args"]["topic"] = "/odom"
    node["desc"] = "Subscribes to a rostopic"
