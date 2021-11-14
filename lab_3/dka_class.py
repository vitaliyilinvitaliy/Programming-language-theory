import os
import csv

class DKA:
    
    dka_matrix = []
    alphabet = []
    final_states = []

    number_states = int(0)
    initial_state = int(0)
    
    name_configure_file = ''
    str_output = ''

    #def __init__(self, config_file: str):
    #    self.name_configure_file = config_file
    #    self._read_config_(config_file)
        #self.alphabet = list(filter(None, self.alphabet))
        #self.final_states = list(filter(None, self.final_states))

    def __init__(self, matrix: list, st_num: int):
        self.dka_matrix = matrix
        self.number_states = st_num
    
    def _set_final_states(self, final_st_l: list):
        self.final_states = final_st_l

    def _set_init_state(self, state_num: int):
        self.initial_state = int(state_num)

    def _read_config_(self, config_file: str):
        filename, file_extension = os.path.splitext(config_file)
    
        if file_extension != '.csv':
            print('ERROR: The file must have a .csv extension!')
            exit()
        print(os.path.exists(config_file))
        if os.path.exists(config_file) == False:
            print('ERROR: File ' + config_file + ' not found!')
            exit()
        
        with open(config_file, encoding='utf-8') as csv_file:
            file_reader = csv.reader(csv_file, delimiter=',') 
            line_number = int(0)

            for row in file_reader:
                
                mass_state = []

                if line_number > 1:
                    if len(row) != self.number_states:
                        self.str_output += 'ERROR: Invalid Jump String Len = ' + str(len(row)) + ' != ' + str(self.number_states) + '\n'

                        print('ERROR: Invalid Jump String Len = ',len(row), ' != ', self.number_states)
                        return
                        
                    for i in range(len(row)):
                        mass_state.append(row[i].split(' '))

                    self.dka_matrix.append(mass_state)
                    
                elif line_number == 0:
                    self._set_configure(row)        
                elif line_number == 1:
                    self._set_alphabet(row)
                line_number += 1


    def _set_configure(self, row: list):
        if len(row) < 3:
            self.str_output += 'ERROR: Invalid configuration length (len <3)\n'
            print('ERROR: Invalid configuration length (len <3)')
            return

        self.initial_state = int(row[1])
        self.number_states = int(row[0])
        self.final_states = row[2].split(' ')
        
        
    def display_dka(self):
        print('Name configure file:\t', self.name_configure_file, end='\n\n')
        print('Alphabet:\t', self.alphabet)
        print('Number states:\t ', self.number_states)
        print('Initail state:\t q' + str(self.initial_state))
        print('Final states:\t ', end='')
        
        for fs in self.final_states:
            print('q' + fs, end=' ')

        print('\n\n\t ', end='')
        for i in range(self.number_states):
            print('q' + str(i),end='\t ')

        print('')

        for i in range(self.number_states):
            print('q' + str(i),end='\t')
            for j in range(self.number_states):
                print(self.dka_matrix[i][j], end='\t')
                
            print('')


    def _set_alphabet(self, alph: list):
        if len(alph) != 0:
            self.alphabet = alph[0].split(' ')
        else:
            self.str_output += 'ERROR: Size alphabet list invalid!\n'
            print('ERROR: Size alphabet list invalid!')
            return 


    def _string_character_checking(self, chain: str) -> bool:
        #if len(chain) == 0:
             
            #self.str_output += 'ERROR: The chain is empty!\n'
            #print('ERROR: The chain is empty!')
            #return False

        flag_no_alphabet = False

        for i in chain:
            if i not in self.alphabet:
                flag_no_alphabet = True
                self.str_output += 'Chain: ' + str(i) + ' - does not belong to the alphabet!\n' 
                print(i,'- does not belong to the alphabet!')

        for st in self.final_states:
            if int(st) >= self.number_states:
                self.str_output += 'State ' + str(st) +  ' cannot be final!\n'

        for spis in self.dka_matrix:
            ch_dict = dict()
            for it in spis:
                for i in it:
                    if i in ch_dict:
                        print(ch_dict)
                        self.str_output += 'This is a non-deterministic state machine!\n'
                        return False
                    else:
                        if i not in self.alphabet and i != ' ':
                            self.str_output += 'Graph: ' + str(i) + ' - does not belong to the alphabet!\n'
                            flag_no_alphabet = True
                        if i != ' ': 
                            ch_dict[i] = 1



        if flag_no_alphabet:
            return False

        return True


    def _find_next_state(self, current_state: int, chain_symbol: str) -> int:
        self.str_output += 'q' + str(current_state) + '--' + chain_symbol + '-->'
        print('q' + str(current_state) + '--' + chain_symbol + '-->', end='') 
    
        index_state = 0
        flag_find_state = False

        for symbols in self.dka_matrix[current_state]:
            if chain_symbol in symbols:
                self.str_output += 'q' + str(index_state) + '\n'
                print('q' + str(index_state))
                flag_find_state = True
                break

            index_state += 1

        if flag_find_state == False:
            index_state = -1
            self.str_output += 'Not found!\n'
            print('Not found!')

        return index_state


    def _start_building_chain(self, chain: str)->bool:
        current_state = self.initial_state

        for symbol in chain:
            current_state = self._find_next_state(current_state, symbol)
            
            if current_state == -1:
                break

        if str(current_state) in self.final_states:
            self.str_output += 'Success!\n'
            print('Success!')
        else:
            if current_state != -1:
                self.str_output += 'q' + str(current_state) + ' - the current state is not final!\n'
                print('q' + str(current_state) + ' - the current state is not final!')
            self.str_output += 'Failed!\n'
            print('Failed!')
            return False


    def check_chain(self, chain: str):
        self.str_output += 'Checked chain: ' + chain + '\n'
        print('Checked chain: ', chain)
        
        if self._string_character_checking(chain):
            self._start_building_chain(chain)
        else:
            self.str_output += 'Chain ' + chain + ' cannot be built!\n' 
            print('Chain ' + chain + ' cannot be built!')
