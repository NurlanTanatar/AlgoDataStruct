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
    bool _has_one_child(Node *node){
        return (node->left == NULL and node->right != NULL) or ((node->left != NULL and node->right == NULL));
    }
    void _one_child(Node *node){
        if(node == NULL){
            return;
        }
        _one_child(node->left);
        if(_has_one_child(node))
            cout << node->data << endl;
        _one_child(node->right);
    }
    public:
    BST(){
        root = NULL;
    }
    void insert(int x){
        root = _insert(this->root, x);
    }
    void one(){
        _one_child(this->root);
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
    bst->one();
    return 0;
}

