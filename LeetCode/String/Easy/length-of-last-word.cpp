class Solution {
public:
int lengthOfLastWord(string s)
{
	int i = 0;
	vector<string> strs;
	string tmpString;
	while (i < s.length())
	{
		if (s[i] == ' ')
			i++;
		else if (s[i] != ' ')
		{
			tmpString = "";
			while(s[i] != ' ' && i < s.length())
			{
				tmpString.push_back(s[i]);
				i++;
			}
			strs.push_back(tmpString);
			i++;
		}
	}
	if (strs.empty()){
		return 0;
	}
	string lastString = strs.back();
	return (lastString.length());
}
};
