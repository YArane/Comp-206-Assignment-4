/*Program: login.c
 *Authors: Yarden & Daniel
 *Date created: 150405
 *Last modified 150405
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*returns whether the username and password match an entry within members.csv*/
int validateCredentials(char *usernameInput, char *passwordInput){
	FILE *file;
	//open file
	if((file=fopen("members.csv", "r")) == 0){
		printf("error reading members.csv.\n");
		return -1;
	}
	//reading a line
	char *line;
	int bytes = 200;
	if((line = (char *) malloc(bytes+1)) == 0){
		printf("error readding from file.\n");
		return -1;
	}
	char username[32], password[32];
	while(getline(&line, &bytes, file) > 0){
		//parsing the line
		sscanf(line, "%s %s", username, password);
		//validating
		if(strcmp(usernameInput, username) == 0 && strcmp(passwordInput, password) == 0)
			return 1;		
	}
	return 0;

}

int main(){
	/* receive username and password from Welcome.html
		 * generate an error web page with a link back to the  welcome page
		 * display a sucess page with a link to the topics update page
	     ^generate these redirection pages using printf
	*/
	int length = atoi(getenv("CONTENT_LENGTH"));
	printf("%d", validateCredentials("daniel", "yarden"));	
	
}
