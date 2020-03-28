#include <iostream>
#include <map>
using namespace std;
int main(){
int arrsize, arr[200000];
cin>>arrsize;
map<int,int> freq;
long long sum = 0, x;
for(int i = 0; i < arrsize; i++){
	cin>>x;
	arr[i] = x;
	sum += x;
	freq[x]++;
}
int res[200000], cnt=0, s;
for(int i = 0 ; i < arrsize; i++){
	s = sum - arr[i];
	
	if(s % 2 ==0){
		s = s >> 1;
		if(freq[s]!=0)
		    if((arr[i] == s && freq[s] > 1) || arr[i] != s)
			        res[cnt++] = i + 1;
		    
	}
}
cout<<cnt<<endl;
for(int i = 0; i < cnt; i++)
	cout<<res[i]<<" ";

}
