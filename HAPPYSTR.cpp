#include <bits/stdc++.h>

using namespace std;


int main() {
  int t;
  cin>>t;
  while(t--){
      string s;
      cin>>s;
      int c = 0;
      bool isthree = false;
      for (int i = 0; i < s.size(); i++)
       {
          if(s[i] == 'a'||s[i] == 'e'||s[i] == 'i'||s[i]=='o'||s[i] == 'u')
           {
              c++;
              if(c>=3)
               {
                  cout<<"Happy"<<endl;
                  isthree = true;
                  break;
               }
           }
          else c = 0;
       }
      if(!isthree){
          cout<<"Sad"<<endl;
      }
  }
  
  return 0;
}