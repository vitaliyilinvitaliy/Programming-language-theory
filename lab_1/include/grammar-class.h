#ifndef _GRAMMAR_CLASS_H_
#define _GRAMMAR_CLASS_H_

#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>

        /*   Класс грамматики   */
class Grammar{
    private:
        std::set<char> VT;                              //Множество терминальных символов
        std::set<char> NT;                              //Множество нетерминльных символов
        std::map<char,std::vector<std::string>> P;      //Множество правил
        std::pair<unsigned int, unsigned int> Range;    //Диапазон длин цепочки    
        char S;                                         //Целевой символ грамматики

        std::set<std::string> Chains;                   //set всех цепочек 
        void generate_chain(std::string);               //Функция генерации цепочек
    

    public:
        int push_term_symb(char symbol);                                    //Метод для добавления терминального символа
        int push_no_term_symb(char symbol);                                 //Метод для добавления нетерминального символа
        int push_rule(char vn_symbol, std::vector<std::string> rule_vect);  //Метод для добавления правила
        int set_start_symbol(char symbol);                                  //Метод для задания целевого символа
        int print_grammar(void);                                            //Метод для вывода грамматики на экран  
        int set_range(unsigned int x, unsigned int y);                      //Метод для задания диапазона длин цепочек

        void generate(void);                                                //Метод генерации цепочек
};

#endif //_GRAMMAR_CLASS_H_
