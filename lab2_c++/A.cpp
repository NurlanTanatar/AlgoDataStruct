#include <iostream>
#include <string>
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

class LL {
    private:
        Node *head, *tail;
        void _print(){
            while( head != NULL){
                cout << head->data << " ";
                head = head->next;
            }
        }
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

        int count(string key)
{
            if(head == NULL)
                return 0;
                
            int frequency = count(key);

            if(head->data == key)
                return 1 + frequency;
            return frequency;
        }

};

int main(){
    LL *l = new LL();
    string hell = "hello";
    for(int i = 0; i < 10; ++i){
        l->add(hell + to_string(i));
    }
    int counted = l->count(hell);
    cout << counted  << endl;

    return 0;
}
