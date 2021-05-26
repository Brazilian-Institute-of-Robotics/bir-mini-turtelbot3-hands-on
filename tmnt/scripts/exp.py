#!/usr/bin/env python3

# IMPORT DE COISAS QUE IREMOS USAR:
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Twist, Vector3
from move_base_msgs.msg import MoveBaseActionGoal, MoveBaseAction, MoveBaseGoal, MoveBaseActionResult
from random import *
from sensor_msgs.msg import Image

# CLASSE:
class Tartaruga:
    # funcao inicial:
    def __init__(self):
        rospy.init_node('explore')
        self.move_base_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)
        self.cicle_var = 150    

    # funcao de publicar no topico goal move base:
    def goal_move_base(self, pose_x, pose_y, pose_z, pose_w):
        msg_move_to_goal = PoseStamped()
        msg_move_to_goal.pose.position.x = pose_x 
        msg_move_to_goal.pose.position.y = pose_y
        msg_move_to_goal.pose.orientation.z = pose_z
        msg_move_to_goal.pose.orientation.w = pose_w
        msg_move_to_goal.header.frame_id = 'base_footprint'

        rospy.sleep(1)

        self.move_base_pub.publish(msg_move_to_goal)

    # funcao que se inscreve em um determinado topico:    
    def listener(self):
        rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback)    
        rospy.spin()
    
    # a funcao que iremos editar:
    def callback(self, data):
        if self.cicle_var >= 40:
            self.cicle_var = 0
            f_rand_x = round(uniform(1,2), 1)
            f_rand_y = round(uniform(-0.5,0.5), 1)

            rand_z = randint(-1,1)

            self.goal_move_base(f_rand_x, f_rand_y, rand_z, 1)
            rospy.loginfo('point')

        self.cicle_var +=1    

# FUNCAO PRINCIPAL:
if __name__ == '__main__':
    try:
        leonardo = Tartaruga()
        leonardo.listener()
    except rospy.ROSInterruptException:
        pass	

    
    