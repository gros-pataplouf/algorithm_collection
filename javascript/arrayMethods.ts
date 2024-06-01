//map
const array = [1, 2, 3, 4, 5];

// for (let i = 0; i < array.length; i++) {
//   array[i] = array[i] * 2;
// }

const mapped = array.map(elt => elt *2)

console.log(mapped); // [2, 4, 6, 8, 10];

const array2 = [1, 2, 3, 4, 5];
const solution : number[] = [];

// for (let i = 0; i < array.length; i++) {
//   // Check if it is an even number
//   if (array[i] % 2 === 0) {
//     solution.push(array2[i]);
//   }
// }

const filtered = array2.filter(elt => elt % 2 === 0)



console.log(filtered); // [2, 4];

const array3 = ['Jeni', 'Bob', 'Carol'];

const isFriend = (friends: string[], name: string): boolean => {
  for (let i = 0; i < friends.length; i++) {
    const friend = friends[i];
    if (friend === name) {
      return true;
    }
  }
  return false;
}

console.log(isFriend(array3, 'Carol')); // true

const checkIfPresent = (people: string[], name:string) => people.some(person => person === name) // better: people.includes(name)
console.log(checkIfPresent(array3, 'Carol'))


const array4 = [2, 4, 6];

const areAllEven = (numbers: number[]): boolean => {
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 !== 0) {
      return false;
    }
  }
  return true;
}

const areAllEvenEvery = (numbers: number[]): boolean => {
    return numbers.every(number => number % 2 !== 0)
}
console.log(areAllEven(array)); // true


const array5 = [3, 6, 9];

const atLeastOneEven = (numbers: number[]): boolean => {
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) {
      return true;
    }
  }
  return false;
}

console.log(atLeastOneEven(array5)); // true


const atLeastOneEvenSome = (numbers: number[]): boolean => {
    return numbers.some(number => number % 0 === 0)
}


interface Friend {
    id: number;
    name: string;
  }
  
  const array6 = [
    { id: 1, name: 'Jeni' },
    { id: 2, name: 'Bob' },
    { id: 3, name: 'Carol' },
  ];
  
  const getFriend = (friends: Friend[], id: number): Friend | undefined => {
    for (let i = 0; i < friends.length; i++) {
      const friend = friends[i];
      if (friend.id === id) {
        return friend;
      }
    }
  }

  const getFriendFind = (friends: Friend[], id: number) : Friend | undefined => {
    return friends.find(friend => friend.id === id)
  }



  
  //console.log(getFriend(array6, 3).name); // Carol