def _upd_tickets(ticket):
    _new_name = input('Ingrese Nombre del Pasajero: ')
    _new_last_name = input('Ingrese Apellido del Pasajero: ')
    _new_dni = input('Ingrese DNI del Pasajero: ')

    ticket['name'] = _new_name
    ticket['last_name'] = _new_last_name
    ticket['dni'] = _new_dni

    return ticket
    