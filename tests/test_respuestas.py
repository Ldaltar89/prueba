from src.respuestas import obtener_respuesta

def test_respuesta_horario():
    assert obtener_respuesta("horario") == "Nuestro horario de atención es de lunes a viernes de 08h00 a 17h00."

def test_respuesta_precio():
    assert obtener_respuesta("precio") == "El precio depende del servicio solicitado. Puede contactarnos para más información."

def test_respuesta_no_existe():
    assert obtener_respuesta("beca") == "No se encontró una respuesta para esa consulta."

def test_respuesta_con_mayusculas():
    assert obtener_respuesta("HORARIO") == "Nuestro horario de atención es de lunes a viernes de 08h00 a 17h00."