#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

void ____syscall_malloc() {
	puts("Good job.");
	return;
}

void ___syscall_malloc() {
	puts("Nope.");
	exit(1);
}

int main() {
	int ret;
	size_t len;
	char tmp[4];
	char val[9];
	char input[31];
	bool boule;
	int uret;

	printf("Please enter key: ");
	ret = scanf("%s23s", input);
	if (ret != 1)
		___syscall_malloc();
	if (input[1] != '2')
		___syscall_malloc();
	if (input[0] != '4')
		___syscall_malloc();
	fflush(0);
	memset(val, 0, 9);
	val[0] = '*';
	tmp[3] = 0;
	int i = 2;
	int j = 1;
	while (1) {
		boule = false;
		if (strlen(val) < 8) {
			len = i;
			boule = len < strlen(input);
		}
		if (boule != true)
			break;
		tmp[0] = input[i];
		tmp[1] = input[i + 1];
		tmp[2] = input[i + 2];
		val[j] = atoi(tmp);
		i += 3;
		j += 1;
	}
	uret = strcmp(val, "********");
	if (uret == -2)
		___syscall_malloc();
	else if (uret == -1)
		___syscall_malloc();
	else if (uret == 0) {
		____syscall_malloc();
		return 0;
	}
	else if (uret == 1)
		___syscall_malloc();
	else if (uret == 2)
		___syscall_malloc();
	else if (uret == 3)
		___syscall_malloc();
	else if (uret == 4)
		___syscall_malloc();
	else if (uret == 5)
		___syscall_malloc();
	else if (uret == 115)
		___syscall_malloc();
	else
		___syscall_malloc();
	return 0;
}