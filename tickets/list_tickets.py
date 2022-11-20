def _list_ticket(data):
    print('\n')
    print('+===============================================================REPORTE DE PASAJES==================================================================+')
    print('|  CODIGO  |  NOMBRES            |  APELLIDOS        |    DNI    |  DESTINO  |  COSTO  |  TIPO    | ASIENTO |       SALIDA      |      LLEGADA      |')
    print('+===================================================================================================================================================+')
    for ticket in data:
        if ticket['status'] != True:
            continue
        init = ticket['date_init'] + ' ' + ticket['hour_init']
        end = ticket['date_end'] + ' ' + ticket['hour_end']
        print('{0}  {1:7} {0} {2:19} {0} {3:17} {0} {4:9} {0} {5:9} {0} S/.{6:4} {0} {7:8} {0} {8:7} {0} {9:17} {0} {10:17} {0}'.format(
            '|', ticket['code'], ticket['name'], ticket['last_name'], ticket['dni'], ticket['destinity'],ticket['cost'], ticket['type_ticket'], ticket['seat'], init, end))
    print('+===================================================================================================================================================+')

    # cont = 0
    # if len(data) == 0:
    #     print('No hay pasajes registrados')
    #     cont = 1
        
    for i in range(9-len(data)):
        print('')

    return
