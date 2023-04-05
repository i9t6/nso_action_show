# nso_action_show

Se require instalar textfsm en python 
pip install textfsm 


ncs-make-package --service-skeleton python --action-example show_action

y luego remplazar el show_action.yang y main.py con los archivos anexos.

En Python estoy usanto textFSM, para esto tengo un directorio "templates" donde están los archivo "index" y "sh_ip_route.template".

En el main.py está el path completo, en mi caso '/home/cisco/ncs-run/templates' esto hace el parsing particularmente para el "show ip route", otros show regresa la salida de cli


cisco@u22:~/ncs-run$ ls -l
total 56
drwxrwxr-x 2 cisco cisco 4096 Apr  5 01:09 logs
-rw-rw-r-- 1 cisco cisco 3572 Apr  4 03:23 Makefile
drwxrwxr-x 2 cisco cisco 4096 Apr  5 01:09 ncs-cdb
-rw-rw-r-- 1 cisco cisco 9906 Apr  4 03:04 ncs.conf
drwxrwxr-x 7 cisco cisco 4096 Apr  4 23:40 netsim
drwxrwxr-x 4 cisco cisco 4096 Apr  5 00:54 packages
-rw-rw-r-- 1 cisco cisco  908 Apr  4 03:04 README.ncs
drwxrwxr-x 4 cisco cisco 4096 Apr  4 03:04 scripts
drwxrwxr-x 5 cisco cisco 4096 Apr  5 01:09 state
-rw-rw-r-- 1 cisco cisco  311 Apr  4 23:42 storedstate
drwxrwxr-x 3 cisco cisco 4096 Apr  4 03:07 target
drwxrwxr-x 2 cisco cisco 4096 Apr  5 01:05 templates
cisco@u22:~/ncs-run$ ls -l templates/
total 8
-rw-rw-r-- 1 cisco cisco  349 Apr  5 01:02 index
-rw-rw-r-- 1 cisco cisco 2360 Apr  5 01:02 sh_ip_route.template
