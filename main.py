mememe_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "bir şakaya karşılık cevap",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            }
world = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if world in mememe_dict.keys():
    print(mememe_dict[world])
else:
    print("lütfen başka bir kelime yazınız")
