#
import thread
import urllib2
import json
from time import sleep
import time

def ipToGeoinfo(ip):
    url = "http://www.iptolatlng.com?ip="+ ip
    data = urllib2.urlopen(url).read()
    #print data
    geoInfo = json.loads(data)
    return geoInfo

def geoLocExtractor():
    in_f = open("../resources/xiaomi_com.csv","r")
    out_f = open("../resources/geoInfo","w")
    tmpcnt = 0
    stime = time.time()
    for line in in_f:
        tmpcnt+=1
        if (tmpcnt%800!=0):
            continue
        elems = line.split(",")
        ip = elems[4][1:-2]
        if(ip == 'hidden'):
            continue
        geoInfo = ipToGeoinfo(ip)
        out_f.write(str(geoInfo['lat'])+" "+str(geoInfo['lng']))
        #sleep(0.1)
    print time.time()-stime,'s'

def latlngThreadWriter(ip,outFileName):
    out_f = open(outFile)

if __name__ == '__main__':
    geoLocExtractor()