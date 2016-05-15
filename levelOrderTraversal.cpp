#include <iostream>
#include <queue>
using namespace std;

struct node
{
	int data;
	node* left;
	node* right;
	/* data */
};


int gethieght(node* root) {
	if(root==NULL) {
		return 0;
	} else {
	int left_height = gethieght(root->left);
	int right_height = gethieght(root->right);
	if(left_height < right_height) {
		return right_height+1;
	} else {
		return left_height+1;
	}
	}
}

void printGivenLevel(node * root, int level) {
	if(root==NULL) {
		return;
	} 
	if(level == 1) {
		//print fo that level
		cout<<"\t"<<root->data;
	} else if(level > 1) {
		//comment out whichever to get either left view or right view......
		printGivenLevel(root->left , level-1);
		printGivenLevel(root->right, level-1);
	}

}


void printLevelOrder(node* root) {
	int height = gethieght(root);
	for (int i = 1; i <= height; ++i)
	{
		printGivenLevel(root, i);
		/* code */
	}
}

//the queue method is simpler and easier than the recursive one..
//time complexity is O(n)
void printLeveOrderQueue(node *root) {
	if(root==NULL)
		return;
	queue<node *> q;
	q.push(root);
	while(q.empty() == false) {
		node* temp = q.front();
		cout<<"\t\n"<<temp->data;
		q.pop();
		//left view and right view can be handled from here.......
		//enque left child
		if(temp->left!=NULL) {
			q.push(temp->left);
		}
		//enque right child
		if(temp->right!=NULL) {
			q.push(temp->right);
		}	
	}
}


node* newnode(int data) {
	node* root = new node();
	root->data = data;
	root->left = NULL;
	root->right = NULL;
	return root;
}

//-----solve level order generic problem----//---solve left view---//---solve right view.....
int main(int argc, char const *argv[])
{
	/*
				  10
		 	5           15
	    4         6   13       19

	*/
	node* root = newnode(10);
	root->left =  newnode(5);
	root->left->left = newnode(4);
	root->left->right =  newnode(6);
	root->right =   newnode(15);
	root->right->right = newnode(19);
	root->right->left = newnode(13);
	printLevelOrder(root);
	printLeveOrderQueue(root);
	/* code */
	return 0;
}