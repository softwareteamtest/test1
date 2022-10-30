#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
	string s;
	int i,j,k,count[1010],y=0,n,sum=0;
	getline(cin,s);
	n=s.size();
	for(i=1;i<n-1;i++)
	{
		
		for(j=1; ;j++)
		{
			//cout<<"11"<<endl;
			if(j+i>=n||i-j<0)
			{
				count[y]=(j-1)*2+1;
				y++;
				break;
			}
			if(s[i-j]==s[i+j])
			{
			
				continue;
			}
			else
			{
				count[y]=(j-1)*2+1;
				y++;
				break;
			}
			
		}
		
		
		
		
	}
	
	
	
		for(i=0;i<n;i++)
	{
		
		for(j=0; ;j++)
		{
			//cout<<"11"<<endl;
			if(j+i>=n||i-j<0)
			{
				count[y]=j*2;
				y++;
				break;
			}
			if(s[i-j]==s[i+j+1])
			{
			
				continue;
			}
			else
			{
				count[y]=j*2;
				y++;
				break;
			}
			
		}
		
		
		
		
	}
	

//	cout<<y<<"yzhi"<<endl;
	sort(count,count+y);
//	for(i=0;i<y;i++)
//	{
//		cout<<count[i]<<endl;
//	}
	cout<<count[y-1]<<endl;
}
