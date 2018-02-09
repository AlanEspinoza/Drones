from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

#El dron se enlaza y despega
def arm_and_takeoff(TargetAltitude):
	print("Executing takeoff")

	while not drone.is_armable:
		print("Vehicle is not armable, waiting....")
		time.sleep(1)

	print("ready to arm")
	drone.mode = VehicleMode("GUIDED")
	drone.armed = True
	while not drone.armed:
		print("Waiting for arming....")
		time.sleep(1)

	print("Ready for takooff, taking off...")
	drone.simple_takeoff(TargetAltitude)

	while True:
		Altitude = drone.location.global_relative_frame.alt
		print("altitude: ",Altitude)
		time.sleep(1)

		if Altitude >= TargetAltitude * 0.95:
			print("Altitude reached")
			break


#Vehicle connection 

#Se enlaza a la laptop
drone = connect('127.0.0.1:14551', wait_ready=True)
arm_and_takeoff(20)

#Coordenadas de vuelo
drone.airspeed = 10
a_location = LocationGlobalRelative(20.736291,-103.456896,20)
b_location = LocationGlobalRelative(20.735932,-103.456938,20)
c_location = LocationGlobalRelative(20.735951,-103.457305,20)


print("Se mueve al punto a")
drone.simple_goto(a_location)
time.sleep(20)
print("Se mueve al punto b")
drone.simple_goto(b_location)
time.sleep(20)
print("Se mueve al punto c")
drone.simple_goto(c_location)
time.sleep(20)

#aterriza en donde salio
drone.mode = VehicleMode("RTL")

#el nivel de bateria
print(drone.batery.level,"v")