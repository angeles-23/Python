import os
os.system('cls')

lenguajes = {
    'ja': 'Java',
    'sql': 'SQL',
    'py': 'Python',
    'ht': 'HTML',
    'xm': 'XML',
    'cs': 'CSS',
    'jv': 'JavaScript',        
    'md': 'MarkDown'    
}

# Añadir valores al diccionario
lenguajes['ph'] = 'PHP'
# Alterar valores al diccionario
lenguajes['ht'] = 'html'

# Imprimir diccionarios
print(f'Vamos a adquirir unas nociones de {lenguajes['py']}')

print(lenguajes)
print(lenguajes.keys())
print(lenguajes.values())

print(lenguajes)