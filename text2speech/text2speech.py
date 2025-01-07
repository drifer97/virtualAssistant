from  gtts import gTTS
    
text_to_say = "Somos o que fazemos, mas somos, principalmente, o que fazemos para mudar o que somos."

language = 'pt-br'

gtts_object = gTTS(text=text_to_say, lang=language, slow=False)


gtts_object.save("Nas_veias_abertas_da_America_Latina.mp3")