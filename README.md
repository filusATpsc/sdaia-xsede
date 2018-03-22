Fork of SDAIA Project for use by XSEDE 
=======================================

GIT: https://git.ncsa.illinois.edu/awithers/sdaia
CICI: Secure Data Architecture: Shared Intelligence Platform for Protecting our National Cyberinfrastructure
ACI Award Number:1547249

-----------------------

Ansible roles found in site.yml.  Comment out roles not needed.

  - To build a "consumer-only" appliance, comment out "honeynet".

You can run `install.sh`, which requires and runs Ansible locally. Or deploy using your own Ansible instance via SSH. Install requires root.

Deploys SDAIA software on Ubuntu 16 and CentOS 7 (beta).

Report bugs to filus@psc.edu
