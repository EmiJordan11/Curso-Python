estilo = {
    "reset": "\033[0m",
    "negrita": "\033[1m",
    "subrayado": "\033[4m",
    "negro": "\033[30m",
    "rojo": "\033[31m",
    "verde": "\033[32m",
    "amarillo": "\033[33m",
    "naranja": "\033[38;5;208m",
    "azul": "\033[94m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "blanco": "\033[37m",
    "fondo_negro": "\033[40m",
    "fondo_rojo": "\033[41m",
    "fondo_verde": "\033[42m",
    "fondo_amarillo": "\033[43m",
    "fondo_azul": "\033[44m",
    "fondo_magenta": "\033[45m",
    "fondo_cyan": "\033[46m",
    "fondo_blanco": "\033[47m"
}

def titulo(cadena):
    return f'{{}}{{}}{{}}{cadena}{{}}'.format(estilo['subrayado'],estilo['negrita'],estilo['verde'],estilo['reset'])

def subtitulo(cadena):
    return f'{{}}{{}}{cadena}{{}}'.format(estilo['negrita'],estilo['naranja'],estilo['reset'])

def azul(cadena):
    return f'{{}}{cadena}{{}}'.format(estilo['azul'],estilo['reset'])

def datos(cadena):
    return f'{{}}{cadena}{{}} '.format(estilo['subrayado'], estilo['reset'])

def error(cadena):
    return f'{{}}{{}}{cadena}{{}}'.format(estilo['fondo_rojo'],estilo['negro'],estilo['reset'])