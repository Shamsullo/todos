#include <iostream>
using namespace std;

int computeWeightedSum(int a[], int len)
{
	int evenMultiplayer = 2;
	int oddMultiplayer = 3;
	int evenSum = 0;
	int oddSum = 0;

	for (int i = 0; i < len; ++i)
	{
		if (a[i]%2 == 0)
		{
			evenSum += a[i];
		}
		else
		{
			oddSum += a[i]
		}
	}

	return (evenMultiplayer * evenSum) + (oddMultiplayer * oddSum)

}