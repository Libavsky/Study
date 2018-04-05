#include "stdafx.h" 
#include <iostream>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cstring>



#define maxNumber 200001

using namespace std;

int rsq(int index, long long *fenwick) {
	int returnValue = 0;
	for (int i = index + 1; i > 0; i -= i&-i) {
		returnValue += fenwick[i];
	}
	return returnValue;
}

void adjust(int index, long long *fenwick) {
	for (int i = index + 1; i < maxNumber; i += i&-i) {
		fenwick[i]++;
	}
}



int values[maxNumber];
int positions[maxNumber];

int cmp(int a, int b) {
	if (values[a] != values[b]) return values[a] < values[b];
	return positions[a] < positions[b];
}

int main()
{
	int t;
	scanf("%d", &t);

	long long fenwick[maxNumber];
	for (int qwertz = 0; qwertz < t; ++qwertz) {
		memset(fenwick, 0, sizeof fenwick);
		int n;
		scanf("%d", &n);

		long long solution = 0;
		vector<int> pos;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &values[i]);
			positions[i] = i;
			pos.push_back(i);
		}

		sort(pos.begin(), pos.end(), cmp);

		for (int i = 0; i < n; ++i) {
			adjust(pos[i], fenwick);
			solution += pos[i] - rsq(pos[i], fenwick) + 1;
		}

		printf("%lld\n", solution);
	}

	return 0;
}