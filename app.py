import menu
import tickets.list_tickets
import tickets.add_tickets
import tickets.upd_tickets
data = []

while True:
    menu._get_menu()
    option = input('                                Ingrese una opción:')
    if option == '1':
        menu._get_list_detinity()
        input('Presione enter para continuar...')
    elif option == '2':
        tickets.list_tickets._list_ticket(data)
        input('Presione enter para continuar...')
    elif option == '3':
        menu._get_list_detinity()
        id_destinity = int(input('                                          Ingrese el destino:'))
        destinity = menu._get_list_detinity(id_destinity,True)
        menu._get_list_seat()
        id_seat = input('                                          Ingrese el asiento:')
        data.append(tickets.add_tickets._add_tickets(len(data) + 1,'PASAJE',destinity,id_seat))
        input('Presione enter para continuar...')
    elif option == '4':
        menu._get_list_detinity()
        id_destinity = int(input('                                          Ingrese el destino:'))
        destinity = menu._get_list_detinity(id_destinity,True)
        menu._get_list_seat()
        id_seat = input('                                          Ingrese el asiento:')
        data.append(tickets.add_tickets._add_tickets(len(data) + 1,'PAQUETE',destinity,id_seat))
        input('Presione enter para continuar...')
    elif option == '5':
        tickets.list_tickets._list_ticket(data)
        code = input('Ingrese el codigo del pasage: ')
        for i in range(len(data)):
            if data[i]['code'] == code:
                data[i] = tickets.upd_tickets._upd_tickets(data[i])
                break

        input('Presione enter para continuar...')
    elif option == '6':
        tickets.list_tickets._list_ticket(data)
        code = input('Ingrese el codigo del pasage: ')
        for i in range(len(data)):
            if data[i]['code'] == code:
                data[i]['status'] = False
                break
        print('                       ELIMINADO')
    elif option == '7':
        print('                       GRACIAS POR USAR NUESTRO SISTEMA...!!! 😊❤')
        break
