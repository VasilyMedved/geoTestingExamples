import telnetlib

# Works only for Android 
# 'MockGeoFix' application should be installed and running on device!

port = b'5554'
host = b'192.168.88.161'
device = telnetlib.Telnet(host=host,port=port)
device.write(b'geo fix ' + xpoint + b' ' + ypoint + b' ' + b'\n')
''' it's also possible to send NMEA route using the same techique, 
could be something like device.write('geo nmea $GPRMC,081836,A,3751.65,S,14507.36,E,000.0,360.0,130998,011.3,E*62') 
'''