#include<iostream>
#include <bits/stdc++.h>
using namespace std;

//o(n) implementation
int power(int x,unsigned int y) {
	cout << "\n" << x << "\t" << y;
	if(y == 0) {
		return 1;
	 } else if (y%2 == 0) { 
	 	cout<<"In even";
		return power(x, y/2)*power(x, y/2);
	 } else { 
	 	cout<<"\nIn odd";
		return x*power(x, y/2)*power(x, y/2);
	 }
}

//O(log n) implementation
int powerOpt(int x , unsigned int y) {
	int temp;
	cout<<x<<y;
	if(y==0) {
		return 1;
	} 
	temp = powerOpt(x, y/2);
	cout<<"\nthe value\n"<<temp;
	if(y%2==0) {
		return temp*temp;
	} else {
		cout<<"here with "<<"\t"<<x<<"\t"<<temp;
		return x*temp*temp;
	}
}


int main(int argc, char const *argv[])
{

	cout<<"the power function";
	int x = 2;
	unsigned int y  = 3;
	cout<<"\nthis is the output\t\n---"<<powerOpt(x, y);
	/* code */
	return 0;
}