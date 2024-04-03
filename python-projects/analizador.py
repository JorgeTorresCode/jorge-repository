import openai

openai.api_key = "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"
system_rol = """Haz de cuenta que eres un analizador de sentimientos.
Yo te paso mensajes y tu analizas el sentimiento de los mensajes y me das una respuesta
con al menos 1 caracter y como maximo 4 caracteres. SOLO RESPUESTAS NUMÉRICAS donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
Puedes ir entre esos rangos, es decir 0.3, -0.5, etc también son válidos
(Solo puedes responder con ints o floats)
Reitero, UNICAMENTE RESPUESTAS NUMÉRICAS"""

mensajes = [{"role": "system", "content": system_rol}]


class Sentimiento:
    
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return "\x1b[1;{}m{}\n\x1b[0;37m".format(self.color, self.nombre)


class AnalizadorDeSentimientos:
    
    def __init__(self, rangos):
        self.rangos = rangos
    
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <=rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")
        
rangos = [
    ((-0.7, -0.4), Sentimiento("Negativo","31")),
    ((-0.4, -0.2), Sentimiento("Algo negativo","31")),
    ((-0.2, 0.1), Sentimiento("Neutral","33")),
    ((0.2, 0.4), Sentimiento("Algo positivo","32")),
    ((0.4, 0.7), Sentimiento("Positivo","32")),
    ((0.7, 1), Sentimiento("Muy positivo","32"))
]

        
analizador = AnalizadorDeSentimientos(rangos)
print("\nPuedo saber que tan positivo o negativo es tu comentario")

while True:
    user_prompt = input("Dime algo: ")
    mensajes.append({"role": "user", "content": user_prompt})
    
    completion = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message.content
    mensajes.append({"role": "assistant", "content": respuesta})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)