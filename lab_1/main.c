#include "grammar-class.h"

#include <iostream>
#include <vector>

int main(void)
{
    Grammar mygram;
//data = {"VT": ["0", "1", "2"], "VN": ["A", "B", "C"], "P": {"A": ["aaBbbC"], "B": ["aaBb", ""], "C": ["cC", ""]}, "S": "A"}
    
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

    mygram.set_range(1, 8);
    mygram.set_start_symbol('A');
    
    mygram.print_grammar();
    mygram.generate();

    return 0;
}
