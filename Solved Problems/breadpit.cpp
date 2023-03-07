
#include <iostream>
#include <fstream>
#include <list>
#include <iterator>

using namespace std;

void recur(int pos,list<int>* matrix, int rem, long mod, int* output, int n, int q){
    int nChildren = matrix[pos].size();
    
    if(nChildren == 0){
        int iter = 0;
        while(rem+(iter*mod)<q){
            output[rem+iter*mod] = pos;
            iter++;
        }
    }else{
        long diff = mod;
        if(mod>q){
            recur(matrix[pos].front(),matrix,rem,mod,output,n,q);
            return;
        }
        mod *= nChildren;
        int iter = 0;
        for(list<int>::iterator it = matrix[pos].begin();it != matrix[pos].end();it++){
            if(rem+iter*diff >= q){
                break;
            }
            recur(*it,matrix,rem+iter*diff,mod,output,n,q);
            iter++;
        }
    }
}


    
int main()
{
    
    int n = 0;
    int q = 0;
    
    cin>>n;
    cin>>q;
    
    list<int> *adjList = new list<int>[n];
    
    int* output = new int[q];
    for(int i=0;i<q;i++){
        output[i] = 0;
    }
    
    int parentNode;
    
    for(int i=1;i<n;i++){
        cin >> parentNode;
        adjList[parentNode].push_back(i);
    }
    
    recur(0,adjList,0,1,output,n,q);
    
    for(int i=0;i<q;i++){
        cout<<output[i]<<endl;
    }
    
    return 0;
}