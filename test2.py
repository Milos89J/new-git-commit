# pip install pyspeedtest
# pip install speedtest
# pip install speedtest-cli

#method 1
import test2

speedTest = speedtest.Speedtest()
print(speedTest.get_best_server())

#Check download speed
print(speedTest.download())

#Check upload speed
print(speedTest.upload())

# Method 2

import test2
st = pyspeedtest.SpeedTest()
st.ping()
st.download()
st.upload()