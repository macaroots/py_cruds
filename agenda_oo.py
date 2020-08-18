import tkinter as tk

class Controlador:
	def __init__(self):
		
		self.menuView = MenuGUI(self)
		self.formView = FormGUI(self, self.menuView)
		self.listaView = ListaTextView(self)
		
		'''
		self.listaView = ListaGUI(self, self.menuView)
		self.menuView = MenuTextView(self)
		self.formView = FormTextView(self)
		
		self.formView = FormGUI(self)
		self.listaView = ListaGUI(self)
		
		
		self.menuView = MenuTextView(self)
		root = tk.Tk()
		self.formView = FormGUI(self, root)
		self.listaView = ListaGUI(self, root)
		'''
		self.crud = Crud()
		return self.menu()
		
	def menu(self):
		return self.menuView.render()
		
	def formCadastrar(self):
		return self.formView.render()
		
	def inserir(self, pessoa):
		self.crud.inserir(pessoa)
		return self.listar()
		
	def formEditar(self, id):
		pass
		
	def listar(self):
		pessoas = self.crud.listar()
		self.listaView.attributes.pessoas = pessoas
		return self.listaView.render()
		
	def formLogin(self):
		pass
	def login(self):
		pass
	def sair(self):
		exit()

class Pessoa:
	def __init__(self, nome='', telefone=''):
		self.nome = nome
		self.telefone = telefone
		
class Crud:
	def __init__(self):
		self.pessoas = []
	def inserir(self, pessoa):
		self.pessoas.append(pessoa)
	def listar(self):
		return self.pessoas

class View:
	def __init__(self, controlador, **args):
		self.controlador = controlador
		self.attributes = Pessoa()
		
		super().__init__(**args)
		
class GUI(View, tk.Frame):
	def __init__(self, controlador, master=None):
		if master == None:
			master = tk.Tk()
		super().__init__(controlador, master=master)
		self.pack()	
		
class MenuTextView (View):
	def render(self):
		while True:
			print('1. Cadastrar')
			print('2. Listar')
			print('3. Sair')
			
			opcao = int(input())
			if opcao == 1: 
				self.controlador.formCadastrar()
			elif opcao == 2:
				self.controlador.listar()
			elif opcao == 3:
				self.controlador.sair()
		
class FormTextView (View):
	def render(self):
		pessoa = Pessoa()
		pessoa.nome = input('Nome: ')
		pessoa.telefone = input('Telefone: ')
		self.controlador.inserir(pessoa)

class ListaTextView(View):
	def render(self):
		pessoas = self.attributes.pessoas
		print('Nome\t\tTelefone')
		for pessoa in pessoas:
			print('{0.nome}\t\t{0.telefone}'.format(pessoa))
	
class FormGUI(GUI):
	def render(self):
		frame = self
        
		lbNome = tk.Label(frame)
		lbNome['text'] = 'Nome: '
		lbNome.pack()
		self.txNome = tk.Entry(frame)
		self.txNome.pack()
		lbTelefone = tk.Label(frame)
		lbTelefone['text'] = 'Telefone: '
		lbTelefone.pack()
		self.txTelefone = tk.Entry(frame)
		self.txTelefone.pack()
		
		btOk = tk.Button(frame)
		btOk['text'] = 'Inserir'
		btOk['command'] = self.inserir
		btOk.pack()
		
		btLista = tk.Button(frame)
		btLista['text'] = 'Listar'
		btLista['command'] = self.controlador.listar
		btLista.pack()
		
	def inserir(self):
		pessoa = Pessoa()
		pessoa.nome = self.txNome.get()
		pessoa.telefone = self.txTelefone.get()
		
		self.controlador.inserir(pessoa)

class ListaGUI(GUI):
	def render(self):
		for widget in self.winfo_children():
			widget.destroy()	
			
		try:
			pessoas = self.attributes.pessoas
		except:
			pessoas = []
		for pessoa in pessoas:
			label = tk.Label(self)
			label['text'] = '{0.nome}\t{0.telefone}'.format(pessoa)
			label.pack()


'''GUI - Graphical User Interface'''
class MenuGUI(GUI):
	def render(self):  
		frame = self
		self.controlador.formCadastrar()
		self.controlador.listar()
		self.mainloop()
