#coding:utf-8

#变量和命名


cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driver = cars - drivers
cars_driver = drivers
carpool_capacity = cars_driver * space_in_a_car
average_passengers_per_car = passengers / cars_driver

print "There are", cars,"cars availiable."
print "There are only", drivers,"drivers availiable."
print "There will be", cars_not_driver,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car, "in each car."
