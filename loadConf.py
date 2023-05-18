import json
from os import environ

confFile = open("config.json")
conf = json.load(confFile)
confFile.close()

with open(environ["GITHUB_OUTPUT"], "a") as f:
    # the keys there matches the keys in jobs->load_conf->outputs of build.yml
    f.write("refs=" + str(conf["refs"]) + "\n")
    f.write("platforms=" + str(conf["platforms"]) + "\n")
