/*
BEGIN ANNOTATION
PROBLEM URL: https://nasouth22d1.kattis.com/problems/branchmanager
TAGS: Trees, Largest Common Ancestor
EXPLANATION: First tried in python, turns out to be too slow :(
When iterating through the tree, we can number the leaf nodes in order.
Logically, if one visits a higher leaf node, all leaf nodes with a lower value can now not be visited.
From there we can recurse upwards and express parent nodes as the range of leaf nodes they encompass.
If a parent node is visited successfully, all nodes lower than the bottom range are now off limits.
But a node within the range is still valid.
We recursively iterate through the tree to implement these values as a pair in an array.
Then check with each visiting person whether they are above the lowest possible value.
END ANNOTATION
*/

#include <iostream>
#include <iterator>
#include <list>
#include <tuple>
#include <utility>

using namespace std;

int counter = -1;

pair <int,int> recur(int pos, list<int>* adjList, pair<int,int>* value){
    int low = counter+1;
    int high = counter+1;
    adjList[pos].sort();
    for(list<int>::iterator it = adjList[pos].begin();it != adjList[pos].end();it++){
        pair <int,int> holder;
        holder = recur(*it,adjList,value);
        if(low > holder.first){
            low = holder.first;
        }
        if(high < holder.second){
            high = holder.second;
        }
    }
    if(adjList[pos].size()==0){
        counter ++;
        low = counter;
        high = counter;
    }
    value[pos] = make_pair(low,high);
    pair<int,int> temp(low,high);
    return temp;
} 

int main()
{
    int c,p;
    
    cin>>c;
    cin>>p;
    
    list<int>* adjList = new list<int>[c];
    pair <int,int>* value = new pair <int,int>[c];
    
    for(int i=1;i<c;i++){
        int a,b;
        cin>>a>>b;
        adjList[a-1].push_back(b-1);
    }
    
    recur(0,adjList,value);
    
    int lowest = 0;
    int people = 0;
    for(int i=0;i<p;i++){
        int person;
        cin>>person;
        person--;
        
        pair<int,int> pVal = value[person];
        if(pVal.second < lowest){
            cout<<people;
            exit(0);
        }else if(pVal.first > lowest){
            lowest = pVal.first;
        }
        people++;
    }
    cout<<people;
}
