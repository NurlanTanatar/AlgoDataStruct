#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;

string rm_space(string str)
{
    string word = "";
    for (auto x : str) 
    {
        if (x == ' ')
        {
            return word;
            word = "";
        }
        else {
            word = word + x;
        }
    }
    return word;
}

struct comp
{   
    template<typename T>
    bool operator()(T &l, T &r)
    {
        if (l.second != r.second) {
            return l.second > r.second;
        }
 
        return l.first > r.first;
    }
};

int main(){
    map<string, int> m;
    string s;
    while(cin >> s) {
        m[rm_space(s)]++;
    }

    set<pair <string, int>, comp> set(m.begin(), m.end());

    for (auto &pair:  set) cout << pair.first << " " << pair.second << endl;
    return 0;
}
