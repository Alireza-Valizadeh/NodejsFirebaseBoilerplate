import os
here = os.getcwd()
dir = os.path.join(here, "js")
if not os.path.exists(dir):
  os.mkdir(dir)
os.system('cmd /c "cd js & npm init -y"')
dataDir = os.path.join(here, "js", "DataAccess")
if not os.path.exists(dataDir):
  os.mkdir(dataDir)
validatorsDir = os.path.join(here, "js", "Validators")
if not os.path.exists(validatorsDir):
  os.mkdir(validatorsDir)
configsDir = os.path.join(here, "js", "Configs")
if not os.path.exists(configsDir):
  os.mkdir(configsDir)
testsDir = os.path.join(here, "js", "__tests__")
if not os.path.exists(testsDir):
  os.mkdir(testsDir)
helpersDir = os.path.join(here, "js", "Helpers")
if not os.path.exists(helpersDir):
  os.mkdir(helpersDir)
constantsDir = os.path.join(here, "js", "Helpers", "Constants")
if not os.path.exists(constantsDir):
  os.mkdir(constantsDir)
servicesDir = os.path.join(here, "js", "Configs")
if not os.path.exists(servicesDir):
  os.mkdir(servicesDir)
dataDirRead = os.path.join(here, "js", "DataAccess", "Read")
if not os.path.exists(dataDirRead):
  os.mkdir(dataDirRead)
dataDirWrite = os.path.join(here, "js", "DataAccess", "Write")
if not os.path.exists(dataDirWrite):
  os.mkdir(dataDirWrite)
file = open("js/index.js", "w")
file.write("const functions = require(\"firebase-functions\");")
file.write("const admin = require(\"firebase-admin\");")
file.write("exports.myFunction = functions.database.ref(\"myRef\").onWrite(async(change, context) => {})")
file.close()
