
class DMPA:
	#Параметры грамматики ДМПА
	input_state_list = []
	size_state_int = int(0)
	alphabet_list = []
	stack_alphabet_list = []
	start_state_int = int(0)
	stack_symbol_str = str('Z')
	end_state_int = int(0)
	chain_str = str('')

    #Вспомогательные параметры
	output_str = str('')
	result_checking = False

	stack_dmpa = ''


	def __init__(self, args_list :list):
		if len(args_list) != 8:
			self.error_print('incorrect number of arguments: ' +  str(len(args_list)) + ' != 8')

		self._set_state_list(args_list[0])
		self._set_size_state_int(args_list[1])
		self._set_alphabet_list(args_list[2])
		self._set_stack_alphabet_str(args_list[3])
		self._set_start_state_int(args_list[4])
		self._set_stack_symbol_str(args_list[5])
		self._set_end_state_int(args_list[6])
		self._set_chain_str(args_list[7])


	def _set_state_list(self, state_str :str):
		pass


	def _set_size_state_int(self, size_state_str :str):
		if size_state_str.isdigit():
			self.size_state_int = int(size_state_str)
			return True
		else:
			self.error_print(size_state_str + ' - no digit!')
			return False

    	
	def _set_alphabet_list(self, alphabet_list :str):
		alph = list(set(filter(None, alphabet_list.split(' ')))) 
		
		if len(alph) == 0:
			self.error_print('the alphabet is empty!')
			return False

		for item in alph:
			if len(item) > 1:
				self.error_print(item + ' alphabet character cannot be of length > 1!')
				return False

		self.alphabet_list = alph

		return True


	def _set_stack_alphabet_str(self, stack_alphabet :str):
		pass


	def _set_start_state_int(self, start_state_str :str):
		if start_state_str.isdigit():
			self.start_state_int = int(start_state_str)
			return True
		else:
			self.error_print(start_state_str + ' - no digit!')
			return False

	def _set_stack_symbol_str(self, stack_symbol:str):
		if len(stack_symbol) > 1:
			self.error_print(stack_symbol + ' stack symbol cannot be of length > 1!')
			return False
		
		self.stack_symbol_str = stack_symbol
		return True


	def _set_end_state_int(self, end_state_str :str):
		if len(end_state_str) == 0:
			self.error_print('end state is empty!')
			return False

		if end_state_str.isdigit():
			self.end_state_int = int(end_state_str)
			return True
		else:
			self.error_print(end_state_str + ' - no digit!')
			return False


	def _set_chain_str(self, chain :str):
		chain = chain.replace(' ', '')
		
		if len(chain) == 0:
			self.error_print('chain is empy!')
			return False

		for item in chain:
			if not item in self.alphabet_list:
				self.error_print('symbol ' + item + ' - not found in alphabet!')
				return False

		self.chain_str = chain


	def _start_checking(self):
		pass



	def error_print(self, error_message :str):
		err_message = 'ERROR: ' + error_message + '\n'
		self.output_str += err_message
		print(err_message)

	def print_dmpa_p(self):
		pass