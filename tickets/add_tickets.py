from datetime import datetime

def _add_tickets(correlative, type_ticket, _destinity, _seat):
        now = datetime.now()
        today = str(now.day) + '/' + str(now.month) + '/' + str(now.year)
        lastDay = str(now.day+1) + '/' + str(now.month) + '/' + str(now.year)


        name = input('Ingrese Nombre del Pasajero: ')
        last_name = input('Ingrese Apellido del Pasajero: ')
        dni = input('Ingrese DNI del Pasajero: ')
        destinity = _destinity[0]
        cost = _destinity[1]
        type_ticket = type_ticket
        seat = _seat
        date_init = today
        hour_init = _destinity[2]
        date_end = lastDay
        hour_end = _destinity[3]

        new_correlative = '{0:04d}'.format(correlative)

        data = {
            'code': new_correlative,
            'name': name,
            'last_name': last_name,
            'dni': dni,
            'destinity': destinity,
            'cost': cost,
            'type_ticket': type_ticket,
            'seat': seat,
            'date_init': date_init,
            'hour_init': hour_init,
            'date_end': date_end,
            'hour_end': hour_end,
            'status': True,
        }
        return data