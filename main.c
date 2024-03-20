#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

const char* filter_string(const char* content) {
    int size = strlen(content);
    char* extracted_string = (char*)malloc(size);
    int i = 0, j = 0;

    for (i = 0; i < size; i++)
        if (isalpha(content[i]))
            extracted_string[j++] = tolower(content[i]);

    return extracted_string;
}

const int is_palindrome(const char* content) {
    int size = strlen(content);

    for (int i = 0; i < size/2; i++)
        if (content[i] != content[size-i-1])
            return 0;

    return 1;
}

int main() {
    char* user_content = (char*)malloc(2000); 
    
    printf("Enter a string: ");
    scanf("%[^\n]", user_content);

    const char* extracted_string = filter_string(user_content);
    printf("Extracted String: %s\n", extracted_string);
    printf(is_palindrome(extracted_string) ? "Yes, it is\n" : "No, it is not\n");
    
    return 0;
}