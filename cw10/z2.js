const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const inp = q => new Promise(resolve => rl.question(q, a => resolve(a)));

async function main() {
  const numbers = await inp('podział: ');
  const arr = numbers.split(' ').map(a => Number(a));

  const newArr = [...Array(arr[0])].map(a => 0);

  arr.forEach(element => {
    let i = 0;
    while (element) {
      newArr[i]++;
      i++;
      element--;
    }
  });

  console.log(JSON.stringify(newArr));

  rl.close();
}

main();
