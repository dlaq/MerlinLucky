#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import os
import sys
import json
import hashlib
from string import Template

parent_path = os.path.dirname(os.path.realpath(__file__))

def md5sum(full_path):
    """Calculate MD5 hash of a file"""
    with open(full_path, 'rb') as rf:
        return hashlib.md5(rf.read()).hexdigest()

def get_or_create():
    """Read or create config file"""
    conf_path = os.path.join(parent_path, "config_upgraded.json.js")
    conf = {}
    if not os.path.isfile(conf_path):
        print("config_upgraded.json.js not found，build.py is root path. auto write config_upgraded.json.js")
        module_name = os.path.basename(parent_path)
        conf["module"] = module_name
        conf["version"] = "1.6.0"
        conf["home_url"] = ("Module_%s.asp" % module_name)
        conf["title"] = "title of " + module_name
        conf["description"] = "description of " + module_name
    else:
        with open(conf_path, "r", encoding="utf-8") as fc:
            conf = json.loads(fc.read())
    return conf

def build_module():
    """Build the lucky_upgraded module"""
    try:
        conf = get_or_create()
    except Exception as e:
        print(f"config_upgraded.json.js file format is incorrect: {e}")
        import traceback
        traceback.print_exc()
        return
    
    if "module" not in conf:
        print("module is not in config_upgraded.json.js")
        return
    
    module_path = os.path.join(parent_path, conf["module"])
    if not os.path.isdir(module_path):
        print(f"not found {module_path} dir，check config_upgraded.json.js is module ?")
        return
    
    install_path = os.path.join(parent_path, conf["module"], "install.sh")
    if not os.path.isfile(install_path):
        print(f"not found {install_path} file，check install.sh file")
        return
    
    print("building...")
    
    # Write version file
    version_file = os.path.join(parent_path, conf["module"], "version")
    with open(version_file, "w") as f:
        f.write(conf["version"])
    
    # Create tar.gz package
    tar_cmd = f'cd "{parent_path}" && tar -czf {conf["module"]}.tar.gz {conf["module"]}'
    print(f"Executing: {tar_cmd}")
    os.system(tar_cmd)
    
    # Calculate MD5
    tar_file = os.path.join(parent_path, conf["module"] + ".tar.gz")
    if os.path.exists(tar_file):
        conf["md5"] = md5sum(tar_file)
        
        # Write updated config
        conf_path = os.path.join(parent_path, "config_upgraded.json.js")
        with open(conf_path, "w", encoding="utf-8") as fw:
            json.dump(conf, fw, sort_keys=True, indent=4, ensure_ascii=False)
        
        print(f"Build done: {conf['module']}.tar.gz")
        print(f"MD5: {conf['md5']}")
        print(f"Version: {conf['version']}")
    else:
        print(f"Error: tar file not created at {tar_file}")

if __name__ == "__main__":
    build_module()
