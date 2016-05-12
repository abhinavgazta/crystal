#include<iostream>
#include <bits/stdc++.h>
#include<vector>
using namespace std;

struct Node {
	Node *left;
	Node* right;
	int data;
};

void diagonalPrintUtil(Node *root, int distance, map<int, vector<int> > &diagonalPrintMap) {
	if(!root)
		return;
	diagonalPrintMap[distance].push_back(root->data);
	//left child increase distance
	diagonalPrintUtil(root->left, distance+1, diagonalPrintMap);
	//right child keep distacnce sam and all all to the map..
	diagonalPrintUtil(root->right, distance, diagonalPrintMap);
}

void diagonalPrint(Node *root) {
	 // create a map of vectors to store Diagonal elements
    map<int, vector<int> > diagonalPrint;
    diagonalPrintUtil(root, 0, diagonalPrint);
    cout << "Diagonal Traversal of binary tree : \n";
    for (map<int, vector<int> >::const_iterator it = diagonalPrint.begin(); it != diagonalPrint.end(); ++it)
		    {
		    	cout<< "\n"<<it->first<<"\n";
		    	typedef vector<int>::const_iterator ListIterator;
		        for (ListIterator itr = it->second.begin(); itr != it->second.end(); ++itr) {
		            cout << *itr  << ' ';
		        }
		        cout << '\n';
		    }

}


Node* createnode(int data) {
	Node* node = new Node();
	node->data = data;
	node->left = NULL;
	node->right =  NULL;
	return node;
}

int main(int argc, char const *argv[])
{
	Node* root = createnode(8);
	root->left = createnode(3);
	root->right = createnode(10);
	root->left->left = createnode(1);
	root->left->right = createnode(6);
	root->right->right = createnode(14);
	root->right->right->left =  createnode(13);
	root->left->right->left = createnode(4);
	root->left->right->right = createnode(7);
	diagonalPrint(root);
	/* code */
	return 0;
}