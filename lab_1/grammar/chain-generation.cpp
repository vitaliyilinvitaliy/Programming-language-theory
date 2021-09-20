#include "grammar-class.h"

#include <ostream>
#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

void Grammar::generate_chain(string chain)
{
    unsigned int count_VT_symbol = 0;
    unsigned int count_NT_symbol = 0;
    
    for(int i = 0; i < chain.size(); i++)
    {
        if(chain[i] == '^')
        {
            chain.erase(i,1);
        }         
    }

    for(int i = 0; i < chain.size(); i++)
    {
        if(VT.find(chain[i]) != VT.end())
        {
            count_VT_symbol++;
        }
        else
        {
            count_NT_symbol++;
        }
    }
   
    if(count_NT_symbol == 0)
    {
        Chains.insert(chain);
    }

    if(count_VT_symbol > Range.second)
    {
        return;
    }
    
    string begin_chain;

    for(int i = 0; i < chain.size(); i++)
    {
        if(P.find(chain[i]) != P.end())
        {
            for(int j = 0; j < P[chain[i]].size(); j++)
            { 
                string new_chain = begin_chain;  
                new_chain += P[chain[i]][j];
                for(int k = i + 1; k < chain.size(); k++)
                {
                     new_chain += chain[k];
                }
                generate_chain(new_chain);               
            }        
        }
        else
        {
            begin_chain += chain[i];
        }
    }
}


void Grammar::generate(void)
{
    string S_str = "S";
    S_str[0] = S;
    
    generate_chain(S_str);

    for(auto it : Chains)
    {
        cout << it << endl;
    }
}
