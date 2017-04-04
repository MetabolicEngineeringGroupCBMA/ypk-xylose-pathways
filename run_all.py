#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
import pathlib

thisdir = os.path.dirname(os.path.realpath(__file__))

for dirpath, dirnames, filenames in os.walk(thisdir):
    if dirpath.startswith(('.','_')): continue
    for file_ in filenames:
        if not file_=="pYPK5.ipynb": continue #################################
        if not file_.endswith(".ipynb"): continue
        p = pathlib.Path(os.path.join(dirpath, file_))
        if any( [f for f in p.parts if f.startswith(("_","."))] ): continue    
        os.chdir(dirpath)
        cmd = "jupyter nbconvert --execute --inplace {}".format(file_)
        print(cmd)
        pr = subprocess.run(cmd.split())
        if pr.returncode:
            p.rename(p.with_name("ERROR_"+p.name))
print("run_all.py finished.")