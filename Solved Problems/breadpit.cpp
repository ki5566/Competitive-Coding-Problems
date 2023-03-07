/*
BEGIN ANNOTATION
PROBLEM URL: https://open.kattis.com/problems/breadpit
TAGS: Trees, Mod
EXPLANATION: Seeing as there are 3*10^5 nodes and 3*10^5 breads, simulation is not possible.
Note that for a parent node with two leaf children, the bread will alternate between the two.
Or alternatively, the bread index which are === 0 (mod 2) go to the first child and 1 (mod 2) go to the second child.
Thus when iterating through each node, we can identify a mod and remainder value, such that the bread at those index
will pass through that node. If the node is a leaf, append the node value to the correct indices.
Edge cases: modulus grows larger than bread size -> ignore modulus growth, move value of leftmost leaf node to index
            remainder grows larger than bread size -> break instantly as no bread will reach this point
END ANNOTATION
*/
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
