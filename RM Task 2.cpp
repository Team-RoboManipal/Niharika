//1
#include<iostream>
int main(){
    char temp;
    std::string st;
    std::cout << "Enter the text:";
    std::cin >> st;
    int n = st.length();
    for(int i=1; i<n-1; i++){
        for(int j=0; j<n-i-1; j++){
            if(st[j]>st[j+1]){
                temp=st[j];
                st[j]=st[j+1];
                st[j+1]=temp;
            }
        }
    }

    std::cout << st;

    return 0;
}

//6
#include <iostream>

int main() {
    int i, j, m, n, p, q, k;
    int A[10][10], B[10][10],C[10][10];
    std::cout<<"enter dimension for a \n";
    std::cin>>m>>n;
    std::cout<<"\n enter dimension for b\n";
    std::cin>>p>>q;
    
    if(n!=p){
        std::cout<<"Enter sq matrix \n";
        exit(0); }
    std::cout<<"enter elements for a \n";
    for (i=0;i<m;i++){
        for(j=0;j<n;j++)
            std::cin>>A[i][j];
    }
    std::cout<<"\n enter elements for b\n";
    for(i=0;i<p;i++){ 
        for(j=0;j<q;j++)
            std::cin>>B[i][j];
    }

    for(i=0;i<m;i++) {
        for(j=0;j<q;j++) {
            C[i][j]=0;
            for(k=0;k<n;k++)
                C[i][j]=C[i][j]+A[i][k]*B[k][j];
        }
    }
    std::cout<<"\n The product matrix is \n";
    for(i=0;i<m;i++){
        for(j=0;j<q;j++)
            std::cout<<C[i][j]<<"\t";
        std::cout<<"\n";
}


    return 0;
}


//3
#include <iostream>

int main() {
    int i,j,n,temp, pos, small;
    char x;
    int a[10];
    std::cout<<"enter dimension for a \n";
    std::cin>>n;
    
 
    std::cout<<"enter elements for a \n";
    for(i=0;i<n;i++)
        std::cin>>a[i]; 
        
    std::cout<<"enter 's' or 'b' \n";
    std::cin>>x;    
    
    switch(x){
        case 'b':
            for(i=0;i<n-1;i++) { 
                for(j=0;j<n-i-1;j++) {
                    if(a[j]>a[j+1]){ 
                        temp=a[j];
                        a[j]=a[j+1];
                        a[j+1]=temp;
                    }
                }
            }
            for(i=0;i<n;i++)
                std::cout<<a[i]<<"\t"; 
        
        
        case 's':
            for(i = 0; i < n-1; i++) { 
                pos = i; 
                small = a[i];
                for(j=i+1; j<n; j++) { 
                    if(small > a[j]) { 
                        pos = j; 
                        small = a[j]; 
                    }
                }
            a[pos] = a[i]; 
            a[i] = small;
            }
        for(i=0;i<n;i++)
            std::cout<<a[i]<<"\t"; 

    }
    
        

    return 0;
}

//8
