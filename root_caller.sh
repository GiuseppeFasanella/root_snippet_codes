#! /bin/bash
#prepara macro.C che fa quello che vuoi tu
root -l -b macro_caller.C
#macro_caller.C e' organizzato cosi':
```
##questa e' macro_caller.C
{
gROOT->ProcessLine(".L macro.C+");
MyFunction("args");
gROOT->ProcessLine(".q");
}
```
