
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
