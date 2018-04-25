from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.shortcuts import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import subprocess
import os
import os.path
import paramiko
import csv
import shutil
from paramiko import SSHClient
from scp import SCPClient
import re
from .models import livedatas

def server_login(request):
	
	return render(request,'liveapp/login.html',{'error':'Enter ur Server Details'})



def firstindex(request):
    if request.method == 'POST':
        userid = request.POST.get('user_field', None)
        host=request.POST.get('hostname_field', None)
        passwd=request.POST.get('pswd_field')


    pscmd="""ps aux --sort -rss |awk 'BEGIN{OFS="||"}  NR<=10 { print $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11}'"""
    netstat=""" netstat -tu |awk 'BEGIN{OFS="||" } { print $1,$2,$3,$4,$5,$6}'"""

    sshObj  = paramiko.SSHClient()
    sshObj .set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        sshObj .connect(host, username=userid, password=passwd )
    except Exception as ERR:
        print(ERR)
        return render(request,'liveapp/login.html',{'error':"incorrect server Details"})
    stdin, stdout, stderr = sshObj .exec_command(pscmd)
    stdin2, stdout2, stderr2 = sshObj .exec_command(netstat)
    stdout1=stdout.readlines()
    stdout1_st = list(map(lambda x: x.strip(), stdout1))
    ad=[]
    for iy in stdout1_st:
        b=(iy.split("||"))
        ad.append(b)
    stdout3=stdout2.readlines()
    stdout3_st = list(map(lambda x: x.strip(), stdout3))
    stdn=[]
    for ia in stdout3_st:
        a=(ia.split("||"))
        stdn.append(a)

    # print stdout1
    # print stdout3
    return render(request,'liveapp/index.html',{'header_ps':ad[0],'stdout1':ad[1:],'header_conn':stdn[1],'stdout3':stdn[2:]})

def secondindex(request):
    a=request.POST['val']
    q=livedatas.objects.create(PSDETAILS=a)
    q.save()
    return render(request,'liveapp/index2.html')

 
