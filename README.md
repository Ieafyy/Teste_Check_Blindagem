# Teste_Check_Blindagem
Sistema desenvolvido por mim para realizar a validação de placas de produção

O sistema foi criado com a finalidade de ser utilzado na linha de produção e tem a função de checar se as placas em questão estão montadas corretamente. A 
lógica foi escrita em Python, a interface foi criada em HTML/CSS (Tailwind CSS) e o hardware comunica com o software a partir de um Arduino Leonardo.

<h2> Analisando o Software </h2>

![image](https://user-images.githubusercontent.com/70926962/172070865-f9d60f3c-8448-4dd1-8df9-d66bdc0cf51e.png)

Inicialmente o testador precisará escanear o QR Code presente em cada placa, esse código é único e cada placa possui o seu. O Hardware (como mostrarei mais pra
frente) foi montado de maneira a testar até 4 placas simultâneas, porém caso o teste seja realizado com menor quantidade de placas, basta entrar com o valor 0
ou então deixar o campo em branco.

![image](https://user-images.githubusercontent.com/70926962/172071025-c80ada75-df8a-4fce-92ac-4d9c744cf00e.png)

Neste exemplo, dei os nomes PCB01, PCB02 e PCB03 para as placas, além de não querer testar a placa 4. Aqui o sistema se comunica com o hardware para ler os
sensores conectados nas entradas do Arduino. 

![image](https://user-images.githubusercontent.com/70926962/172071124-e6ccf597-e430-4bc0-ba1f-5dccff170056.png)

(Ativando todos os sensores -> Todas as placas foram aprovadas)

![image](https://user-images.githubusercontent.com/70926962/172071150-1e40fba5-44c7-4831-b21e-e748653ae1ef.png)

(Sensores 1 e 3 não foram ativados -> apenas a placa 2 passou no teste)

Após posicionar todas as placas e ver os resultados, é preciso gerar o relátorio. Aqui o sistema gerará um .txt no formato específico para outro sistema
ler. Devido a sigilo industrial, nesse exemplo o arquivo .txt será gerado apenas de forma genérica, com o código da placa e o resultado desta no teste. 

![image](https://user-images.githubusercontent.com/70926962/172071384-83b6e101-3a8c-48d4-8710-b372c845e6fe.png)

(Teste completo)

![image](https://user-images.githubusercontent.com/70926962/172071748-0b28b37a-5e06-4a7f-a491-26ec157e2f0c.png)

(Resultados do teste)
