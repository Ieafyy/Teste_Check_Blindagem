import cherrypy
import pyfirmata
import webbrowser

class checagem_blindagem(object):
    
    start = 0
    
    @cherrypy.expose
    def index(self, **params):
         
        if checagem_blindagem.start == 0:

            self.placas = ['', '', '', '']
            self.valores_invalidos = ['', ' ', '0', 'None']
            self.placas_status = ['', '', '', '']
            self.arduino = pyfirmata.Arduino("COM3")
            self.it = pyfirmata.util.Iterator(self.arduino)
            self.it.start()

            self.arduino.digital[7].mode = pyfirmata.INPUT
            self.arduino.digital[8].mode = pyfirmata.INPUT
            self.arduino.digital[9].mode = pyfirmata.INPUT
            self.arduino.digital[10].mode = pyfirmata.INPUT
        
            checagem_blindagem.start = 1

        return open("index.html")
    
    @cherrypy.expose
    def checagem(self, *args, **params):
 
        stl_status = ['', '', '', '']
        txt_placas = ['', '', '', '']

        if self.placas[0] == "":
            self.placas[0] = cherrypy.request.params.get("placa_1")
        if self.placas[1] == "":
            self.placas[1] = cherrypy.request.params.get("placa_2")
        if self.placas[2] == "":
            self.placas[2] = cherrypy.request.params.get("placa_3")
        if self.placas[3] == "":
            self.placas[3] = cherrypy.request.params.get("placa_4")

        p1_style = "display:block;"
        p2_style = "display:block;"
        p3_style = "display:block;"
        p4_style = "display:block;"
        
        self.placas_status[0] = self.arduino.digital[7].read()
        self.placas_status[1] = self.arduino.digital[8].read()
        self.placas_status[2] = self.arduino.digital[9].read()
        self.placas_status[3] = self.arduino.digital[10].read()


        print(self.placas_status[0])

        i = 0

        for i in range(len(stl_status)):
            if self.placas_status[i] == True:
                stl_status[i] = "background-color:green;"
                txt_placas[i] = "APROVADO"
            else:
                stl_status[i] = "background-color:red;"
                txt_placas[i] = "REPROVADO"

        if str(self.placas[0]) == "0" or str(self.placas[0]) == "" or str(self.placas[0]) == "None":
            p1_style = "display:none;"
        if str(self.placas[1]) == "0" or str(self.placas[1]) == "" or str(self.placas[1]) == "None":
            p2_style = "display:none;"
        if str(self.placas[2]) == "0" or str(self.placas[2]) == "" or str(self.placas[2]) == "None":
            p3_style = "display:none;"
        if str(self.placas[3]) == "0" or str(self.placas[3]) == "" or str(self.placas[3]) == "None":
            p4_style = "display:none;"

        return open("pagina2.html").read().format(p1_style=p1_style, p2_style=p2_style, p3_style=p3_style, p4_style=p4_style, placa_1=self.placas[0], placa_2=self.placas[1], placa_3=self.placas[2], placa_4=self.placas[3], placa_1_status=txt_placas[0], placa_2_status=txt_placas[1], placa_3_status=txt_placas[2], placa_4_status=txt_placas[3], p1_status_style = stl_status[0], p2_status_style = stl_status[1], p3_status_style = stl_status[2], p4_status_style = stl_status[3])
 

    @cherrypy.expose
    def aprovar(self, *args, **params):

        relatorio = open('relatorio.txt', 'w')
        if str(self.placas[0]) not in self.valores_invalidos:
            if self.placas_status[0]:
                relatorio.write(str(self.placas[0]) + " -> APROVADO\n")
            else:
                relatorio.write(str(self.placas[0]) + " -> REPROVADO\n")

        if str(self.placas[1]) not in self.valores_invalidos:
            if self.placas_status[1]:
                relatorio.write(str(self.placas[1]) + " -> APROVADO\n")
            else:
                relatorio.write(str(self.placas[1]) + " -> REPROVADO\n")
        
        if str(self.placas[2]) not in self.valores_invalidos:
            if self.placas_status[2]:
                relatorio.write(str(self.placas[2]) + " -> APROVADO\n")
            else:
                relatorio.write(str(self.placas[2]) + " -> REPROVADO\n")

        if str(self.placas[3]) not in self.valores_invalidos:
            if self.placas_status[3]:
                relatorio.write(str(self.placas[3]) + " -> APROVADO\n")
            else:
                relatorio.write(str(self.placas[3]) + " -> REPROVADO\n")

        relatorio.close()

        i = 0

        for i in range(len(self.placas)):
            self.placas[i] = ""
            self.placas_status[i] = ""

        return open("pagina3.html")

 
cherrypy.config.update(
    {'server.socket_host': '0.0.0.0',
    'tools.encode.encoding': 'utf-8'} )

#webbrowser.open("http://127.0.0.1:8080")
cherrypy.quickstart(checagem_blindagem())
