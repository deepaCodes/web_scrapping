import pyodbc

print(pyodbc.version)
print('available drivers: {}'.format(pyodbc.drivers()))