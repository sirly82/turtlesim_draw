#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def callback_pose(msg):
    rospy.loginfo("Pose: x=%f y=%f theta=%f", msg.x, msg.y, msg.theta)

def draw_square():
    rospy.init_node('draw_square')

    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('turtle1/pose', Pose, callback_pose)

    rospy.sleep(1)

    move_cmd = Twist()

    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # --- 1 rectange ---
        for _ in range(4):
            # Move forward
            move_cmd.linear.x = 2.0
            move_cmd.angular.z = 0.0
            pub.publish(move_cmd)
            rospy.sleep(2)

            # Turn 90 deg
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 1.57
            pub.publish(move_cmd)
            rospy.sleep(1.5)

        # Stop for 0.5s before next square
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 0.0
        pub.publish(move_cmd)
        rospy.sleep(0.5)

        rospy.loginfo("Kotak selesai → mulai kotak berikutnya")

    rospy.spin()

if __name__ == '__main__':
    draw_square()
