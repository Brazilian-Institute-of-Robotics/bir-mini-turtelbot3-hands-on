#!/usr/bin/env python3

# IMPORT DE COISAS QUE IREMOS USAR:
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist, Vector3
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseAction, MoveBaseGoal, MoveBaseActionResult

# CLASSE:
class Tartaruga:
    # funcao inicial:
    def __init__(self):
        rospy.init_node('explore')
        self.move_base_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)

    # funcao de publicar no topico goal move base:
    def goal_move_base(self, pose_x, pose_y, pose_z, pose_w):
        msg_move_to_goal = PoseStamped()
        msg_move_to_goal.pose.position.x = pose_x 
        msg_move_to_goal.pose.position.y = pose_y
        msg_move_to_goal.pose.orientation.z = pose_z
        msg_move_to_goal.pose.orientation.w = pose_w
        msg_move_to_goal.header.frame_id = 'map'

        rospy.sleep(1)

        self.move_base_pub.publish(msg_move_to_goal)
    
    # a funcao que iremos editar:
    def ir_para_ponto(self):
        self.goal_move_base(0.5,0,0,1)
        rospy.wait_for_message("/move_base/result", MoveBaseActionResult, timeout=None)
        
        self.goal_move_base(2,0.5,1,1)
        rospy.wait_for_message("/move_base/result", MoveBaseActionResult, timeout=None)
        
        self.goal_move_base(0,2,1,1)
        rospy.wait_for_message("/move_base/result", MoveBaseActionResult, timeout=None)

# FUNCAO PRINCIPAL:
if __name__ == '__main__':
    leonardo = Tartaruga()
    leonardo.ir_para_ponto()


