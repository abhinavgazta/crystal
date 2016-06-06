#include <iostream>
using namespace std;

struct node {
	node *left;
	node* right;
	int data;
};


// populating height and size in one go rather tan seperate traversals for them...
int sizeandheight(node* root, int &size) {
	if(!root) {
		return 0;
	}
	int l = sizeandheight(root->left, size);
	int r = sizeandheight(root->right, size);
	size++;
	return (l > r) ? l+1 : r+1;
}


float getDensity(node* root) {
	if(root == NULL) {
		return 0;
	}
	int size = 0;
	int _height = sizeandheight(root, size);
	return (float)size/_height;
}



node* createnode(int data) {
	node* root = new node();
	root->data = data;
	root->left = NULL;
	root->right = NULL;
	return root;
}



int main(int argc, char const *argv[])
{
	node* root = createnode(10);
	root->left = createnode(8);
	root->right = createnode(15);
	root->left->left = createnode(6);
	root->left->left->left = createnode(5);
	cout<<"this is the density\t\n"<<getDensity(root);
	/* code */
	return 0;
}