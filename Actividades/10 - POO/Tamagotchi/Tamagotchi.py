import estilo as es

class Tamagotchi():
    humores= ["enojado 😡", "triste 😞", "indiferente 🙂", "feliz 😀", "eufórico 😁"]
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 5
        self.nivel_felicidad = 50
        self.humor = Tamagotchi.humores[2]
        self.esta_vivo = True
        
    #MOSTRAR ESTADO   
    def mostrar_estado(self):
        print(es.azul(f"Datos de {self.nombre} 📊"))
        print(f"-Energia: {self.nivel_energia}")
        print(f"-Hambre: {self.nivel_hambre}")
        print(f"-Humor: {self.humor}")
        print(f"-Nivel Humor: {self.nivel_felicidad}")
    
    #ALIMENTAR   
    def alimentar(self):
        hambre_previa=self.nivel_hambre
        self.nivel_hambre= self.nivel_hambre - 10 if self.nivel_hambre>10 else 0
        print(es.naranja(f"{self.nombre} ha sido alimentado 🍖🍗!"))
        
        if hambre_previa>10:
            print(f"-Nivel de hambre: {hambre_previa} - 10⬇️  = {self.nivel_hambre}")
        else:
            print(f"-Nivel de hambre: {hambre_previa} - {hambre_previa}⬇️  = {self.nivel_hambre}✅")
        
    #JUGAR    
    def jugar(self):
        situacion= None
        if self.nivel_hambre>=20: #situacion critica
            situacion=0
            energia_previa=self.nivel_energia
            self.nivel_energia=self.nivel_energia - 20 if self.nivel_energia>=20 else 0
            self.nivel_felicidad=self.nivel_felicidad - 30 if self.nivel_felicidad>=30 else 0
        else: #situacion normal
            situacion=1
            energia_previa=self.nivel_energia
            self.nivel_felicidad=self.nivel_felicidad + 20 if self.nivel_felicidad<=80 else 100
            self.nivel_energia=self.nivel_energia - 18 if self.nivel_energia>=18 else 0
        
        hambre_previa=self.nivel_hambre
        self.nivel_hambre=self.nivel_hambre + 10 if self.nivel_hambre<=90 else 100
        
        #verifico si esta vivo
        if self.verificar_estado():    
            self.verificar_humor()
            print(es.amarillo(f"{self.nombre} se ha divertido mucho 😄😄!!"))
            
            #muestro como cambian las estadisticas
            if situacion==0:
                #energia
                if energia_previa>=20:
                    print(f"-Nivel de energia: {energia_previa} - 20⬇️  = {self.nivel_energia}")
                    
            else:
                if energia_previa>=18:
                    print(f"-Nivel de energia: {energia_previa} - 18⬇️  = {self.nivel_energia}") 
                    
            #hambre       
            if hambre_previa<90:
                print(f"-Nivel de hambre: {hambre_previa} + 10⬆️  = {self.nivel_hambre}")
            else:
                print(f"-Nivel de hambre: {hambre_previa} + {100-hambre_previa}⬆️  = {self.nivel_hambre}❗")
            
    
    #DORMIR              
    def dormir(self):
        situacion = None
        if self.nivel_hambre>=20: #situacion critica
            situacion=0
            energia_previa=self.nivel_energia
            self.nivel_energia=self.nivel_energia - 20 if self.nivel_energia>=20 else 0
            self.nivel_felicidad=self.nivel_felicidad - 30 if self.nivel_felicidad>=30 else 0
        else: #situacion normal
            situacion=1
            energia_previa=self.nivel_energia
            self.nivel_energia= self.nivel_energia + 40 if self.nivel_energia<=60 else 100
        
        hambre_previa=self.nivel_hambre
        self.nivel_hambre= self.nivel_hambre + 5 if self.nivel_hambre<=95 else 100
        
        #verifico si esta vivo
        if self.verificar_estado():
            self.verificar_humor()
            print(es.lila(f"{self.nombre} se ha dormido, buenas noches 😴🌙"))
            
            #muestro como cambian las estadisticas
            if situacion==0:
                #energia
                if energia_previa>=20:
                    print(f"-Nivel de energia: {energia_previa} - 20⬇️  = {self.nivel_energia}")
            
            else:
                #energia
                if energia_previa<60:
                    print(f"-Nivel de energia: {self.nivel_energia-40} + 40⬆️  = {self.nivel_energia}")
                
                else:
                    print(f"-Nivel de energia: {energia_previa} + {100-energia_previa}⬆️  = {self.nivel_energia}✅")
            
            #hambre
            if hambre_previa<95:
                print(f"-Nivel de hambre: {hambre_previa} + 5⬆️  = {self.nivel_hambre}")
            else:
                print(f"-Nivel de hambre: {hambre_previa} + {100-hambre_previa}⬆️  = {self.nivel_hambre}❗")

                
            
        
    #para modificar el humor dependiendo del nivel de felicidad (por intervalos de 20)
    def verificar_humor(self):
        if self.nivel_felicidad<=20:
            self.humor= Tamagotchi.humores[0]
        elif self.nivel_felicidad>20 and self.nivel_felicidad<=40:
            self.humor= Tamagotchi.humores[1]
        elif self.nivel_felicidad>40 and self.nivel_felicidad<=60:
            self.humor= Tamagotchi.humores[2]
        elif self.nivel_felicidad>60 and self.nivel_felicidad<=80:
            self.humor= Tamagotchi.humores[3]
        else:
            self.humor= Tamagotchi.humores[4]
    
    #VERIFICAR ESTADO        
    def verificar_estado(self):
        if self.nivel_energia==0:
            self.esta_vivo=False
            print(es.azul(f"😭😭 {self.nombre} ha muerto debido a que ha quedado sin energía 😭😭"))
            quit()
        else:
            return True
            
        


