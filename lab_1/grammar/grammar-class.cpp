#include "grammar-class.h"

#include <iostream>
#include <iostream>
#include <iterator>
#include <string>

int Grammar::push_term_symb(char symbol)
{
    if(VT.find(symbol) != VT.end())
    {
        std::cout <<"push_term_symb: Such a TERMINAL symbol already exists!" << std::endl;
        return 1;
    }

    if(NT.find(symbol) != NT.end())
    {
        std::cout <<"push_term_symb: Such a NON-TERMINAL symbol already exists!" << std::endl;
        return 1;
    }

    VT.insert(symbol);

    return 0;
}


int Grammar::push_no_term_symb(char symbol)
{
    if(NT.find(symbol) != NT.end())
    {
        std::cout <<"push_no_term_symb: Such a NON-TERMINAL symbol already exists!" << std::endl;
        return 1;
    }
     
    if(VT.find(symbol) != VT.end())
    {
        std::cout <<"push_no_term_symb: Such a TERMINAL symbol already exists!" << std::endl;
        return 1;
    }

    NT.insert(symbol);

    return 0;
}


int Grammar::push_rule(char vn_symbol, std::vector<std::string> rule_vect)
{
    std::pair<char, std::vector<std::string>> rule_pair(vn_symbol, rule_vect);

    if(NT.size() == 0)
    {
        std::cout <<"push_rule: There are NON-TERMINAL symbols!" << std::endl;
        return 1;
    }

    if(NT.find(vn_symbol) == NT.end())
    {
        std::cout <<"push_rule: There is NO such nonterminal!" << std::endl;
        return 2;
    }

    if(P.size() == NT.size())
    {
        std::cout <<"push_rule: The number of RULES should not exceed the number of NON-TERMINAL characters!" << std::endl;
        return 3;
    }

    for(auto it : rule_vect)
    {
        for(int i = 0; i < it.size(); i++)
        {
            if(VT.find(it[i]) == VT.end() &&  NT.find(it[i]) == NT.end() && it[i] != '^')
            {
                std::cout << it << ": " << it[i] << " - not found!" << std::endl;
                return 4;
            }
        }
    }

    P.insert(rule_pair);

    return 0;
}


int Grammar::set_start_symbol(char symbol)
{
    if(NT.find(symbol) == NT.end())
    {
        std::cout <<"set_start_symbol: You cannot start with this symbol! Symbol not found!" << std::endl;
        return 1;
    }
    
    S = symbol;

    return 0;
}

int Grammar::print_grammar(void)
{
    if(VT.size() == 0)
    {
        std::cout << "Terminal symbols not found!" << std::endl;
        return 1;
    }
    
    if(NT.size() == 0)
    {
        std::cout << "No nonterminal symbols found!" << std::endl;
        return 2;
    }

    if(P.size() == 0)
    {
        std::cout << "No rules found!" << std::endl;
        return 3;
    }
    
    if(NT.find(S) == NT.end())
    {
        std::cout << "Target symbol not found!" << std::endl;
        return 4;
    }

    std::cout << std::endl << "Grammar: " << std::endl;
    std::cout << "VT{ ";
   
    int i = 0;

    for(auto it : VT) 
    {
        std::cout << it << ((i != VT.size() - 1)? ", " : " }");
        i++;
    }
    
    std::cout << std::endl << "NT{ ";    

    i = 0;

    for(auto it : NT) 
    {
        std::cout << it << ((i != NT.size() - 1)? ", " : " }");
        i++;
    }

    std::cout << std::endl << "P: " << std::endl;
    
    std::cout << "\tS -> " << S << std::endl;

    for(auto it : P) 
    {
        std::cout << "\t" << it.first << " -> "; //<< it.second << std::endl;
        i = 0;
        for(auto it_vec : it.second)
        {
            std::cout << it_vec <<  ((i != it.second.size() - 1)? " | " : "\n");
            i++;
        }
        
    }

    std::cout << "\n\t" << Range.first << " - " << Range.second << std::endl;
    std::cout << "lr - " << direction << std::endl;
    return 0;
}


int Grammar::set_range(unsigned int x, unsigned int y)
{
    Range.first = x;
    Range.second = y;

    return 0;
}

int Grammar::set_direction(char lr)
{
    if(lr == 'l' || lr == 'r')
    {
        direction = lr;
    }
    else 
    {
        std::cout << "Direction - " << lr << " not found!" << std::endl;
        return 1;
    }
    return 0;
}

