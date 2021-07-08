#include <iostream>
#include <string>
using namespace std;

class Node {
    public:
    string data;
    Node *next;
    int freq = 1;
    // Node(int data) {
    //     this->data = data;
    //     this->next = NULL;
    //     this->prev = NULL;
    // }
    Node(string x):data(x), next(NULL){
        freq = 1;
    }
};
bool comp (string x, string y) {return x<y;}; 
class LL {
    private:
        Node *head, *tail;
        void _print(){
            while( head != NULL){
                cout << head->data << " ";
                head = head->next;
            }
        }
        int frequency;
    public:
        LL(){
            head = NULL;
        }

        void add(string x){
            Node *newNode = new Node(x);
            if(head == NULL){
                head = newNode;
            } else {
                tail->next = newNode;
                tail = newNode;
            }
            if(search(x)){
                
            }
        }
        void print(){
            _print();
        }
        
        bool search(string key){
            while( head != NULL){
                if (head->data == key)
                    return true;
                head = head->next;
            }
            return false;
        }
        
        int count(string key){
            frequency = 0;
            while( head != NULL){
                if (head->data == key)
                    frequency++;
                head = head->next;
            }
            return frequency;
        }
};

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    string s;
    LL * l = new LL();
    while(getline(cin,s)) {
        if(s == " "){
            break;
        }else if(s.length()){
            l->add(s);
        }
    };
    return 0;
}
