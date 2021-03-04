#include <iostream>
using namespace std;


int hasNValues(int a[ ], int n, int len)
{
	// for keeping quantities 
	int tem1p[len];
	// for keeping uniques
	int temp2[len];
	 // Finding frequency of each element
	for (i = 0; i < len; i++){
		cnt = 1;
		for (j = i + 1; j < len; j++){

		  if (a[i] == a[j]){
		    cnt++;
		    temp1[j] = 0;
		  }
		}

		temp1[i] = cnt;
	}

	bool reason = false;
	int uCount = 0;
	// Printing all unique elements of the array
	for (i = 0; i < len; i++){
		if (temp1[i] == 1){
			if(temp1[i] == n)
			{
				reason = true;
			}
		 	temp2[i] = a[i];
		 	uCount++;
		}
	}

	if (reason == true) {
		return 1
	}
	return 0

}


