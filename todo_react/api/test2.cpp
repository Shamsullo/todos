#include <iostream>
using namespace std;

isPairedN(int a[], int n, int len)
{
	if (len < 3) return 0;

	for (int i = 0; i < len; ++i)
	{
		// int j = i + 1;
		for (int 0; j < len; ++i)
		{
			if (j != i)
			{
				if (a[i] + a[j] == n)
				{
					if (i + j == n)
					{
						return 1
					}
				}
			}
		}
	}

	return 0
}

c int a6(int[] a)
{
 if (a.length < 3) return -1;
 int i = 0;
 int j = a.length - 1;
 int idx = 1;
 int leftSum = a[i];
 int rightSum = a[j];
 for (int k = 1; k < a.length - 2; k++)
 {
 if (leftSum < rightSum)
 {
i++;
leftSum += a[i];
idx = i + 1;
 }
 else
 {
j--;
rightSum += a[j];
idx = j - 1;
 }
 }
 if (leftSum == rightSum)
 return idx;
 else
 return -1;
}