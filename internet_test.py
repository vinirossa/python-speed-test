import speedtest

st = speedtest.Speedtest()
  
while True:
    print("======= SPEED TEST =======")
    download_speed = st.download()/10**6
    print("Download Speed:","{0:.2f}".format(download_speed),"Mbps")
    upload_speed = st.upload()/10**6
    print("Upload Speed:","{0:.2f}".format(upload_speed),"Mbps")
    servernames =[]  
    st.get_servers(servernames) 
    print("Ping:",st.results.ping,"ms")  
