from datetime import datetime

def _get_menu():
    print('\n\n\n')
    print('                          +========================================+')
    print('                          |                  MENU                  |')
    print('                          +========================================+')
    print('                          |   1.- LISTAR RUTAS/DISTINOS            |')
    print('                          |   2.- LISTAR PASAJES - RESERVAS        |')
    print('                          |   3.- NUEVO PASAJE                     |')
    print('                          |   4.- NUEVO RESERVA                    |')
    print('                          |   5.- MODIFICAR PASAJE - RESERVAS      |')
    print('                          |   6.- ELIMINAR PASAJE                  |')
    print('                          |   7.- SALIR                            |')
    print('                          +========================================+')
    print('\n')


def _get_list_detinity(index=0,isReturn=False):
    now = datetime.now()
    today = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
    lastDay = str(now.day+1) + '/' + str(now.month) + '/' + str(now.year)

    destinitys = [
        ['CHICLAYO','80','20:00','06:00'], 
        ['CIMBOTE','60','19:45','07:00'],
        ['ICA','70','21:30','08:00'],
        ['PAITA','90','22:15','09:00'],
        ['PIURA','100','23:15','05:00'],
        ['SULLANA','80','20:00','07:00'],
        ['TALARA','70','17:00','06:00'],
        ['TRUJILLO','100','20:30','06:00']
    ]

    if isReturn != False:
        return destinitys[index-1]

    print('                    +=============================================================================+')
    print('                    |                             DESTINOS DESDE LIMA                             |')
    print('                    +=============================================================================+')
    print('                    |  OP  |  DESTINO            |  PRECIO  |       SALIDA      |     LLEGADA     |')
    print('                    +=============================================================================+')

    for i in range(len(destinitys)):
        if (index-1) != i:
            print('                    {0}{1:5} {0} {2:19} {0} S/.{3:5} {0} {4:10} {5:5} {0} {6:10} {7:5} |'.format('|',i+1, destinitys[i][0],destinitys[i][1],today,destinitys[i][2],lastDay,destinitys[i][3]))
    print('                    +=============================================================================+')

def _get_list_seat(index=0,isReturn=False):
    print('                                        +=========================+')
    print('                                        |   ASIENTOS DISPONIBLES  |')
    print('                                        +=========================+')
    print('                                        | FA | FB | --- | FC | FD |')
    print('                                        +_________________________+')
    print('                                        | 01 | 02 | --- | 03 | 04 |')
    print('                                        | 05 | 06 | --- | 07 | 08 |')
    print('                                        | 09 | 10 | ---           |')
    print('                                        | 11 | 12 | --- | 13 | 14 |')
    print('                                        | 15 | 16 | --- | 17 | 18 |')
    print('                                        | 19 | 20 | --- | 21 | 22 |')
    print('                                        | 23 | 24 | --- | 25 | 26 |')
    print('                                        | 27 | 28 | --- | 29 | 30 |')
    print('                                        | 31 | 32 | --- | 33 | 34 |')
    print('                                        | 35 | 36 | --- | 37 | 38 |')
    print('                                        +=========================+')

