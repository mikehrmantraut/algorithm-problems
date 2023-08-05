class Solution {
public:
int sum(int n)
{
	int count = 0;
	vector<int> digitsVector;
	digitsVector.clear();
	while (n != 0)
	{
		digitsVector.push_back(n % 10);
		n /= 10;
	}
	for (int n:digitsVector)
	{
		count += pow(n, 2);
	}
	return (count);
}
bool isHappy(int n) {
    unordered_set<int> seen;
    while (n != 1 && seen.find(n) == seen.end()) {
        seen.insert(n);
        n = sum(n);
    }
    return n == 1;
}
};
