class Solution {
public:
string firstPalindrome(vector<string>& words)
{
    string tmp1, tmp2;
    string tmp3;
    int j = 0;
    for (string word : words)
    {
        tmp1 = "";
        tmp2 = "";
        tmp3 = "";
        if (word.size() % 2 == 1)
        {
            for (int i = 0; i <= word.size() / 2; i++)
            {
                tmp1.push_back(word.at(i));
            }
            for (int i = word.size() / 2; i <= word.size() - 1; i++)
            {
                tmp2.push_back(word.at(i));
            }

        }
        if (word.size() % 2 == 0)
        {
            for (int i = 0; i < word.size() / 2; i++)
            {
                tmp1.push_back(word.at(i));
            }
            for (int i = word.size() / 2; i <= word.size() - 1; i++)
            {
                tmp2.push_back(word.at(i));
            }

        }
        for (int i=tmp2.size() - 1; i>=0;i--)
        {
            tmp3.push_back(tmp2.at(i));
        }
        if (tmp1 == tmp3)
        {
            return (word);
            break;
        }
        else continue;
    }
    return "";  
}

};
