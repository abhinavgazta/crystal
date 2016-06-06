#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define MAX_CHARS 256

bool stringsIsomorphic(string str1, string str2) {
	int str1_len = str1.length();
	int str2_len = str2.length();
	if(str1_len != str2_len) {
		cout<<"in herer";
		return false;
	}
	bool marked[MAX_CHARS] = {false};
	int map[MAX_CHARS];
	memset(map, -1, sizeof(map));
	for (int i = 0; i < str2_len; ++i)
	{
		// all str1 init to -1
		if(map[str1[i]] == -1) {
			
			if(marked[str2[i]] == true) {
				return false;
			}
			// visited
			marked[str2[i]] = true;
			
			//for them mapping 
			map[str1[i]] = str2[i];

		} else if( map[str1[i]] != str2[i]) {
			cout<<"i am exiting";
			return false;
		}
		/* code */
	}
	return true;
}


int main(int argc, char const *argv[])
{

	string str1 = "aab";
	string str2 = "xxy";	
	if(stringsIsomorphic(str1, str2)) {
		cout<<"they are isomorphic equal";
	} else {
		cout<<"they are not isomorphic";
	}	
	/* code */
	return 0;
}