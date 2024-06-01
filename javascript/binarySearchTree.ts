export class BinaryNode {
    data: number
    right: BinaryNode | null
    left: BinaryNode | null
    constructor(data: number, left: BinaryNode | null, right: BinaryNode | null) {
        this.data = data
        this.left = left
        this.right = right
    }
}
export class BinarySearchTree {
    root: BinaryNode | null;
    constructor() {
      this.root = null;
    }
    insert(data: number): BinarySearchTree {
      const newNode = new BinaryNode(data, null, null)
      if (this.root == null) {
        this.root = newNode; // base case => insertion
        return this;
      }  
      else {
        let currentRoot = this.root
        while (true) {
          if (data > currentRoot.data) {
            if (!currentRoot.right) {
              currentRoot.right = newNode;
              return this 
            }
            currentRoot = currentRoot.right
          } else if (data <= currentRoot.data) {
            if (!currentRoot.left) {
              currentRoot.left = newNode;
              return this
            }
            currentRoot = currentRoot.left;
          }
        }
      }
    }
    search(data: number): BinaryNode | null {
      let currentRoot = this.root
      if (currentRoot) {
        while (currentRoot) {
          if (currentRoot.data === data ) {
            return currentRoot
          } else if (currentRoot.data < data ) {
            currentRoot = currentRoot.right;
          } else {
            currentRoot = currentRoot.left;
          }
        }
      }
      return null;
    }
    findMaxDepth() : number {
      let depthArr = [0];
      let currentRoot = this.root;
      if (!currentRoot) {
        return -1;
      }
      while (currentRoot) {
        if (currentRoot.left) {
          
        }
      }
      return depthArr[0];
    }
  }

  const maxDepthArray:number[] = [-1]
  const findMaxDepth = (node: BinaryNode | null, maxDepth:number, currentDepth:number): number => {
  if (node) {
    currentDepth++;
    if (currentDepth > maxDepth) {
      maxDepth = currentDepth;
    }
    if (node.left) {
      findMaxDepth(node.left, maxDepth, currentDepth)
    }
    if (node.right) {
      findMaxDepth(node.right, maxDepth, currentDepth)
    }
  }
  maxDepthArray.push(maxDepth)
  return maxDepthArray.sort().reverse()[0];
}

interface StackElt {
  depth: number, 
  node: BinaryNode
}


//iterative solution

const findMaxDepthIterative = (root: BinaryNode): number => {
  const stack = [];
  let maxDepth = -1; // Value to return if no node is given

  if (root !== null) {
    // Updates to the correct root depth of 0
    maxDepth = maxDepth + 1;
    // Add the root to the stack
    stack.push({ node: root, depth: maxDepth  });
  }

  while(stack.length !== 0) {
    // Remove top item on the stack and extract the node and its depth
    const { node, depth } = stack.pop();

    // If the node exists, compare it to the current max and add its children to the stack
    if (node !== null) {
      maxDepth = Math.max(maxDepth, depth);
      stack.push({ node: node.right, depth: depth + 1 });
      stack.push({ node: node.left, depth: depth + 1 });
    }
  }

  return maxDepth;
}


  const testTree = new BinarySearchTree()
  const testNumbers : number[] = [23, 4, 50, 100]
  testNumbers.forEach((nr) => testTree.insert(nr))

  console.log(findMaxDepth(testTree.root, -1, -1))
  console.log(testTree)

