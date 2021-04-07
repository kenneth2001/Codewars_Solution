#include <stdbool.h>
#include <stddef.h>

size_t count_sheep(const bool *sheep, size_t count) {
  int i, total = 0;
  for (i = 0; i < count; i++){
    if (sheep[i] == true){
      total++;
    }
  }
  return total;
}
