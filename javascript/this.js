class User {
  constructor(name) {
    this.name = name;
  }
  getName() {
    return this.name;
  }
  printSeatNumber() {
    console.log('The seats have not been set');
  }
}

class Meeting {
  constructor(users) {
    const presenter = users[0];
    this.getPresenterName = presenter.getName.bind(presenter); //broken code was: this.getPresenterName = presenter.getName
    this.setUserSeats(users);
  }
  setUserSeats(users) {
    // for (let i = 0; i < users.length; i++) { //broken code : var
    //   users[i].printSeatNumber = () => {
    //     console.log(i);
    //   }
    // }
    for (var i = 0; i < users.length; i++) {
      users[i].printSeatNumber = (function(seatNumber){
        return () => console.log(seatNumber);
      })(i);
      }
    }
  }


const users = [new User('Jeni'), new User('Dan'), new User('Carol')];
const meeting = new Meeting(users);

// Broken results
console.log(meeting.getPresenterName()); // undefined (expected ‘Jeni’)
users[0].printSeatNumber(); // 3 (expected 0)
users[1].printSeatNumber(); // 3 (expected 1)
users[2].printSeatNumber(); // 3 (expected 2)


// Immediately Invoked Function Expressions (IIFE) are JavaScript functions that are executed immediately after they are defined. They are typically used to create a local scope
// for variables to prevent them from polluting the global scope.

///
// (function() {
//   // IIFE code block
//   var localVar = 'This is a local variable';
//   console.log(localVar); // Output: This is a local variable
// })();
///