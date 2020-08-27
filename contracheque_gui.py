import tkinter as tk

# visão substituta para o receber_dados()
class FormGUI(tk.Frame):
	def render(self):
		frame = self
		frame.pack()	
		
		lbValorHora = tk.Label(frame)
		lbValorHora['text'] = 'Valor por hora: '
		lbValorHora.pack()
		self.txValorHora = tk.Entry(frame)
		self.txValorHora.pack()
		lbHoras = tk.Label(frame)
		lbHoras['text'] = 'Horas trabalhadas: '
		lbHoras.pack()
		self.txHoras = tk.Entry(frame)
		self.txHoras.pack()
		
		btOk = tk.Button(frame)
		btOk['text'] = 'Mostrar contracheque'
		btOk['command'] = self.mostraClick
		btOk.pack()
				
		frame.mainloop()
	
	def mostraClick(self):
		valor_hora = float(self.txValorHora.get())
		horas_trabalhadas = int(self.txHoras.get())

		controla_contracheque(valor_hora, horas_trabalhadas)

# visão
def receber_dados():
	print('Qual o valor ganho por hora?')
	valor_hora = float(input())
	print('Quantas horas foram trabalhadas?')
	horas_trabalhadas = int(input())

	controla_contracheque(valor_hora, horas_trabalhadas)
	
# modelo
def calcula_salario_bruto(valor_hora, horas_trabalhadas):
	return valor_hora * horas_trabalhadas

# modelo	
def porcentagem(valor, percentual):
	porcento = valor * percentual / 100
	return porcento

# controle
def controla_contracheque(valor_hora, horas_trabalhadas):
	salario_bruto = calcula_salario_bruto(valor_hora, horas_trabalhadas)
	imposto_renda = porcentagem(salario_bruto, 11)
	inss = porcentagem(salario_bruto, 8)
	sindicato = porcentagem(salario_bruto, 5)
	salario_liquido = salario_bruto - imposto_renda - inss - sindicato

	exibe_contracheque(salario_bruto, imposto_renda, inss, sindicato, salario_liquido)

# visão
def exibe_contracheque(salario_bruto, imposto_renda, inss, sindicato, salario_liquido):
    print('''+ Salário Bruto : R$ {:.2f}
- IR (11%) : R$ {:.2f}
- INSS (8%) : R$ {:.2f}
- Sindicato ( 5%) : R$ {:.2f}
= Salário Liquido : R$ {:.2f}'''.format(salario_bruto, imposto_renda, inss, sindicato, salario_liquido))

# controle
#receber_dados()
FormGUI().render()