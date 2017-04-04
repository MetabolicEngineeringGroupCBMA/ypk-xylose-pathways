#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pathlib

import nbformat
from nbconvert.preprocessors.execute import ExecutePreprocessor

thisdir = os.path.dirname(os.path.realpath(__file__))

for dirpath, dirnames, filenames in os.walk(thisdir):
    if dirpath.startswith(('.','_')): continue
    for file_ in filenames:
        if not file_.endswith(".ipynb"): continue
        p = pathlib.Path(os.path.join(dirpath, file_))
        if any( [f for f in p.parts if f.startswith(("_","."))] ): continue    
        os.chdir(dirpath)
        
        nb = nbformat.read(file_, as_version=4)        
        pp = ExecutePreprocessor(timeout=120, kernel_name='python3')
        pp.interrupt_on_timeout = True        
        pp.preprocess(nb, resources={})
        nbformat.write(nb, file_)
        
        #cmd = "jupyter nbconvert --execute --inplace {}".format(file_)
        #print(cmd)
        #pr = subprocess.run(cmd.split())
        #if pr.returncode:
        #    p.rename(p.with_name("ERROR_"+p.name))
print("run_all.py finished.")