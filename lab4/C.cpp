#include <iostream>

using namespace std;

struct Node{
    int data;
    Node *left, *right;
    Node(int x):left(NULL), right(NULL),data(x){}
};

class BST{
    private:
    Node *root;
    void _print(Node *node){
        if (node == NULL)
            return;
        _print(node->left);
        cout << node->data << " ";
        _print(node->right);
    }
    Node* _insert(Node *node, int data) {
        if (node == NULL) {
            node = new Node(data);
            return node;
        }
        if (data < node->data) 
            node->left = _insert(node->left, data);
        else if (data > node->data)
            node->right = _insert(node->right, data);
        return node;
    }
    Node* _rightmost(Node * _root){
        Node * temp = _root;
        while(temp != NULL && temp->right != NULL){
            temp = temp->right;
        }
        if(temp == NULL) return NULL;
        return temp;
    }
    Node* _second(Node *node) {
        if (node->right == NULL and node->left != NULL)
            return _rightmost(node->left);
        if(node->right != NULL and 
            node->right->left == NULL and 
            node->right->right == NULL)
           return node;
        return _second(node->right);
    }
    public:
    BST(){
        root = NULL;
    }
    void insert(int x){
        root = _insert(this->root, x);
    }
    void scnd(){
        cout << (_second(this->root))->data << endl;
    }
    
};

int main(){
    BST *bst = new BST();

    int n;
    while(cin >> n){
        if(n == 0)
            break;
        else 
            bst->insert(n);
    }
    bst->scnd();
    return 0;
}
