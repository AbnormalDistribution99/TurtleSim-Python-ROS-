#!/usr/bin/env python3
import rospy
import numpy
from geometry_msgs.msg import Twist

rospy.init_node('square', anonymous=True)
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10) # 10hz
speed = 3
length = 3.1415

print('Starting square . . .')
    
def straight_line(length,vel_msg,pub):
	vel_msg.linear.x = speed
	initial_time = rospy.Time.now().to_sec()
	distance_covered = 0

	while distance_covered <= length:
		pub.publish(vel_msg)
		final_time = rospy.Time.now().to_sec()
		distance_covered = speed*(final_time-initial_time)

	vel_msg.linear.x = 0    
	
def turtle_rotation(vel_msg,pub):
	angular_speed = 2
	vel_msg.angular.z = angular_speed
	initial_time = rospy.Time.now().to_sec()
	angle = 0

	while angle <= 1.5707:
		pub.publish(vel_msg)
		final_time = rospy.Time.now().to_sec()
		angle = angular_speed*(final_time-initial_time)
	vel_msg.angular.z = 0
while not rospy.is_shutdown():
    twist = Twist()
    vel_msg = twist
    
    while True:
    	straight_line(length, vel_msg, pub)
    	turtle_rotation(vel_msg, pub)
    	
    pub.publish(twist)
    rate.sleep() #sleep until the next time to publish
    

	
    

