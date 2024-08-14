#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "Strings.h"
#include "MN.h"
#define LIMIT 32
#define NC '\0'
#define BLANK ' '
#define SLASH '/'
#define PLUS '+'
#define MINUS '-'

// Function to extract unsigned numerator from the given mixed number
int getNumerator(MN this) {
    return abs(this->rn->N);
}

// Function to extract denominator from the given mixed number
int getDenominator(MN this) {
    return this->rn->D;
}

// Function to extract unsigned whole number from the given mixed number
int getWhole(MN this) {
    return (getNumerator(this) / getDenominator(this));
}

// Function to reduce the given mixed number to proper form
void reduceMixedNumber(MN this) {
    reduce(this->rn);
}

// Function to create a new mixed number from a string
MN createMixedNumberFromString(char *str) {
    int sign = 1, whole = 0, numerator = 0, denominator = 1;
    Strim(str);

    if (str[0] == MINUS) {
        sign = -1;
        str++;
    }

    sscanf(str, "%d", &whole);
    char *spacePos = strchr(str, BLANK);
    if (spacePos != NULL) {
        str = spacePos + 1;
        sscanf(str, "%d", &numerator);
        char *slashPos = strchr(str, SLASH);
        if (slashPos != NULL) {
            str = slashPos + 1;
            sscanf(str, "%d", &denominator);
        }
    }

    if (denominator == 0) {
        denominator = 1;
    }

    return createMixedNumber(sign, whole, numerator, denominator);
}

// Function to create a new mixed number
MN createMixedNumber(int sign, int whole, int numerator, int denominator) {
    MN result = (MN)malloc(sizeof(MN));
    result->rn = newI((sign * (((abs(whole) * abs(denominator)) + abs(numerator)))), abs(denominator));
    return result;
}

// Function to get the sign of the mixed number
int getSign(MN this) {
    return (this->rn->N < 0) ? -1 : 1;
}

// Function to get the whole number part of the mixed number
int getWholeNumber(MN this) {
    return getWhole(this);
}

// Function to get the numerator part of the mixed number
int getNumeratorPart(MN this) {
    return (getNumerator(this) % getDenominator(this));
}

// Function to get the denominator part of the mixed number
int getDenominatorPart(MN this) {
    return getDenominator(this);
}

// Function to invert the given mixed number
void invertMixedNumber(MN this) {
    invert(this->rn);
}

// Function to add two mixed numbers
void addMixedNumbers(MN this, MN that) {
    add(this->rn, that->rn);
    reduceMixedNumber(this);
}

// Function to subtract one mixed number from another
void subtractMixedNumbers(MN this, MN that) {
    subtract(this->rn, that->rn);
    reduceMixedNumber(this);
}

// Function to multiply two mixed numbers
void multiplyMixedNumbers(MN this, MN that) {
    multiply(this->rn, that->rn);
    reduceMixedNumber(this);
}

// Function to divide one mixed number by another
void divideMixedNumbers(MN this, MN that) {
    divide(this->rn, that->rn);
    reduceMixedNumber(this);
}

// Function to compare two mixed numbers
int compareMixedNumbers(MN this, MN that) {
    return compareTo(this->rn, that->rn);
}

// Function to convert mixed number to string
char *mixedNumberToString(MN this) {
    char wholeStr[LIMIT], numeratorStr[LIMIT], denominatorStr[LIMIT];
    int wholeLen, numeratorLen, denominatorLen, needed;
    char *result = NULL, *ptr;

    wholeLen = snprintf(wholeStr, LIMIT, "%d", getWholeNumber(this));
    if (wholeLen < LIMIT) {
        numeratorLen = snprintf(numeratorStr, LIMIT, "%d", getNumeratorPart(this));
        if (numeratorLen < LIMIT) {
            denominatorLen = snprintf(denominatorStr, LIMIT, "%d", getDenominatorPart(this));
            if (denominatorLen < LIMIT) {
                needed = 1 + wholeLen + 1 + numeratorLen + 1 + denominatorLen + 1;
                result = malloc(needed);
                if (result != NULL) {
                    ptr = result;
                    if (getSign(this) < 0) {
                        strcpy(ptr, "-");
                        ptr++;
                    }
                    strcpy(ptr, wholeStr);
                    ptr += wholeLen;
                    strcpy(ptr, " ");
                    ptr++;
                    strcpy(ptr, numeratorStr);
                    ptr += numeratorLen;
                    strcpy(ptr, "/");
                    ptr++;
                    strcpy(ptr, denominatorStr);
                }
            }
        }
    }
    return result;
}
