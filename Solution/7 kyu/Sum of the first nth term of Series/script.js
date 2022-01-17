function SeriesSum(n){
    let ans = 0.0
    for(let i=0; i<n; i++){
      ans += 1.0 / (1 + 3 * i)
    }

    return ans.toFixed(2)
  }

console.log(SeriesSum(2))