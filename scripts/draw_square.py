#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def draw_square():
    rospy.init_node('draw_square', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz
    move_cmd = Twist()

    for _ in range(5):  # Draw a square
        # Move forward
        move_cmd.linear.x = 2.0
        move_cmd.angular.z = 0.0
        pub.publish(move_cmd)
        rospy.sleep(2)

        # Turn 90 degrees
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 1.56  # Approx 90 degrees
        pub.publish(move_cmd)
        rospy.sleep(2)

    # Stop the turtle
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)

if __name__ == '__main__':
    try:
        draw_square()
    except rospy.ROSInterruptException:
        pass

