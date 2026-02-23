---
title: "Send_NSCA.exe example"
date: 2009-08-11
categories: 
  - "nagios"
  - "nsca"
  - "send_nsca"
---

1\. Make sure you edit your send\_nsca.cfg accordingly  
  
2\. Copy to c:\\test.vbs  
  

> Set oArgs = WScript.Arguments.Unnamed  
> Set WshShell = CreateObject("WScript.Shell")  
> ' 0 = hostname of local machine  
> ' 1 = checkname  
> ' 2 = result, 0 is ok, 1 is warn, 2 is crit  
> ' 3 = notes from the output  
> ' Written by John McLear of Primary Technology 2009  
> exepath = "c:\\program files\\montitech\\nc\_net\\config\\send\_nsca.exe" ' path to exe  
> cfgpath = "c:\\program files\\montitech\\nc\_net\\config\\send\_nsca.cfg" ' path to cfg  
> host = "nagios.server.com" 'host nagios server  
> tab = Chr(9)  
> prefix = "c:\\windows\\system32\\cmd.exe /q /c echo "  
> cmd= prefix & oArgs.Item(0) & tab & oArgs.Item(1) & tab & oArgs.Item(2) & tab & oArgs.Item(3) & " | " & chr(34) & exepath & chr(34) & " -H " & host & " -c " & chr(34) & cfgpath & chr(34)  
> wscript.echo cmd  
> ' Remove or rem out above line after debug  
> WshShell.Run(cmd)

  
  
3\. Edit nagios.server.com to your nagios server name.  
  
4\. Start - run - cmd - cscript c:\\test.vbs Myhostname Mycheckname Status(seebelow)  
My Example: cscript c:\\test.vbs mooocow simsdbversion 0 3.142
