#include <iostream>
#include <stdio.h>
#include <new>
using namespace std;

struct Bstnode {
	int data;
	Bstnode *left;
	Bstnode *right;
};


Bstnode* GetNewNode(int data) {
	Bstnode* root =  new Bstnode();
	root->data = data;
	root->left = NULL;
	root->right = NULL;
	return root;	
}

bool Search(Bstnode* root, int data) {
	if( root == NULL ) return false;
	else if (data == root->data) return true;
	else if (data <= root->data) return Search(root->left, data);
	else return Search(root->right, data);		
}

Bstnode* Insert(Bstnode* root , int data) {
	if(root == NULL) {
		printf("found null so getting new\n");
		root = GetNewNode(data);
	 } else if(data <= root->data) {
		printf("inserting into left subtreee\n");
		root->left = Insert(root->left, data);
	} else {
		printf("inserting into right subtree\n");
		root->right = Insert(root->right, data);
	}
	return(root);
}

void loopPrintLeft(Bstnode* root) {
	while(root !=NULL) {
		printf("%d\n",root->data);
		root = root->left;
	}
}
void loopPrintRight(Bstnode* root) {
	while(root !=NULL) {
		printf("%d\n",root->data);
		root = root->right;
	}
}

void printTree(Bstnode* root) {
	if(root != NULL) {
		printf("%d \n", root->data);
		printTree(root->left);
		printf("%d \n", root->data);
		
	}	
}

void printPreOrder(Bstnode* root) {
	if(root != NULL) {
		printf("%d \n", root->data);
		printPreOrder(root->left);
		printPreOrder(root->right);
	}
}

void printBSTInoder(Bstnode* root) {
	if(root != NULL) {
		printBSTInoder(root->left);
		printf("%d \n", root->data);
		printBSTInoder(root->right);
	}
}

void printPostOrder(Bstnode* root) {
	if(root != NULL) {
		printPostOrder(root->left);
		printPostOrder(root->right);
		printf("%d \n", root->data);
	}
}

Bstnode* getMinNode(Bstnode* node) {
	while(node->left !=NULL) {
		node = node->left;
	}
	return node;
}

Bstnode* deletenode(Bstnode* root, int data) {
	if (root == NULL) return root;
	if(data < root->data) {
	//move left
		root->left = deletenode(root->left, data);	
	}
	if(data > root->data) {
	//move right
		root->right = deletenode(root->right, data);
	}
	else if (data == root->data) {
		if(root->left == NULL) {
			struct Bstnode* temp = root->right;
			printf("here");
			free(root);
			printf("%d",temp->data);
			return temp;	
		} 
		else if( root->right == NULL) {
			struct Bstnode* temp = root->left;
			printf("second");
			free(root);
			return temp;
		}
		
		struct Bstnode* temp = getMinNode(root->right);
		root->data = temp->data;
		root->right = deletenode(root->right, data);
	}
	return root;
}

/*def FindNode(Bstnode* root, Bstnode* &pre, Bstnode* &suc, int data) {
	if(root == NULL) return;
	if(root->data == data) {
		return;
		}
	if(data < root->data) {
		// left node
		suc = root
		FindNode(root->left, pre, suc, data);
	}
	else {
		//right node
		pre = root
		Findnode(root->right, pre, suc, data);
	} 
}
*/

int main() {
	Bstnode* root = NULL;
	//int t = root->data;
	//printf("this is %d", t);
	root = Insert(root, 10);root = Insert(root, 20);root = Insert(root, 5);root = Insert(root, 6);root = Insert(root, 4);Insert(root, 30);Insert(root, 15);
	//int number;
	//cout<<" please enter a number";
	//cin>>number;
	//if(Search(root, number) == true) cout<<"found it\n";
	//else cout<<"not found";
	//printTree(root);
	//printBSTInoder(root);
	//loopPrint(root);
	//loopPrintRight(root);
	//printPostOrder(root);
	//Bstnode* take = getMinNode(root);
	//printf("output %d \n", take->data);
	printBSTInoder(root);
	printf("------\n");
	root = deletenode(root, 4);
	printf("------\n");
	printBSTInoder(root);
	root = deletenode(root, 5);
	printf("------\n");
	printBSTInoder(root);
	root = deletenode(root, 6);
	printf("------\n");
	printBSTInoder(root);
}


