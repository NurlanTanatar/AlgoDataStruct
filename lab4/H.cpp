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
    bool _is_balanced(Node *node){
        if(node == NULL)
            return true;
        if(abs( _depth(node->left) - _depth(node->right)) <= 1 
        and _is_balanced(node->left) and _is_balanced(node->right))
            return true;
        return false;
    }
    public:
    BST(){
        root = NULL;
    }
    void insert(int x){
        root = _insert(this->root, x);
    }
    void balanced(){
      _is_balanced(this->root) ? cout << "YES" << endl: cout << "NO" << endl;
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
    bst->balanced();
    return 0;
}



