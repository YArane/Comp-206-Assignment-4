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
	if((file=fopen("../databases/members.csv", "r")) == 0){
		printf("error reading members.csv.\n");
		return -1;
	}
	//reading a line
	char *line;
	int *bytes_ptr;
	int bytes = 200;
	bytes_ptr = &bytes;
	if((line = (char *) malloc(bytes+1)) == 0){
		printf("error readding from file.\n");
		return -1;
	}
	char username[32], password[32], name[32];
	while(getline(&line, (size_t *) bytes_ptr, file) > 0){
		//parsing the line
		sscanf(line, "%s %s %s", name, username, password);
		//validating
		if(strcmp(usernameInput, username) == 0 && strcmp(passwordInput, password) == 0)
			return 1;		
	}
	return 0;

}

int parseCredentials(char *query, int length, char *username, char *password){
	int i;
	int u = 0;
	int p = 0;
	for(i=0;*(query+i) != '=';i++){}
	i++;
	//copy username
	while(*(query+i) != '&'){
		*(username+u) = *(query+i);
		u++;
		i++;
	}
	*(username+u) = '\0';
	for(;*(query+i) != '=';i++){}
	i++;
	//copy password
	while(i<length){
		*(password+p) = *(query+i);
		p++;
		i++;
	}
	*(password+p) = '\0';
	return 0;
}

int main(){
	/* receive username and password from index.html
		 * generate an error web page with a link back to the  welcome page
		 * display a sucess page with a link to the topics update page
	     ^generate these redirection pages using printf
	*/
	printf("%s%c%c\n",
	  "Content-Type:text/html;charset=iso-8859-1",13,10);
	printf("<title>Login Page</title>\n");
	int length = atoi(getenv("CONTENT_LENGTH"));
	char string[200];
	fgets(string, length+1, stdin); 
	
	char username[32], password[32];
	parseCredentials(string, length, username, password);
	if(validateCredentials(username, password)){
		printf("<p>login successful. %s</p>", username);
		//printf("<a href=\"../feed.html\"> go to the feed page. </a>");
		printf("<form action=\"MyFacebookPage.py\" method=post><fieldset><input type=\"hidden\" name=\"username\" value=\"%s\"><br><br><input type=\"submit\" value=\"Go to Feed Page\"></fieldset></form>", username);
	}else{
		printf("<p>incorrect login information</p>");
		printf("<a href=\"../index.html\"> please try again. </a>");	
	}
	return 0;	
}
