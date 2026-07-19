import subprocess 

print("This programe can be stopped with pressing Ctrl + c")
print("programe by abu")

app = "openvpn"
app1 = "openvpn.exe"
config = "offenso.ovpn"

os = input("windows or linux: ").strip().lower()

if os == "windows":
	subprocess.run([app1,"--config",config])
elif os == "linux":
	subprocess.run(["sudo",app,"--config",config])
else:
	print("select an os bruh")

#dont worry i didnt got 1QB virus for you yet

