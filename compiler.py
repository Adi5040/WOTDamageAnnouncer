import py_compile, zipfile, os

if os.path.exists("ReceivedDamage.zip"):
	os.remove("ReceivedDamage.zip")

py_compile.compile("res_mods/0.8.8/scripts/client/vehicle.py")

fZip = zipfile.ZipFile( "ReceivedDamage.zip", "w" )
fZip.write("res_mods/0.8.8/scripts/client/vehicle.pyc")
fZip.write("res_mods/0.8.8/scripts/client/vehicle_damage.json")
fZip.close()
