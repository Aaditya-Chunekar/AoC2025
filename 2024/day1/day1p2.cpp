
#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> lt;
    vector<int> rt;
    unordered_map<int,int> mp;
    // Open the file for reading
    ifstream f("day1.ip");
    
    // Always check if the file opened successfully in C++
    if (!f.is_open()) {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    int left_num, right_num;
    
    // Reads two integers at a time until the end of the file
    while (f >> left_num >> right_num) {
        lt.push_back(left_num);
        rt.push_back(right_num);
        mp[right_num]++;
    }

    // ifstream closes automatically when it goes out of scope, 
    // but you can call it manually if preferred:
    f.close();
    long long ans=0;
    for(int l:lt)
    {
        ans+=l*mp[l];
    }
    cout<<ans<<endl;
    return 0;
}