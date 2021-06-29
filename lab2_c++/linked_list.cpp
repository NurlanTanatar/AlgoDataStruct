#include <iostream>
#include <string>
#include <set>
using namespace std;

class Node {
    public:
    string data;
    Node *next;

    // Node(int data) {
    //     this->data = data;
    //     this->next = NULL;
    //     this->prev = NULL;
    // }
    Node(string x):data(x), next(NULL){}
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
            head, tail = NULL;
        }

        void add(string x){
            Node *newNode = new Node(x);
            if(head == NULL){
                head = tail = newNode;
            } else {
                tail->next = newNode;
                tail = newNode;
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

int main() {
    string hell;
    LL *l = new LL();
    set<string> uniq;
    while(cin >> hell){
        l->add(hell); //добавление всех элементов
        uniq.insert(hell);
    }
    for(auto& it : uniq)
        cout << it <<" "<< l->count(it) << endl;
}