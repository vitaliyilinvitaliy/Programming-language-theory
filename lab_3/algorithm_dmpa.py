
class DMPA:
	#Параметры грамматики ДМПА
	input_state_list = list()
	size_state_int = int(0)
	alphabet_list = []
	start_state_int = int(0)
	stack_symbol_str = str('Z')
	end_state_int = int(0)
	chain_str = str('')

    #Вспомогательные параметры
	output_str = str('')
	result_checking = False

	cur_state = int(0)

	stack_dmpa = list()

	def __init__(self, args_list :list):
		if len(args_list) != 6:
			self._error_print('incorrect number of arguments: ' +  str(len(args_list)) + ' != 6')

		print(args_list)


		if not self._set_size_state_int(args_list[1]):
			print('Code error - 1')
			return
		if not self._set_state_list(args_list[0]):
			print('Code error - 0')
			return
		if not self._set_alphabet_list(args_list[2]):
			print('Code error - 2')
			return
		if not self._set_start_state_int(args_list[3]):
			print('Code error - 3')
			return
		if not self._set_end_state_int(args_list[4]):
			print('Code error - 4')
			return
		if not self._set_chain_str(args_list[5]):
			print('Code error - 5')
			return

		self._start_checking()


	def _set_state_list(self, state_str :str):
		self.stack_dmpa.clear()

		list_str = state_str.split('\n')
		for i in list_str:
			self._parse_str(i)

		counter = 0

		for i in self.input_state_list:
			print(counter,' : ',i)
			counter += 1

		return True


	def _set_size_state_int(self, size_state_str :str):
		self.size_state_int = int(0)
		self.input_state_list = list()

		if len(size_state_str) == 0:
			self._error_print('size state is empty!')
			return False

		if size_state_str.isdigit():
			self.size_state_int = int(size_state_str)

			if self.size_state_int < 0:
				self._error_print(size_state_str + ' - size incorrect!')
				return False

			for i in range(self.size_state_int):
				self.input_state_list.append(list())

			print('list: ',self.input_state_list)

			return True
		else:
			self._error_print(size_state_str + ' - size state no digit!')
			return False

    	
	def _set_alphabet_list(self, alphabet_list :str):
		self.alphabet_list = []
		alph = list(set(filter(None, alphabet_list.split(' ')))) 
		
		if len(alph) == 0:
			self._error_print('the alphabet is empty!')
			return False

		for item in alph:
			if len(item) > 1:
				self._error_print(item + ' alphabet character cannot be of length > 1!')
				return False

		self.alphabet_list = alph

		return True

	def _set_start_state_int(self, start_state_str :str):
		self.start_state_int = int(0)

		if len(start_state_str) == 0:
			self._error_print('start state is empty!')
			return False

		if start_state_str.isdigit():
			self.start_state_int = int(start_state_str)

			if self.start_state_int >= self.size_state_int:
				self._error_print(start_state_str + ' - start state out of range!')
				return False

			return True
		else:
			self._error_print(start_state_str + ' - start state no digit!')
			return False


	def _set_end_state_int(self, end_state_str :str):
		self.end_state_int = int(0)

		if len(end_state_str) == 0:
			self._error_print('end state is empty!')
			return False

		if end_state_str.isdigit():
			self.end_state_int = int(end_state_str)

			if self.end_state_int >= self.size_state_int:
				self._error_print(self.end_state_int + ' - start state out of range!')
				return False

			return True
		else:
			self._error_print(end_state_str + ' - end state no digit!')
			return False


	def _set_chain_str(self, chain :str):
		self.chain_str = str('')

		chain = chain.replace(' ', '')

		for item in chain:
			if not item in self.alphabet_list:
				self._error_print('symbol ' + item + ' - not found in alphabet!')
				return False

		self.chain_str = chain + 'E'
		return True


	def _start_checking(self):
		num_st = self.start_state_int

		self.stack_dmpa.append(self.stack_symbol_str)

		for item in self.chain_str:
			self.cur_state = num_st
			num_st = self._get_number_state(num_st, item)
			if num_st == -1:
				self._error_print('State not found for q' + str(self.cur_state) + ' and symbol: ' + item +' !')
				return

		if self.cur_state == self.end_state_int:
			self.out_add('Success')
		else:
			self.out_add('State ' + str(self.cur_state) + ' not finish!')



		
	def _get_number_state(self, current_number: int, current_symbol :str):
		last_stack = self.stack_dmpa[-1]

		copy_cur = current_number

		print('last_stack:',last_stack, 'current_number:',current_number)
		for item in self.input_state_list[current_number]:
			self.cur_state = item[1][0]
			if current_symbol == item[0][0] and last_stack == item[0][1]:
				print('(q' + str(current_number) + ',' + str(item[0][0]) + ',' + str(item[0][1]) + ') -> (q' + str(item[1][0]) + ',' + str(item[1][1]) + ')')
				self.out_add('q' + str(current_number) + ',' + str(item[0][0]) + ',' + str(item[0][1]) + ') -> (q' + str(item[1][0]) + ',' + str(item[1][1]) + ')')
				self.add_stack(item[0][1], item[1][1])
				print('Stack:', self.stack_dmpa)
				return item[1][0]

		return -1


	def add_stack(self, last_stack :str, new_stack :str):
		if len(new_stack) == 2:
			if new_stack[1] == last_stack:
				print('append:',new_stack[0])
				self.stack_dmpa.append(new_stack[0])
				return 0
			else:
				return -1
		elif len(new_stack) == 1:
			if new_stack[0] == last_stack:
				return 0
			elif new_stack[0] == 'E':
				self.stack_dmpa.pop()
				return 0


		return -1


	def out_add(self, args :str):
		self.output_str += args + '\n' 



	def _error_print(self, error_message :str):
		err_message = 'ERROR: ' + error_message + '\n'
		self.output_str += err_message
		print(err_message)

	def print_dmpa_p(self):
		pass


	def _parse_str(self, line :str):
		list_parse = list(filter(None, line.split('->')))

		if list_parse == []:
			return False

		if len(list_parse) != 2:
			self._error_print(line + ' - line incorrect!')
			return False

		first_arg = (list_parse[0].replace('(','')).replace(')','')
		second_arg = (list_parse[1].replace('(','')).replace(')','')

		first_arg = first_arg.split(',')
		second_arg = second_arg.split(',')

		if len(first_arg) != 3 or len(second_arg) != 2 or first_arg[0][0] != 'q' or second_arg[0][0] != 'q':
			self._error_print(line + ' - line incorrect!')
			return False

		first_arg[0] = first_arg[0].replace('q','')
		second_arg[0] = second_arg[0].replace('q','')

		if not first_arg[0].isdigit() or not second_arg[0]:
			self._error_print(line + ' - line incorrect!')
			return False 

		first_arg[0] = int(first_arg[0])
		second_arg[0] = int(second_arg[0])

		if first_arg[0] >= self.size_state_int or second_arg[0] >= self.size_state_int:
			self._error_print(line + ' - line incorrect number state out of range!')
			return False

		if len(first_arg[1]) != 1 or len(first_arg[2]) != 1 or len(second_arg[1]) > 2 or len(second_arg[1]) == 0:
			self._error_print(line + ' - line incorrect len arg!')
			return False

		result_list = [[first_arg[1],first_arg[2]],second_arg]

		self.input_state_list[first_arg[0]].append(result_list)

		print(result_list)#first_arg, ' ', second_arg)
		return True