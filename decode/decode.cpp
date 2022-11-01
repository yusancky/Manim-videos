#include <cmath>
#include <cstdio>
using namespace std;

long long int pow_n_2(long long int n){
  return n * n;
}

int k;
long long int n,e,d,p,q,b,c,delta;

int main(){
  scanf("%d",&k);
  for (int _ = 1;_ <= k;_++){
    scanf("%lld%lld%lld",&n,&e,&d);
    b = e * d - n - 2,c = n;
    delta = b * b - 4 * c;
    if (delta < 0) printf("NO\n");
    else if (pow_n_2((int)(round(sqrt(delta)) + 0.1)) != delta) printf("NO\n");
    else{
      p = -(int)(round(sqrt(delta)) + 0.1) - b;
      q = (int)(round(sqrt(delta)) + 0.1) - b;
      if (p % 2 == 1 || q % 2 == 1 || p <= 0) printf("NO\n");
      else printf("%lld %lld\n",p / 2,q / 2);
    }
  }
  return 0;
}