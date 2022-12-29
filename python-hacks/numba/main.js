let num = 1;
const repeat = 1000000000;
const startTime = performance.now();
for (let c = 0; c < repeat; c++) {
    num = num + num - num
}
console.log(num)
const endTime = performance.now();

console.log((endTime-startTime)/1000);
