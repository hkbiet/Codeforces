#include<stdio.h>

int main(){


	int weight;
	scanf("%d",&weight);

	for(int i = 1; i <=weight; i++){

		if(i%2 != 0){
		
			continue;
		}
	
		for(int j = 1; j<=weight; j++){
			
			if(j%2 != 0){
			
				continue;
			}

			if(i+j == weight){
			
				printf("YES");
				return 0;
			
			}

		
		
		
		}
	
	
	
	}

	printf("NO");
	return 0;
}
