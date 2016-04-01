#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from time import strftime
from collections import Counter

archivo = file('README', 'r').read();
fichas  = re.findall('Fichas\s]=*(.*)==\[.*', archivo, re.S);
tipos   = re.findall('Tipo:\s*(.*)', fichas[0]);

empresas = organismos = universidades = otros = 0;
for tipo in tipos:
    if tipo == 'empresa':
       empresas += 1
    elif tipo == 'organismo':
       organismos += 1
    elif tipo == 'universidad':
       universidades += 1
    else:
       otros += 1

print "Total: " + str(empresas+organismos+universidades) + "\n"
file("stats.txt", 'w').write("Total: " + str(empresas+organismos+universidades) + "\n\n");
print "Por tipo:"
file("stats.txt", 'a').write("Por tipo:\n");
print "* Empresas:      " + str(empresas)
file("stats.txt", 'a').write("* Empresas:      " + str(empresas) + "\n");
print "* Organismos:    " + str(organismos)
file("stats.txt", 'a').write("* Organismos:    " + str(organismos) + "\n");
print "* Universidades: " + str(universidades)
file("stats.txt", 'a').write("* Universidades: " + str(universidades) + "\n");
if otros > 0:
   print "Otros:           " + str(otros)
   file("stats.txt", 'a').write("Otros:      " + str(otros) + "\n");

print "\nPor provincia:"
file("stats.txt", 'a').write("\nPor provincia:\n");
provincias = re.findall('Ubicación:\s*([\w\sáéíóú\/]*)\s', fichas[0]);
provincias = Counter(provincias)
for key in sorted(provincias):
    print "* %-20s: %3s" % (key, str(provincias[key]))
    file("stats.txt", 'a').write("* %-20s: %3s\n" % (key, str(provincias[key])));

file("stats.txt", 'a').write(strftime("\nActualizado: %d-%m-%Y %H:%M:%S\n"));
