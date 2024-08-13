def parse_data(data):
    # Este es un ejemplo sencillo de cómo podrías analizar datos.
    # Dependiendo de la estructura de los datos, puedes adaptar este método.
    parsed_data = []
    for item in data:
        parsed_data.append({
            "name": item["name"],
            "value": item["value"]
        })
    return parsed_data
