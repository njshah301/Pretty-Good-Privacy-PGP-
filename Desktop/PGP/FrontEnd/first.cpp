#include <iostream>
#include <bits/stdc++.h> 
#include<unordered_set>
#include<unordered_map>
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);
#define ll long long int

using namespace std;

void solve(){
    ll N;
    cin>>N;
    deque <int> dq;
    ll temp;
    for(int i=0;i<N;i++)
    {
        cin>>temp;
        dq.push_back(temp);
    }

    ll ans=1;
    ll track=INT_MIN;
    if(dq.front()>dq.back())
    {
        track=dq.back();
        dq.pop_back();
    }
    else
    {
        track=dq.front();
        dq.pop_front();
    }
    
    while(dq.size())
    {
        ll first=dq.front();
        ll last=dq.back();
        ll maxi=max(first,last);
        ll mini=min(first,last);
        if(mini>=track)
        {
            track=mini;
            if(mini==first)
            {
                dq.pop_front();
            }
            else
            {
                dq.pop_back();
            }
            ans++;
        }
        else if(maxi>=track)
        {
            track=maxi;
            if(maxi==first)
            {
                dq.pop_front();
            }
            else
            {
                dq.pop_back();
            }
            ans++;
        }
        else
        {
            break;
        }

    }
    cout<<ans<<"\n";
}
int main() {
	// your code goes here
fast;

ll T;
cin>>T;
ll cnt=1;
while(T--){
    cout<<"Case #"<<cnt<<": ";
    solve();
    cnt++;
}

	
	
	return 0;
}
//......................................
//.NNNNNN....NNNNN...............JJJJJ..
//.NNNNNN....NNNNN...............JJJJJ..
//.NNNNNNN...NNNNN...............JJJJJ..
//.NNNNNNNN..NNNNN...............JJJJJ..
//.NNNNNNNN..NNNNN...............JJJJJ..
//.NNNNNNNNN.NNNNN...............JJJJJ..
//.NNNNNNNNN.NNNNN...............JJJJJ..
//.NNNNNNNNNNNNNNN...............JJJJJ..
//.NNNNNNNNNNNNNNN...............JJJJJ..
//.NNNNNNNNNNNNNNN...............JJJJJ..
//.NNNNN.NNNNNNNNN...............JJJJJ..
//.NNNNN.NNNNNNNNN........ JJJJ..JJJJJ..
//.NNNNN..NNNNNNNN........ JJJJ..JJJJJ..
//.NNNNN...NNNNNNN........ JJJJJJJJJJJ..
//.NNNNN...NNNNNNN........ JJJJJJJJJJJ..
//.NNNNN....NNNNNN.........JJJJJJJJJJ...
//.NNNNN....NNNNNN..........JJJJJJJJ....
//......................................