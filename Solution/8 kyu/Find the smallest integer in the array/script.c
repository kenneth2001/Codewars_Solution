#include <stddef.h>

int find_smallest_int(int *vec, size_t len)
{
    int idx = 0;
    for (size_t i = 1; i < len; i++){
        if (vec[idx] > vec[i])
          idx  = i;
    }
    return vec[idx];
}
