def obtener_respuesta(palabra_clave):
    respuestas = {
        "horario": "Nuestro horario de atención es de lunes a viernes de 08h00 a 17h00.",
        "precio": "El precio depende del servicio solicitado. Puede contactarnos para más información.",
        "inscripción": "Para inscribirse debe enviar sus datos personales y comprobante de pago.",
        "certificado": "Los certificados se entregan una vez finalizado el proceso correspondiente.",
        "contacto": "Puede comunicarse con nosotros por correo electrónico o WhatsApp."
    }

    palabra_clave = palabra_clave.lower().strip()

    return respuestas.get(
        palabra_clave,
        "No se encontró una respuesta para esa consulta."
    )

if __name__ == "__main__":
    consulta = input("Ingrese una consulta: ")
    print(obtener_respuesta(consulta))