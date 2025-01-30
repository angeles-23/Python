# Almacena la siguiente información sobre los álbumes más vendidos en los años 90 en una lista de diccionarios (menos mal que no existía el Reggaeton):
# Recuerda que cada álbum es un diccionario.
# (Artista o grupo, álbum, unidades vendidas y país del artista)

# 1993 Gloria Estefan Mi tierra 1.000.000  Cuba
# 1993 Laura Pausini Laura Pausini 1.350.000  Italia
# 1991 Juan Luis Guerra Bachata Rosa 700.000  República Dominicana
# 2002 Operación Triunfo Álbum 1.200.000  España
# 1996 Spice Girls Spice 1.000.000  Reino Unido
# 2000 La Oreja de Van Gogh El viaje de Copperpot 1.100.000  España
# 1991 Mecano Aidalai 1.000.000  España
# 1997 Luis Miguel Romances 800.000  México
# 2000 Alejandro Sanz El alma al aire 1.300.000  España
# 2002 David Bisbal Corazón latino 1.300.000  España
# 1985 Rocío Jurado Paloma Brava 700.000  España
# 1997 Alejandro Sanz Más 2.200.000  España
# 1990 Julio Iglesias Raíces 1.100.000  España
# 1996 Rosana Lunas Rotas 1.100.000  España
# 1998 Chayanne Atado a tu amor 1.000.000  Puerto Rico
# 1993 Abba ABBA Gold 800.000  Suecia
# 2001 Álex Ubago ¿Qué pides tú? 900.000  España
# 1988 Mecano Descanso Dominical 1.100.000  España
# 2002 Amaral Estrella de mar 800.000  España
# 1991 Alejandro Sanz Viviendo deprisa 800.000  España
# 1995 Alejandro Sanz 3 800.000  España
# 1997 Backstreet Boys Backstreet's Back 800.000  Reino Unido
# 1996 Ella baila sola Ella baila sola 700.000  España
# 1999 Estopa Estopa  1.100.000  España
# 1997 Mónica Naranjo Palabra de Mujer 1.000.000  España
# 1981 Julio Iglesias De niña a mujer 700.000  España
# 1982 Michael Jackson Thriller 700.000  Estados Unidos
# 1989 Phil Collins ...But Seriously 700.000  Reino Unido
# 1979 Rocío Jurado Señora 900.000  España
# 2003 Alejandro Sanz No es lo mismo 800.000  España
# 2004 David Bisbal Bulería 1.000.000  España


albumes = [
    {"year":1993, "artista":"Gloria Estefan", "album":"Mi tierra", "sold": 1000000, "county": "Cuba"},
    {"year":1993, "artista":"Laura Pausini", "album":"Laura Pausini", "sold": 1350000, "county":"Italia"},
    {"year":1991, "artista":"Juan Luis", "album":"Guerra Bachata Rosa", "sold": 700.000, "county":"República Dominicana"},
    {"year":2002, "artista":"Operación Triunfo", "album":"Álbum", "sold": 1200000, "county":"España"},
    {"year":1996, "artista":"Spice Girls", "album":"Spice", "sold": 1000000, "county":"Reino Unido"},
    {"year":2000, "artista":"La Oreja de Van Gogh ","album": "El viaje de Copperpot", "sold": 1100000, "county":"España"},
    {"year":1991, "artista":"Mecano", "album":"Aidalai", "sold": 1000000, "county":"España"},
    {"year":1997, "artista":"Luis Miguel", "album":"Romances", "sold": 800.000, "county":"México"},
    {"year":2000, "artista":"Alejandro Sanz", "album":"El alma al aire", "sold": 1300000, "county":"España"},
    {"year":2002, "artista":"David Bisbal", "album":"Corazón latino", "sold": 1300000, "county":"España"},
    {"year":1985, "artista":"Rocío Jurado", "album":"Paloma Brava", "sold": 700.000, "county":"España"},
    {"year":1997, "artista":"Alejandro Sanz", "album":"Más", "sold": 2200000, "county":"España"},
    {"year":1990, "artista":"Julio Iglesias", "album":"Raíces", "sold": 1.00000, "county":"España"},
    {"year":1996, "artista":"Rosana Lunas", "album":"Rotas", "sold": 1100000, "county":"España"},
    {"year":1998, "artista":"Chayanne Atado", "album":"a tu amor", "sold": 1000000, "county":"Puerto Rico"},
    {"year":1993, "artista":"Abba ABBA", "album":"Gold", "sold": 800.000, "county":"Suecia"},
    {"year":2001, "artista":"Álex Ubago", "album":"¿Qué pides tú?", "sold": 900.000, "county":"España"},
    {"year":1988, "artista":"Mecano Descanso", "album":"Dominical", "sold": 1100000, "county":"España"},
    {"year":2002, "artista":"Amaral", "album":"Estrella de mar", "sold": 800.000, "county":"España"},
    {"year":1991, "artista":"Alejandro Sanz", "album":"Viviendo deprisa", "sold": 800.000, "county":"España"},
    {"year":1995, "artista":"Alejandro Sanz", "album":"3", "sold": 800.000, "county":"España"},
    {"year":1997, "artista":"Backstreet Boys", "album":"Backstreet's Back", "sold": 800000, "county":"Reino Unido"},
    {"year":1996, "artista":"Ella baila sola", "album":"Ella baila sola", "sold": 700000, "county":"España"},
    {"year":1999, "artista":"Estopa", "album":"Estopa", "sold": 1100000, "county":"España"},
    {"year":1997, "artista":"Mónica Naranjo", "album":"Palabra de Mujer", "sold": 1000000, "county":"España"},
    {"year":1981, "artista":"Julio Iglesias", "album":"De niña a mujer", "sold": 700.000, "county":"España"},
    {"year":1982, "artista":"Michael Jackson", "album":"Thriller", "sold": 700.000, "county":"Estados Unidos"},
    {"year":1989, "artista":"Phil Collins", "album":"...But Seriously", "sold": 700.000, "county":"Reino Unido"},
    {"year":1979, "artista":"Rocío Jurado", "album":"Señora", "sold": 900.000, "county":"España"},
    {"year":2003, "artista":"Alejandro Sanz", "album":"No es lo mismo", "sold": 800.000, "county":"España"},
    {"year":2004, "artista":"David Bisbal", "album":"Bulería", "sold": 1000000, "county":"España"}
]