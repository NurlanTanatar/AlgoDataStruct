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
    int _depth(Node *node) {
        if (node == NULL)
            return 0;
        return 1 + max(_depth(node->left), _depth(node->right));
    }
    public:
    BST(){
        root = NULL;
    }
    void insert(int x){
        root = _insert(this->root, x);
    }
    void depth(){
        cout << _depth(this->root) << endl;
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
    bst->depth();
    return 0;
}
