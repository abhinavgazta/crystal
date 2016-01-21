// C program to print right view of Binary Tree
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

struct Node
{
    int data;
    struct Node *left, *right;
};
 
static int current_level = 0; 
static int current_level_left = 0;
// A utility function to create a new Binary Tree Node
struct Node *newNode(int item)
{
    struct Node *temp =  (struct Node *)malloc(sizeof(struct Node));
    temp->data = item;
    temp->left = temp->right = NULL;
    return temp;
}
 
void leftViewUtil(struct Node *root, int next_level) {

	if(root == NULL)
		return;
	if (current_level_left < next_level) {	
        printf("%d\t", root->data);
        current_level_left = next_level;
	}
	leftViewUtil(root->left, next_level+1);
	leftViewUtil(root->right, next_level+1);
}

// Recursive function to print right view of a binary tree.
void rightViewUtil(struct Node *root, int next_level)
{
    // Base Case
    if (root==NULL)  
    	return;
    // If this is the last Node of its level
    if (current_level < next_level)
    {
        printf("%d\t", root->data);
        current_level = next_level;
    }
    // Recur for right subtree first, then left subtree
    rightViewUtil(root->right, next_level+1);
    rightViewUtil(root->left, next_level+1);
}
 
// A wrapper over rightViewUtil()
void rightView(struct Node *root)
{
    rightViewUtil(root, 1);
}

// a wraapper for left view util 
void leftView(struct Node* root) {
	leftViewUtil(root, 1);
} 


// Driver Program to test above functions
int main()
{
    struct Node *root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    root->right->left->right = newNode(8);
    rightView(root);
 	cout<<"\n";
 	leftView(root);
    return 0;
}
