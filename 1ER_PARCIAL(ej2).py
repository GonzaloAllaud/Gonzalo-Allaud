dinosaurios = [
    {
    "nombre": "Tyrannosaurus Rex",
    "especie": "Theropoda",
    "peso": "7000 kg",
    "descubridor": "Barnum Brown",
    "ano_descubrimiento": 1902
    },
    {
    "nombre": "Triceratops",
    "especie": "Ceratopsidae",
    "peso": "6000 kg",
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1889
    },
    {
    "nombre": "Velociraptor",
    "especie": "Dromaeosauridae",
    "peso": "15 kg",
    "descubridor": "Henry Fairfield Osborn",
    "ano_descubrimiento": 1924
    },
    {
    "nombre": "Brachiosaurus",
    "especie": "Sauropoda",
    "peso": "56000 kg",
    "descubridor": "Elmer S. Riggs",
    "ano_descubrimiento": 1903
    },
    {
    "nombre": "Stegosaurus",
    "especie": "Stegosauridae",
    "peso": "5000 kg",
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1877
    },
    {
    "nombre": "Spinosaurus",
    "especie": "Spinosauridae",
    "peso": "10000 kg",
    "descubridor": "Ernst Stromer",
    "ano_descubrimiento": 1912
    },
    {
    "nombre": "Allosaurus",
    "especie": "Theropoda",
    "peso": "2000 kg",
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1877
    },
    {
    "nombre": "Apatosaurus",
    "especie": "Sauropoda",
    "peso": "23000 kg",
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1877
    },
    {
    "nombre": "Diplodocus",
    "especie": "Sauropoda",
    "peso": "15000 kg",
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1878
    },
    {
    "nombre": "Ankylosaurus",
    "especie": "Ankylosauridae",
    "peso": "6000 kg",
    "descubridor": "Barnum Brown",
    "ano_descubrimiento": 1908
    },
    {
    "nombre": "Parasaurolophus",
    "especie": "Hadrosauridae",
    "peso": "2500 kg",
    "descubridor": "William Parks",
    "ano_descubrimiento": 1922
    },
    {
    "nombre": "Carnotaurus",
    "especie": "Theropoda",
    "peso": "1500 kg",
    "descubridor": "José Bonaparte",
    "ano_descubrimiento": 1985
    },
    {
    "nombre": "Styracosaurus",
    "especie": "Ceratopsidae",
    "peso": "2700 kg",
    "descubridor": "Lawrence Lambe",
    "ano_descubrimiento": 1913
    },
    {
    "nombre": "Therizinosaurus",
    "especie": "Therizinosauridae",
    "peso": "5000 kg",
    "descubridor": "Evgeny Maleev",
    "ano_descubrimiento": 1954
    },
    {
    "nombre": "Pteranodon",
    "especie": "Pterosauria",
    "peso": "25 kg",
    "descubridor": "Othniel Charles Marsh",
    "ano_descubrimiento": 1876
    },
    {
    "nombre": "Quetzalcoatlus",
    "especie": "Pterosauria",
    "peso": "200 kg",
    "descubridor": "Douglas A. Lawson",
    "ano_descubrimiento": 1971
    },
    {
    "nombre": "Plesiosaurus",
    "especie": "Plesiosauria",
    "peso": "450 kg",
    "descubridor": "Mary Anning",
    "ano_descubrimiento": 1824
    },
    {
    "nombre": "Mosasaurus",
    "especie": "Mosasauridae",
    "peso": "15000 kg",
    "descubridor": "William Conybeare",
    "ano_descubrimiento": 1829
    },

]

# NUMERO DE ESPECIES
especies = {dinosaurio["especie"] for dinosaurio in dinosaurios}
cantidad_especies = len(especies)
print(f"Cantidad de especies: {cantidad_especies}")

# NUMERO DE DESCUBRIDORES
descubridores = {dinosaurio["descubridor"] for dinosaurio in dinosaurios}
cantidad_descubridores = len(descubridores)
print(f"Cantidad de descubridores distintos: {cantidad_descubridores}")

# EMPIEZA CON T
dinosaurios_con_T = [dinosaurio for dinosaurio in dinosaurios if dinosaurio["nombre"].startswith("T")]
print("Dinosaurios que empiezan con T:")
for dino in dinosaurios_con_T:
    print(dino["nombre"])

# PESAJE MENOS DE 275KG
dinosaurios_menos_275kg = [dinosaurio for dinosaurio in dinosaurios if int(dinosaurio["peso"].split()[0]) < 275]
print("Dinosaurios que pesan menos de 275 kg:")
for dino in dinosaurios_menos_275kg:
    print(dino["nombre"])

# COMIENZAN CON A, Q, S
pila_AQS = [dinosaurio for dinosaurio in dinosaurios if dinosaurio["nombre"].startswith(("A", "Q", "S"))]
print("Dinosaurios en la pila aparte (comienzan con A, Q, S):")
for dino in pila_AQS:
    print(dino["nombre"])

