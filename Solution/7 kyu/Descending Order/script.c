#include <inttypes.h>
#include <string.h>

void heapify(int *arr, int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[largest] > arr[l]) {
        largest = l;
    }

    if (r < n && arr[largest] > arr[r]) {
        largest = r;
    }

    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heapSort(int *arr, int n) {
    int i;
    for (i = n / 2 - 1; i > -1; i--) {
        heapify(arr, n, i);
    }
    int temp;
    for (i = n - 1; i > 0; i--) {
        temp = arr[i];
        arr[i] = arr[0];
        arr[0] = temp;
        heapify(arr, i, 0);
    }
}

uint64_t descendingOrder(uint64_t n) {
    int arr[20] = {0}, i = 0, size = 0;

    while (n) {
        arr[i] = n % 10;
        n = n / 10;
        size++;
        i++;
    }
    
    heapSort(arr, size);
  
    uint64_t ans = 0;
    for (i = 0; i < size; i++) {
        ans = ans * 10 + arr[i];
    }
    return ans;
}
