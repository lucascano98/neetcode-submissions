public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
            return false;
        
        Dictionary<char, int> dict = new Dictionary<char, int>();
        foreach (char c in s)
        {
            dict[c] = dict.GetValueOrDefault(c) + 1;
        }

        foreach (char c in t)
        {
            if (!dict.ContainsKey(c))
                return false;
            else
                dict[c] -= 1;
        }

        if (dict.Any(x => x.Value != 0))
            return false;
        else 
            return true;
    }
}
