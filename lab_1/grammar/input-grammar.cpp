#include "grammar-class.h"

#include <iostream>
#include <vector>

using namespace std;

void input_grammar(void)
{
    unsigned int size_VT = 0;
    unsigned int size_NT = 0;
    char symbol = 0;
    char target = 0;
    char direction = 0;
    unsigned int x = 0;
    unsigned int y = 0;
    
    Grammar mygram;

    vector<char> NT_vec;
 
    cout << endl << "Input size VT: ";
    cin >> size_VT;
    
    cout << endl << "Input size NT: ";
    cin >> size_NT;

    for(unsigned int i = 0; i < size_VT; )
    {
        cout << endl << "Input VT symbol: ";
        cin >> symbol;
        if(mygram.push_term_symb(symbol) == 0)
        {
            i++;
        }
    }

    for(unsigned int i = 0; i < size_NT; )
    {
        cout << endl << "Input NT symbol: ";
        cin >> symbol;
        if(mygram.push_no_term_symb(symbol) == 0)
        {
            NT_vec.push_back(symbol);
            i++;
        }
       
    }

    for(unsigned int i = 0; i < size_NT; )
    {
        unsigned int size_Pi = 0;
        cout << endl << "Input size rule " << NT_vec[i] << ": ";
        cin >> size_Pi;
        vector<string> rules_vec;

        for(int j = 0; j < size_Pi; )
        {
            string str_Pi;
            cout << "Input rule: ";
            cin >> str_Pi;
            rules_vec.push_back(str_Pi);  
            j++;
        }
        if(mygram.push_rule(NT_vec[i], rules_vec) == 0)
        {
            i++;
        }
    }

    do{
        cout << "Input target symbol: ";
        cin >> target;
        cout << endl;
    }while(mygram.set_start_symbol(target) != 0);
   
    do{
        cout << "Input direction: ";
        cin >> direction;
        cout << endl; 
    }while(mygram.set_direction(direction));
    
    cout << endl << endl << "Input right border: ";
    cin >> x;
    cout << endl << "Input left border: ";
    cin >> y;
    cout << endl;

    mygram.set_range(x, y);
/*
      mygram.push_term_symb('a');
      mygram.push_term_symb('b');
      mygram.push_term_symb('c');
 
      mygram.push_no_term_symb('A');
      mygram.push_no_term_symb('B');
      mygram.push_no_term_symb('C');
 
      std::vector<std::string> A;
      std::vector<std::string> B;
      std::vector<std::string> C;
 
      A.push_back("aBbC");
 
      B.push_back("aaBb");
      B.push_back("^");
 
      C.push_back("cC");
      C.push_back("^");
 
      mygram.push_rule('A', A);
      mygram.push_rule('B', B);
      mygram.push_rule('C', C);
 
      mygram.set_range(3, 8);
      mygram.set_start_symbol('A');
 */
      mygram.print_grammar();
      mygram.generate();

}
