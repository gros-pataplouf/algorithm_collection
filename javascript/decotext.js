function wrapper(orgFn) {
    return function(...args) {
        for (let i in args) {
            args[i] = args[i] / 2
            
        }
        console.log(args)
        return orgFn(...args)
    }
}

function consoleLog(arg) {
    console.log(arg)
}

function outerLoop(lower, higher, fn, arg) {
    for (let i = lower; i < higher; i++) {
        fn(arg)
    }
}


function loop(height, width, outerLoop) {
    const matrix = Array(height).fill([]).map((elt, jndex) => Array(width).fill(0).map((elt, index) => (index + 1) * (jndex + 1)))
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            console.log(matrix[i][j])
        }
    }

}

const wrapperLoop = wrapper(loop)
console.log(wrapperLoop(6, 4))