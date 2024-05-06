def heating_cooling(actual_temp, desired_temp):
    if  actual_temp < desired_temp:
        print("Run Heat")
    elif actual_temp > desired_temp:
        print("Run A/C")
    elif actual_temp == desired_temp:
        print("Standby")


heating_cooling(70, 72)  # Should print "Run heat"
heating_cooling(75, 70)  # Should print "Run A/C"
heating_cooling(72, 72)  # Should print "Standby"