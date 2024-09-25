#método mio
def pagará (cliente, localidad):
    costo=50
    if cobertura(cliente)=="oro":
        if radioDeCobertura==True:
            return "gratis"
        else:
            return 30
    else:
        if radioDeCobertura==True:
            if usados(cliente)<5:
                return "gratis"
            else:
                return costo
        else:
            return costo+30

#método correcto
def pagará (cliente, localidad):
    tipo_cobertura=cobertura(cliente)
    area=radioDeCobertura(cliente, localidad)
    servicios_usados=usado(cliente)
    costo_base=0
    if tipo_cobertura=="oro" or (tipo_cobertura=="plata" and servicios_usados<5):
        costo_base+=0
    else:
        costo_base+=50
    costo_adicional=0
    if area==True:
        costo_adicional+=0
    else:
        costo_adicional+=30
    costo_final=costo_base*costo_adicional
    return costo_final

#otro método
def pagará (cliente, localidad):
    cobro=0
    if cobertura(cliente)=="plata":
        if usados(cliente)>5:
            if radioDeCobertura(cliente, localidad)==True:
                cobro+=50
            else:
                cobro+=80
        else:
            if radioDeCobertura(cliente, localidad)==False:
                cobro+=30
    else:
        if radioDeCobertura(cliente, localidad)==False:
            costo+=30
    return costo

#otro método
def pagará ():
    costoInicial=0
    if radioDeCobertura(cliente, localidad):
        if cobertura(cliente)=="plata":
            if usados(cliente)>5:
                costoInicial=50
    else:
        if cobertura(cliente)=="plata":
            if usados>50:
                costoInicial=80
        else:
            costoInicial=30