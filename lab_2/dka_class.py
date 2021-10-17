import os
import csv

class DKA:
    
    dka_matrix = []
    alphabet = []
    final_states = []

    number_states = int(0)
    initial_state = int(0)
    
    name_configure_file = ''


    def __init__(self, config_file: str):
        self.name_configure_file = config_file
        self._read_config_(config_file)
        #self.alphabet = list(filter(None, self.alphabet))
        #self.final_states = list(filter(None, self.final_states))
        

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
                        print('ERROR: Invalid Jump String Len = ',len(row), ' != ', self.number_states)
                        exit()
                        
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
            print('ERROR: Invalid configuration length (len <3)')
            exit()

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
            print('ERROR: Size alphabet list invalid!')
            exit()


    def _string_character_checking(self, chain: str) -> bool:
        if len(chain) == 0:
            print('ERROR: The chain is empty!')
            return False

        flag_no_alphabet = False

        for i in chain:
            if i not in self.alphabet:
                flag_no_alphabet = True
                print(i,'- does not belong to the alphabet!')

        if flag_no_alphabet:
            return False

        return True


    def _find_next_state(self, current_state: int, chain_symbol: str) -> int:
        print('q' + str(current_state) + '--' + chain_symbol + '-->', end='') 
    
        index_state = 0
        flag_find_state = False

        for symbols in self.dka_matrix[current_state]:
            if chain_symbol in symbols:
                print('q' + str(index_state))
                flag_find_state = True
                break

            index_state += 1

        if flag_find_state == False:
            index_state = -1
            print('Not found!')

        return index_state


    def _start_building_chain(self, chain: str)->bool:
        current_state = self.initial_state

        for symbol in chain:
            current_state = self._find_next_state(current_state, symbol)
            
            if current_state == -1:
                break

        if str(current_state) in self.final_states:
            print('Success!')
        else:
            if current_state != -1:
                print('q' + str(current_state) + ' - the current state is not final!')
            print('Failed!')
            return False


    def check_chain(self, chain: str):
        print('Checked chain: ', chain)

        if self._string_character_checking(chain):
            self._start_building_chain(chain)
        else:
            print('Chain ' + chain + ' cannot be built!')
