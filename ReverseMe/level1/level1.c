#include <stdio.h>
#include <string.h>

void Goodjob() {
	printf("Good job.\n");
}

void Nope() {
	printf("Nope.\n");
}

int main() {
	char tmp[100];
	printf("Please enter key: ");
	scanf("%s", tmp);
	if (strcmp(tmp, "__stack_check") == 0)
		Goodjob();
	else
		Nope();
	return 0;
}